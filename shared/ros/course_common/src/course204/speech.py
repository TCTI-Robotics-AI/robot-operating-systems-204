"""Offline Vosk recognition from a WAV or a bounded microphone recording."""
import json
from pathlib import Path
import queue
import time
import wave


def load_model(path):
    from vosk import Model
    path = Path(path)
    if not (path / "am").is_dir() or not (path / "conf").is_dir():
        raise ValueError("Use an extracted Vosk model directory containing am/ and conf/")
    return Model(str(path))


def transcribe_wav(model, path):
    from vosk import KaldiRecognizer
    with wave.open(str(path), "rb") as audio:
        if audio.getnchannels() != 1 or audio.getsampwidth() != 2 or audio.getcomptype() != "NONE":
            raise ValueError("Expected mono, uncompressed, signed 16-bit PCM WAV")
        if audio.getframerate() != 16000:
            raise ValueError("Convert the WAV to 16000 Hz before recognition")
        recognizer = KaldiRecognizer(model, 16000)
        text = []
        while True:
            data = audio.readframes(4000)
            if not data:
                break
            if recognizer.AcceptWaveform(data):
                text.append(json.loads(recognizer.Result()).get("text", ""))
        text.append(json.loads(recognizer.FinalResult()).get("text", ""))
    return " ".join(part for part in text if part).strip()


def transcribe_microphone(model, duration=8.0, device=None):
    import sounddevice as sd
    from vosk import KaldiRecognizer
    if not 0 < duration <= 60:
        raise ValueError("Microphone duration must be between 0 and 60 seconds")
    blocks = queue.Queue(maxsize=128)
    errors = []

    def callback(data, frames, timing, status):
        if status:
            errors.append(str(status))
        try:
            blocks.put_nowait(bytes(data))
        except queue.Full:
            errors.append("audio queue overflow")

    recognizer = KaldiRecognizer(model, 16000)
    text = []
    with sd.RawInputStream(samplerate=16000, blocksize=4000, device=device,
                           dtype="int16", channels=1, callback=callback):
        end = time.monotonic() + duration
        while time.monotonic() < end:
            try:
                data = blocks.get(timeout=0.2)
            except queue.Empty:
                continue
            if recognizer.AcceptWaveform(data):
                text.append(json.loads(recognizer.Result()).get("text", ""))
    if errors:
        raise RuntimeError("Incomplete recording: " + "; ".join(errors))
    while not blocks.empty():
        if recognizer.AcceptWaveform(blocks.get_nowait()):
            text.append(json.loads(recognizer.Result()).get("text", ""))
    text.append(json.loads(recognizer.FinalResult()).get("text", ""))
    return " ".join(part for part in text if part).strip()
