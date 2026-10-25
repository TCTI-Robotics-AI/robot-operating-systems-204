#!/usr/bin/env python3
"""Bounded offline Arabic recognition; optionally call the ROS LED service.

Run with the native Pi Python environment. GPIO remains owned by its native
agent; this tool controls it only through the ROS service in the container.
"""
import argparse
import array
import json
import math
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import wave

from course204.commands import intent, normalize
from course204.speech import load_model
from course204.spoken_replies import play_acknowledged_reply, validate_acknowledgement, validate_reply_cache


ROS_REQUEST = '''import json,sys,rospy
from std_msgs.msg import Bool
from course_common.srv import SetLamp
rospy.init_node("course204_voice_command",anonymous=True)
rospy.wait_for_service("/lamp/set",timeout=10)
simulated=rospy.wait_for_message("/lamp/simulated",Bool,timeout=5).data
if simulated:
    raise RuntimeError("Expected the physical LED backend, got a simulated lamp")
requested=sys.argv[1]=="true"
result=rospy.ServiceProxy("/lamp/set",SetLamp)(requested)
print(json.dumps({"success":result.success,"state":result.state,"simulated":simulated,"message":result.message},ensure_ascii=False))
if not result.success or result.state != requested:
    raise RuntimeError("The device did not acknowledge the requested state")
'''


def recognize(model, path):
    from vosk import KaldiRecognizer
    with wave.open(str(path), "rb") as audio:
        if (audio.getnchannels(), audio.getsampwidth(), audio.getframerate(), audio.getcomptype()) != (1, 2, 16000, "NONE"):
            raise ValueError("Expected mono 16-bit PCM WAV at 16000 Hz")
        recognizer = KaldiRecognizer(model, 16000)
        recognizer.SetWords(True)
        results = []
        samples = array.array("h")
        while True:
            data = audio.readframes(4000)
            if not data:
                break
            samples.frombytes(data)
            if recognizer.AcceptWaveform(data):
                results.append(json.loads(recognizer.Result()))
        results.append(json.loads(recognizer.FinalResult()))
    text = " ".join(part.get("text", "") for part in results).strip()
    words = [word for part in results for word in part.get("result", [])]
    confidence = sum(word["conf"] for word in words) / len(words) if words else 0.0
    rms = math.sqrt(sum(value * value for value in samples) / len(samples)) if samples else 0
    peak = max((abs(value) for value in samples), default=0)
    return {"text": text, "mean_word_confidence": round(confidence, 4),
            "recorded_seconds": round(len(samples) / 16000, 2),
            "rms_dbfs": round(20 * math.log10(rms / 32768), 1) if rms else None,
            "peak_dbfs": round(20 * math.log10(peak / 32768), 1) if peak else None}


def decide(text, confidence, minimum_confidence):
    command = intent(text)
    if command is None:
        return None, "No exact approved command; no GPIO action"
    if confidence < minimum_confidence:
        return None, "Recognition confidence below threshold; no GPIO action"
    return command, "Exact approved command"


def amplify_pcm(samples, gain_db):
    factor = 10 ** (gain_db / 20)
    clipped = 0
    amplified = array.array("h")
    for sample in samples:
        value = round(sample * factor)
        if not -32768 <= value <= 32767:
            clipped += 1
        amplified.append(max(-32768, min(32767, value)))
    return amplified, round(100 * clipped / len(samples), 4) if samples else 0.0


def recognize_whisper(model, path, gain_db=0, hotwords=None):
    import numpy as np
    with wave.open(str(path), "rb") as audio:
        source_rate = audio.getframerate()
        if (audio.getnchannels(), audio.getsampwidth(), audio.getcomptype()) != (1, 2, "NONE") or source_rate not in (16000, 48000):
            raise ValueError("Expected mono 16-bit PCM WAV at 16000 or 48000 Hz")
        samples = array.array("h", audio.readframes(audio.getnframes()))
    if source_rate != 16000:
        import av
        frame = av.AudioFrame.from_ndarray(np.asarray(samples, dtype=np.int16).reshape(1, -1),
                                          format="s16", layout="mono")
        frame.sample_rate = source_rate
        resampler = av.AudioResampler(format="s16", layout="mono", rate=16000)
        frames = resampler.resample(frame) + resampler.resample(None)
        samples = array.array("h", b"".join(item.to_ndarray().tobytes() for item in frames))
    rms = math.sqrt(sum(value * value for value in samples) / len(samples)) if samples else 0
    peak = max((abs(value) for value in samples), default=0)
    amplified, clipped_percent = amplify_pcm(samples, gain_db)
    segments, _ = model.transcribe(
        np.asarray(amplified, dtype=np.float32) / 32768.0,
        language="ar", task="transcribe", beam_size=5, temperature=0,
        max_new_tokens=24, repetition_penalty=1.1, no_repeat_ngram_size=3,
        condition_on_previous_text=False, vad_filter=True,
        vad_parameters={"threshold": 0.35, "min_silence_duration_ms": 500, "speech_pad_ms": 500}, word_timestamps=True,
        hotwords=hotwords)
    segments = list(segments)
    words = [word for segment in segments for word in (segment.words or [])]
    confidence = sum(word.probability for word in words) / len(words) if words else 0
    return {"text": " ".join(segment.text.strip() for segment in segments).strip(),
            "source_sample_rate_hz": source_rate,
            "vocabulary_context": hotwords,
            "beam_size": 5,
            "mean_word_confidence": round(confidence, 4),
            "software_gain_db": gain_db, "clipped_samples_after_gain_percent": clipped_percent,
            "recorded_seconds": round(len(samples) / 16000, 2),
            "rms_dbfs": round(20 * math.log10(rms / 32768), 1) if rms else None,
            "peak_dbfs": round(20 * math.log10(peak / 32768), 1) if peak else None}


def execute(command, container, docker_prefix):
    result = subprocess.run(
        docker_prefix + ["exec", container, "/course-entrypoint.sh", "python3", "-c", ROS_REQUEST,
                         "true" if command == "on" else "false"],
        capture_output=True, text=True, timeout=25, check=True)
    return json.loads(result.stdout)


def execute_and_reply(command, container, docker_prefix, reply_dir=None, playback_device=None):
    response = execute(command, container, docker_prefix)
    validate_acknowledgement(command, response)
    outcome = {"ros_response": response, "executed": True}
    if reply_dir is not None:
        try:
            outcome["reply"] = play_acknowledged_reply(command, response, reply_dir, playback_device)
        except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
            # The ROS request already succeeded. Report a separate playback
            # failure rather than falsely reporting that device control failed.
            outcome["reply"] = {"played": False, "error": str(error)}
    return outcome


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--backend", choices=["vosk", "whisper"], default="vosk")
    parser.add_argument("--gain-db", type=float, default=0, help="Optional Whisper PCM amplification, 0..24 dB")
    parser.add_argument("--hotwords", help="Optional Whisper vocabulary context; does not force an LED intent")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--wav", type=Path)
    source.add_argument("--microphone", action="store_true")
    parser.add_argument("--device", help="ALSA input; auto-select the configured course204_mic when installed")
    parser.add_argument("--duration", type=int, default=5, choices=range(1, 16), metavar="1..15")
    parser.add_argument("--rounds", type=int, default=1, choices=range(1, 11), metavar="1..10")
    parser.add_argument("--minimum-confidence", type=float, default=0.8)
    parser.add_argument("--execute", action="store_true", help="Execute only exact approved LED phrases")
    parser.add_argument("--reply-dir", type=Path, help="Prepared Arabic reply cache; requires --execute")
    parser.add_argument("--playback-device", help="Explicit ALSA playback device for spoken replies")
    parser.add_argument("--container", default="course204-lamp")
    parser.add_argument("--sudo-docker", action="store_true")
    parser.add_argument("--interactive", action="store_true", help="Wait for Enter before each microphone capture")
    parser.add_argument("--countdown", type=int, default=3, choices=range(0, 16), metavar="0..15")
    parser.add_argument("--save-recordings", type=Path, help="Optional private local directory; never publish audio")
    args = parser.parse_args()
    if not 0 <= args.minimum_confidence <= 1:
        parser.error("Confidence must be between 0 and 1")
    if not 0 <= args.gain_db <= 24 or (args.backend != "whisper" and args.gain_db != 0):
        parser.error("Gain must be 0..24 dB and is supported by the Whisper backend")
    if args.device is None:
        args.device = "course204_mic" if Path("/etc/alsa/conf.d/99-course204-microphone.conf").is_file() else "plughw:CARD=Audio,DEV=0"
    if args.microphone and args.device == "course204_mic" and args.gain_db != 0:
        parser.error("course204_mic already amplifies capture; use --gain-db 0 to avoid double gain")
    if args.wav and (args.rounds != 1 or args.interactive):
        parser.error("WAV input supports a single noninteractive round")
    if args.reply_dir is not None:
        if not args.execute or not args.playback_device:
            parser.error("Spoken replies require --execute and an explicit --playback-device")
        validate_reply_cache(args.reply_dir)
    docker = ["sudo", "-n", "docker"] if args.sudo_docker else ["docker"]
    print("Loading Arabic model locally...", flush=True)
    if args.backend == "whisper":
        from faster_whisper import WhisperModel
        model = WhisperModel(str(args.model), device="cpu", compute_type="int8", cpu_threads=4,
                             num_workers=1, local_files_only=True)
    else:
        model = load_model(args.model)
    print("MODEL READY / النموذج جاهز", flush=True)
    for number in range(args.rounds):
        if args.microphone and args.interactive:
            response = input("Enter to record; q to quit / Enter للتسجيل، q للخروج: ")
            if response.strip().lower() == "q":
                break
        with tempfile.TemporaryDirectory(prefix="course204-voice-") as directory:
            path = args.wav or Path(directory) / "command.wav"
            if args.microphone:
                print("Countdown / العد التنازلي: {} seconds".format(args.countdown), flush=True)
                time.sleep(args.countdown)
                print("SPEAK NOW / تحدث الآن: {} seconds".format(args.duration), flush=True)
                subprocess.run(["arecord", "-q", "-D", args.device, "-f", "S16_LE", "-r", "16000",
                                "-c", "1", "-d", str(args.duration), str(path)],
                               check=True, timeout=args.duration + 10)
                if args.save_recordings:
                    args.save_recordings.mkdir(parents=True, exist_ok=True, mode=0o700)
                    saved = args.save_recordings / ("voice-" + time.strftime("%Y%m%d-%H%M%S") + ".wav")
                    shutil.copyfile(path, saved)
                    saved.chmod(0o600)
            started = time.monotonic()
            result = recognize_whisper(model, path, args.gain_db, args.hotwords) if args.backend == "whisper" else recognize(model, path)
            result["backend"] = args.backend
            result["inference_seconds"] = round(time.monotonic() - started, 2)
        command, reason = decide(result["text"], result["mean_word_confidence"], args.minimum_confidence)
        result.update({"normalized_text": normalize(result["text"]), "intent": command,
                       "decision": reason, "executed": False, "round": number + 1})
        print("RECOGNIZED / النص: " + result["text"], flush=True)
        if args.execute and command is not None:
            result.update(execute_and_reply(command, args.container, docker,
                                            args.reply_dir, args.playback_device))
        print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
    print("Voice session finished / انتهت جلسة الصوت", flush=True)


if __name__ == "__main__":
    main()
