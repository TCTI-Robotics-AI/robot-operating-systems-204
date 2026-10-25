#!/usr/bin/env python3
"""Generate the two fixed Arabic reply WAVs locally; never play or control GPIO."""
import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import tempfile
import wave

from course204.spoken_replies import REPLY_TEXT, READY_TEXT


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path,
                        default=Path.home() / ".local/state/course204/replies")
    parser.add_argument("--volume", type=float, default=0.65)
    parser.add_argument("--include-ready", action="store_true", help="Also prepare the separate wake acknowledgement تفضل")
    args = parser.parse_args()
    if not 0 < args.volume <= 1:
        parser.error("Volume must be greater than zero and no more than one")
    from piper import PiperVoice, SynthesisConfig
    os.umask(0o077)
    args.output_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    voice = PiperVoice.load(str(args.model))
    config = SynthesisConfig(volume=args.volume)
    manifest = {"engine": "piper-tts", "version": importlib.metadata.version("piper-tts"),
                "model": args.model.name,
                "model_sha256": hashlib.sha256(args.model.read_bytes()).hexdigest(),
                "volume": args.volume, "replies": {}}
    phrases = dict(REPLY_TEXT)
    if args.include_ready:
        phrases["ready"] = READY_TEXT
    with tempfile.TemporaryDirectory(prefix="prepare-", dir=str(args.output_dir)) as temporary:
        for command, text in phrases.items():
            path = Path(temporary) / (command + ".wav")
            with wave.open(str(path), "wb") as audio:
                voice.synthesize_wav(text, audio, syn_config=config)
            with wave.open(str(path), "rb") as audio:
                duration = audio.getnframes() / audio.getframerate()
            manifest["replies"][command] = {
                "text": text, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "duration_seconds": round(duration, 3)}
        for command in phrases:
            os.replace(str(Path(temporary) / (command + ".wav")), str(args.output_dir / (command + ".wav")))
        manifest_path = Path(temporary) / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(str(manifest_path), str(args.output_dir / "manifest.json"))
    print(json.dumps(manifest, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
