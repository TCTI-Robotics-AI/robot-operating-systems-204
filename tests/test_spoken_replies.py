import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import wave

from course204.spoken_replies import REPLY_TEXT, play_acknowledged_reply, validate_reply_cache


class SpokenReplyCache(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        manifest = {"replies": {}}
        for command, text in REPLY_TEXT.items():
            path = self.directory / (command + ".wav")
            with wave.open(str(path), "wb") as audio:
                audio.setparams((1, 2, 22050, 0, "NONE", "not compressed"))
                audio.writeframes(b"\0\0" * 2205)
            manifest["replies"][command] = {"text": text, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        self.manifest = manifest
        self.write_manifest()

    def write_manifest(self):
        (self.directory / "manifest.json").write_text(json.dumps(self.manifest), encoding="utf-8")

    def test_successful_physical_off_plays_matching_cached_phrase(self):
        with patch("course204.spoken_replies.subprocess.run") as run:
            reply = play_acknowledged_reply("off", {"success": True, "state": False, "simulated": False}, self.directory, "plughw:CARD=EarPods,DEV=0")
        self.assertEqual(reply["text"], "تم إطفاء اللمبة")
        run.assert_called_once_with(["aplay", "-q", "-D", "plughw:CARD=EarPods,DEV=0", str(self.directory / "off.wav")], check=True, timeout=20)

    def test_mismatched_phrase_or_corrupt_audio_is_rejected(self):
        self.manifest["replies"]["on"]["text"] = REPLY_TEXT["off"]
        self.write_manifest()
        with self.assertRaises(RuntimeError):
            validate_reply_cache(self.directory)
        self.manifest["replies"]["on"]["text"] = REPLY_TEXT["on"]
        self.write_manifest()
        (self.directory / "on.wav").write_bytes(b"corrupt")
        with self.assertRaises(RuntimeError):
            validate_reply_cache(self.directory)

    def test_missing_cache_is_rejected(self):
        (self.directory / "off.wav").unlink()
        with self.assertRaises(OSError):
            validate_reply_cache(self.directory)
