#!/usr/bin/env python3
"""Test date/weather routing and dynamic speech without microphone or GPIO."""
import argparse
import json
from pathlib import Path
import shlex
import subprocess

from course204.assistant_info import assistant_intent, date_reply, weather_reply


def speak_answer(answer, python, model, device):
    arguments = [str(python), str(Path(__file__).with_name("speak_arabic.py")),
                 "--model", str(model), "--device", device, "--text", answer["text"]]
    print("SPEAK ANSWER: " + shlex.join(arguments), flush=True)
    try:
        subprocess.run(arguments, check=True, timeout=90)
        return {"played": True, "text": answer["text"]}
    except (OSError, subprocess.SubprocessError) as error:
        return {"played": False, "text": answer["text"], "error": str(error)}


def information_answer(command, location=None):
    if command == "date":
        return date_reply()
    if command == "weather":
        if location is None:
            return {"intent": "weather", "ok": False, "text": "حدد مدينة الطقس أولا في إعدادات المساعد."}
        return weather_reply(location)
    raise ValueError("Not an information intent")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", required=True)
    parser.add_argument("--weather-config", type=Path)
    parser.add_argument("--tts-python", type=Path)
    parser.add_argument("--tts-model", type=Path)
    parser.add_argument("--playback-device")
    args = parser.parse_args()
    if any((args.tts_python, args.tts_model, args.playback_device)) and not all((args.tts_python, args.tts_model, args.playback_device)):
        parser.error("Speech requires --tts-python, --tts-model and --playback-device")
    command = assistant_intent(args.text)
    if command not in ("date", "weather"):
        parser.error("Expected an exact date/weather question; this tool never controls the lamp")
    location = json.loads(args.weather_config.read_text(encoding="utf-8")) if args.weather_config else None
    answer = information_answer(command, location)
    print(json.dumps(answer, ensure_ascii=False, indent=2), flush=True)
    if args.tts_python:
        reply = speak_answer(answer, args.tts_python, args.tts_model, args.playback_device)
        print(json.dumps(reply, ensure_ascii=False), flush=True)
        if not reply["played"]:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
