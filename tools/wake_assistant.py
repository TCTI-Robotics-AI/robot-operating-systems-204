#!/usr/bin/env python3
"""Local two-stage Arabic wake assistant: يا مساعد, then a five-second command.

Ambient audio is segmented in memory and transcribed through private temporary
WAVs that are overwritten and removed on clean exit. The microphone is closed
during recognition and success replies; buffered readiness audio is discarded.
Only a verified wake phrase arms command capture. No background service is added.
"""
import argparse
import json
import math
import os
from pathlib import Path
import queue
import subprocess
import tempfile
import threading
import time
import wave

from course204.spoken_replies import (
    READY_TEXT, play_ready_prompt, validate_cache_entry, validate_reply_cache)
from course204.wake import SpeechSegmenter, matches_wake_phrase, pcm_rms
from course204.assistant_info import assistant_intent, validate_location


RATE = 48000
BLOCK_BYTES = 960 * 2


def log(event, **values):
    print(json.dumps(dict(event=event, **values), ensure_ascii=False), flush=True)


class Microphone:
    """One ALSA input owner, drained continuously into a bounded queue."""
    def __init__(self, device):
        self.device = device
        self.blocks = queue.Queue(maxsize=400)
        self.error = None
        self.process = self.thread = None

    def __enter__(self):
        arguments = ["arecord", "-q", "-D", self.device, "-t", "raw", "-f", "S16_LE",
                     "-r", str(RATE), "-c", "1"]
        print("INPUT: " + " ".join(arguments), flush=True)
        self.process = subprocess.Popen(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.thread = threading.Thread(target=self._read, daemon=True)
        self.thread.start()
        try:
            for _ in range(5):
                self.read()  # Discard 100 ms of device startup settling.
        except BaseException:
            self.close()
            raise
        return self

    def _read(self):
        try:
            while True:
                block = self.process.stdout.read(BLOCK_BYTES)
                if len(block) != BLOCK_BYTES:
                    self.error = "Microphone stream ended or produced a partial frame"
                    break
                self.blocks.put_nowait(block)
        except queue.Full:
            self.error = "Microphone queue overflow; refusing stale audio"
        except (OSError, ValueError) as error:
            self.error = str(error)
        finally:
            try:
                self.blocks.put_nowait(None)
            except queue.Full:
                pass

    def read(self):
        if self.error:
            raise RuntimeError(self.error)
        try:
            block = self.blocks.get(timeout=3)
        except queue.Empty:
            raise RuntimeError("Microphone read timed out") from None
        if block is None:
            raise RuntimeError(self.error or "Microphone stream ended")
        return block

    def discard_pending(self):
        while True:
            try:
                self.blocks.get_nowait()
            except queue.Empty:
                return

    def close(self):
        if self.process:
            if self.process.poll() is None:
                self.process.terminate()
                try:
                    self.process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    self.process.kill()
                    self.process.wait(timeout=3)
            if self.thread:
                self.thread.join(timeout=3)
            self.process.stdout.close()
            self.process.stderr.close()

    def __exit__(self, *unused):
        self.close()


def listen_utterance(device, minimum_rms):
    with Microphone(device) as microphone:
        print("CALIBRATING INPUT: remain quiet briefly", flush=True)
        levels = sorted(pcm_rms(microphone.read()) for _ in range(30))
        noise = levels[3]
        # Speech or handling noise during calibration must not make the input
        # deaf. Use a low percentile and cap the adaptive part at -40 dBFS.
        threshold = max(minimum_rms, min(0.01, noise * 2.5))
        segmenter = SpeechSegmenter(threshold)
        log("LISTENING_FOR_WAKE", phrase="يا مساعد", threshold_rms=round(threshold, 6))
        while True:
            utterance = segmenter.feed(microphone.read())
            if utterance is not None:
                return utterance


def record_command(device, reply_dir, playback_device):
    with Microphone(device) as microphone:
        play_ready_prompt(reply_dir, playback_device)
        # Drain the readiness playback and any queued self-audio before arming.
        microphone.discard_pending()
        log("SPEAK_COMMAND_NOW", seconds=5)
        captured = b"".join(microphone.read() for _ in range(250))
    if len(captured) != RATE * 5 * 2:
        raise RuntimeError("Incomplete five-second command; no execution")
    return captured


def save_wav(path, pcm):
    with wave.open(str(path), "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(RATE)
        audio.writeframes(pcm)


def dispatch_after_wake(wake_text, capture, process, phrase="يا مساعد"):
    """Keep the wake-to-command boundary independently testable."""
    if not matches_wake_phrase(wake_text, phrase):
        return None
    return process(capture())


def dispatch_command(text, confidence, minimum_confidence, lamp, information):
    """Keep information questions away from the physical ROS service."""
    command = assistant_intent(text)
    result = {"intent": None, "executed": False, "decision": "No exact approved command"}
    if command is None:
        return result
    if not math.isfinite(confidence) or confidence < minimum_confidence:
        result["decision"] = "Recognition confidence below threshold"
        return result
    result.update(intent=command, decision="Exact approved command")
    if command in ("on", "off"):
        result.update(lamp(command))
    else:
        result["information"] = information(command)
    return result


def main():
    import resource
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wake-model", type=Path, required=True)
    parser.add_argument("--command-model", type=Path, required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--playback-device", required=True)
    parser.add_argument("--reply-dir", type=Path, required=True)
    parser.add_argument("--container", default="course204-lamp")
    parser.add_argument("--weather-config", type=Path, help="Explicit city/latitude/longitude JSON")
    parser.add_argument("--tts-python", type=Path, help="Isolated Piper environment for dynamic answers")
    parser.add_argument("--tts-model", type=Path)
    parser.add_argument("--minimum-confidence", type=float, default=0.8)
    parser.add_argument("--minimum-rms", type=float, default=0.0032)
    parser.add_argument("--max-turns", type=int, default=0, help="0 listens until interrupted")
    parser.add_argument("--save-commands", type=Path, help="Optional private command WAVs; ambient/wake audio is not saved")
    args = parser.parse_args()
    if not 0 <= args.minimum_confidence <= 1 or not 0 < args.minimum_rms < 1 or args.max_turns < 0:
        parser.error("Invalid threshold or turn limit")
    if bool(args.tts_python) != bool(args.tts_model):
        parser.error("Dynamic answers require both --tts-python and --tts-model")
    for path in (args.tts_python, args.tts_model):
        if path is not None and not path.is_file():
            parser.error("Dynamic speech path does not exist: " + str(path))
    location = validate_location(json.loads(args.weather_config.read_text(encoding="utf-8"))) if args.weather_config else None
    validate_reply_cache(args.reply_dir)
    validate_cache_entry(args.reply_dir, "ready", READY_TEXT)
    from faster_whisper import WhisperModel
    from voice_lamp import execute_and_reply, recognize_whisper
    from assistant_answer import information_answer, speak_answer
    os.umask(0o077)
    print("LOADING LOCAL WAKE AND COMMAND MODELS; MICROPHONE NOT STARTED YET", flush=True)
    wake_model = WhisperModel(str(args.wake_model), device="cpu", compute_type="int8",
                             cpu_threads=4, num_workers=1, local_files_only=True)
    command_model = WhisperModel(str(args.command_model), device="cpu", compute_type="int8",
                                cpu_threads=4, num_workers=1, local_files_only=True)
    log("MODELS_READY", max_rss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 1))
    turns = 0
    try:
        with tempfile.TemporaryDirectory(prefix="course204-assistant-") as temporary:
            wake_path, command_path = Path(temporary)/"wake.wav", Path(temporary)/"command.wav"
            while not args.max_turns or turns < args.max_turns:
                save_wav(wake_path, listen_utterance(args.device, args.minimum_rms))
                started = time.monotonic()
                wake = recognize_whisper(wake_model, wake_path, 0, "يا مساعد")
                log("WAKE_TRANSCRIPT", text=wake["text"], seconds=round(time.monotonic()-started, 2))
                if not matches_wake_phrase(wake["text"]):
                    log("IGNORED_WITHOUT_WAKE")
                    continue
                log("WAKE_VERIFIED", text=wake["text"])

                def capture():
                    return record_command(args.device, args.reply_dir, args.playback_device)

                def process(pcm):
                    save_wav(command_path, pcm)
                    saved = None
                    if args.save_commands:
                        args.save_commands.mkdir(parents=True, exist_ok=True, mode=0o700)
                        saved = args.save_commands / ("assistant-command-" + str(time.time_ns()) + ".wav")
                        save_wav(saved, pcm)
                        if os.geteuid() == 0:
                            owner = args.save_commands.stat()
                            os.chown(saved, owner.st_uid, owner.st_gid)
                    started = time.monotonic()
                    result = recognize_whisper(command_model, command_path, 0, "اللمبة، كم التاريخ اليوم، كم درجة الحرارة اليوم")
                    result.update(event="COMMAND_RESULT",
                                  inference_seconds=round(time.monotonic()-started, 2))
                    if saved:
                        result["saved_command"] = str(saved)
                    log("COMMAND_TRANSCRIPT", text=result["text"])
                    def lamp(command):
                        return execute_and_reply(command, args.container, ["docker"],
                                                 args.reply_dir, args.playback_device)

                    def information(command):
                        answer = information_answer(command, location)
                        log("INFORMATION_ANSWER", **answer)
                        if args.tts_python:
                            answer["reply"] = speak_answer(answer, args.tts_python, args.tts_model, args.playback_device)
                        else:
                            answer["reply"] = {"played": False, "error": "Dynamic speech is not configured"}
                        return answer

                    result.update(dispatch_command(result["text"], result["mean_word_confidence"],
                                                   args.minimum_confidence, lamp, information))
                    result["max_rss_mb"] = round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 1)
                    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
                    return result

                dispatch_after_wake(wake["text"], capture, process)
                turns += 1
                time.sleep(0.3)
    except KeyboardInterrupt:
        log("LISTENING_STOPPED")


if __name__ == "__main__":
    main()
