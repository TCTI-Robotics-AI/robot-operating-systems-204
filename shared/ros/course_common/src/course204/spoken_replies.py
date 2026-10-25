"""Play fixed Arabic replies only after a matching physical ROS acknowledgement."""
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import wave


REPLY_TEXT = {"on": "تم تشغيل اللمبة", "off": "تم إطفاء اللمبة"}
READY_TEXT = "تفضل"


def validate_acknowledgement(command, response):
    if command not in REPLY_TEXT:
        raise ValueError("Unknown lamp command")
    if (response.get("success") is not True
            or response.get("state") is not (command == "on")
            or response.get("simulated") is not False):
        raise RuntimeError("No matching successful physical acknowledgement; no spoken success reply")


def validate_cache_entry(directory, command, text):
    directory = Path(directory)
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    entry = manifest["replies"][command]
    path = directory / (command + ".wav")
    if entry["text"] != text or entry["sha256"] != hashlib.sha256(path.read_bytes()).hexdigest():
        raise RuntimeError("Spoken reply cache does not match its manifest")
    with wave.open(str(path), "rb") as audio:
        duration = audio.getnframes() / audio.getframerate()
        if audio.getsampwidth() != 2 or audio.getnchannels() not in (1, 2) or not 0 < duration <= 15:
            raise RuntimeError("Spoken reply WAV format or duration is invalid")
    return path


def validate_reply_cache(directory):
    return {command: validate_cache_entry(directory, command, text) for command, text in REPLY_TEXT.items()}


def play_ready_prompt(directory, device):
    path = validate_cache_entry(directory, "ready", READY_TEXT)
    arguments = ["aplay", "-q", "-D", device, str(path)]
    print("READY PROMPT: " + shlex.join(arguments), flush=True)
    subprocess.run(arguments, check=True, timeout=20)


def play_acknowledged_reply(command, response, directory, device):
    validate_acknowledgement(command, response)
    path = validate_reply_cache(directory)[command]
    arguments = ["aplay", "-q", "-D", device, str(path)]
    print("PLAYBACK / إخراج الصوت: " + shlex.join(arguments), flush=True)
    subprocess.run(arguments, check=True, timeout=20)
    return {"text": REPLY_TEXT[command], "played": True, "device": device}
