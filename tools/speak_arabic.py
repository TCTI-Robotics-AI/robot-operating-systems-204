#!/usr/bin/env python3
"""Generate a bounded Arabic answer locally; optional explicit ALSA playback."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import wave


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--text", required=True)
    parser.add_argument("--device", help="Explicit ALSA output; omit for generation only")
    args = parser.parse_args()
    if not args.text.strip() or len(args.text) > 240:
        parser.error("Expected 1..240 characters")
    from piper import PiperVoice, SynthesisConfig
    os.umask(0o077)
    started = time.monotonic()
    voice = PiperVoice.load(str(args.model))
    with tempfile.TemporaryDirectory(prefix="course204-reply-") as temporary:
        path = Path(temporary) / "reply.wav"
        with wave.open(str(path), "wb") as audio:
            voice.synthesize_wav(args.text, audio, syn_config=SynthesisConfig(volume=0.65))
        with wave.open(str(path), "rb") as audio:
            duration = audio.getnframes()/audio.getframerate()
            if not 0 < duration <= 35:
                raise RuntimeError("Dynamic reply exceeds duration limit")
        generated_seconds = round(time.monotonic()-started, 2)
        if args.device:
            subprocess.run(["aplay", "-q", "-D", args.device, str(path)], check=True, timeout=40)
        print(json.dumps({"event": "DYNAMIC_REPLY", "text": args.text, "played": bool(args.device),
                          "duration_seconds": round(duration, 2), "generation_seconds": generated_seconds}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
