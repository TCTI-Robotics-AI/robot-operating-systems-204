import unittest
import array
import importlib.util
from pathlib import Path
from unittest.mock import Mock, patch
from course204.wake import matches_wake_phrase
from course204.wake import SpeechSegmenter

spec = importlib.util.spec_from_file_location("wake_assistant", Path(__file__).resolve().parents[1]/"tools/wake_assistant.py")
assistant = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assistant)


class WakePhraseTests(unittest.TestCase):
    def test_exact_wake_phrase_and_orthographic_variants(self):
        for text in ("يا مساعد", "يَا مُسَاعِد", "يا مساعد!", "يامساعد", "يا مساعد يا مساعد"):
            with self.subTest(text=text):
                self.assertTrue(matches_wake_phrase(text))

    def test_commands_and_mentions_do_not_wake(self):
        for text in ("", "مساعد", "شغل اللمبة", "لا يا مساعد", "هذا مساعد", "يا مساعد شغل اللمبة"):
            with self.subTest(text=text):
                self.assertFalse(matches_wake_phrase(text))

    def test_empty_wake_phrase_is_invalid(self):
        with self.assertRaises(ValueError):
            matches_wake_phrase("", "")

    def test_no_command_capture_or_processing_without_wake(self):
        capture, process = Mock(), Mock()
        for text in ("شغل اللمبة", "مساعد", "لا يا مساعد", ""):
            self.assertIsNone(assistant.dispatch_after_wake(text, capture, process))
        capture.assert_not_called()
        process.assert_not_called()

    def test_verified_wake_captures_then_processes(self):
        events = []
        def capture():
            events.append("capture")
            return b"audio"
        def process(data):
            events.append("process")
            self.assertEqual(data, b"audio")
            return "processed"
        self.assertEqual(assistant.dispatch_after_wake("يا مساعد", capture, process), "processed")
        self.assertEqual(events, ["capture", "process"])

    def test_capture_failure_does_not_process_a_command(self):
        capture = Mock(side_effect=RuntimeError("input disconnected"))
        process = Mock()
        with self.assertRaises(RuntimeError):
            assistant.dispatch_after_wake("يا مساعد", capture, process)
        process.assert_not_called()

    def test_ready_audio_is_discarded_before_exact_five_second_capture(self):
        events = []
        microphone = Mock()
        microphone.discard_pending.side_effect = lambda: events.append("discard")
        def read():
            events.append("record")
            return b"\0\0"*960
        microphone.read.side_effect = read
        with patch.object(assistant, "Microphone") as factory, patch.object(assistant, "play_ready_prompt", side_effect=lambda *args: events.append("ready")), patch.object(assistant, "log"):
            factory.return_value.__enter__.return_value = microphone
            data = assistant.record_command("EarPods", Path("cache"), "EarPods")
        self.assertEqual(events[:3], ["ready", "discard", "record"])
        self.assertEqual(len(data), 48000*5*2)

    def test_silence_and_short_click_do_not_make_a_speech_segment(self):
        silence = b"\0\0"*960
        speech = array.array("h", [3000]*960).tobytes()
        segmenter = SpeechSegmenter(0.01)
        blocks = [silence]*20 + [speech] + [silence]*40
        self.assertTrue(all(segmenter.feed(block) is None for block in blocks))

    def test_speech_segment_is_bounded_and_includes_pre_roll(self):
        silence = b"\0\0"*960
        speech = array.array("h", [3000]*960).tobytes()
        segmenter = SpeechSegmenter(0.01)
        result = None
        for block in [silence]*20 + [speech]*20 + [silence]*30:
            result = segmenter.feed(block)
        self.assertIsNotNone(result)
        self.assertTrue(result.startswith(silence))
        self.assertLessEqual(len(result), 48000*4*2)
