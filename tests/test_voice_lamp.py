import importlib.util
import array
from pathlib import Path
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location(
    "voice_lamp", Path(__file__).resolve().parents[1] / "tools" / "voice_lamp.py")
voice_lamp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(voice_lamp)


class VoiceCommandDecisions(unittest.TestCase):
    def test_gain_increases_quiet_pcm_without_integer_wraparound(self):
        samples, clipped = voice_lamp.amplify_pcm(array.array("h", [100, -100, 4000, -4000]), 20)
        self.assertEqual(list(samples), [1000, -1000, 32767, -32768])
        self.assertEqual(clipped, 50.0)

    def test_exact_arabic_commands(self):
        self.assertEqual(voice_lamp.decide("شغل اللمبة", 0.95, 0.8)[0], "on")
        self.assertEqual(voice_lamp.decide("طف اللمبة", 0.95, 0.8)[0], "off")
        self.assertEqual(voice_lamp.decide("إطفاء اللمبة", 0.31, 0.3)[0], "off")
        self.assertIsNone(voice_lamp.decide("لا إطفاء اللمبة", 0.95, 0.3)[0])

    def test_negation_and_multiple_commands_are_rejected(self):
        for text in ("لا تشغل اللمبة", "لا شغل اللمبة", "شغل اللمبة طف اللمبة", "شغل اللمبة وبعدها طف اللمبة"):
            with self.subTest(text=text):
                self.assertIsNone(voice_lamp.decide(text, 1.0, 0.8)[0])

    def test_empty_unknown_and_low_confidence_do_not_execute(self):
        self.assertIsNone(voice_lamp.decide("", 1.0, 0.8)[0])
        self.assertIsNone(voice_lamp.decide("مرحبا", 1.0, 0.8)[0])
        self.assertIsNone(voice_lamp.decide("شغل اللمبة", 0.79, 0.8)[0])

    def test_spoken_reply_follows_matching_ros_acknowledgement(self):
        events = []
        response = {"success": True, "state": True, "simulated": False}
        def ros(*args):
            events.append("ros")
            return response
        def reply(*args):
            events.append("reply")
            return {"text": "تم تشغيل اللمبة", "played": True}
        with patch.object(voice_lamp, "execute", side_effect=ros), patch.object(voice_lamp, "play_acknowledged_reply", side_effect=reply):
            result = voice_lamp.execute_and_reply("on", "lamp", [], Path("replies"), "EarPods")
        self.assertEqual(events, ["ros", "reply"])
        self.assertTrue(result["executed"])
        self.assertTrue(result["reply"]["played"])

    def test_failed_or_mismatched_ros_response_does_not_speak_success(self):
        for response in ({"success": False, "state": True, "simulated": False},
                         {"success": True, "state": False, "simulated": False},
                         {"success": True, "state": True, "simulated": True}):
            with self.subTest(response=response), patch.object(voice_lamp, "execute", return_value=response), patch.object(voice_lamp, "play_acknowledged_reply") as reply:
                with self.assertRaises(RuntimeError):
                    voice_lamp.execute_and_reply("on", "lamp", [], Path("replies"), "EarPods")
                reply.assert_not_called()

    def test_ros_exception_does_not_play_a_reply(self):
        with patch.object(voice_lamp, "execute", side_effect=RuntimeError("unavailable")), patch.object(voice_lamp, "play_acknowledged_reply") as reply:
            with self.assertRaises(RuntimeError):
                voice_lamp.execute_and_reply("off", "lamp", [], Path("replies"), "EarPods")
            reply.assert_not_called()

    def test_playback_failure_is_distinct_from_successful_device_control(self):
        response = {"success": True, "state": False, "simulated": False}
        with patch.object(voice_lamp, "execute", return_value=response), patch.object(voice_lamp, "play_acknowledged_reply", side_effect=OSError("headset disconnected")):
            result = voice_lamp.execute_and_reply("off", "lamp", [], Path("replies"), "EarPods")
        self.assertTrue(result["executed"])
        self.assertFalse(result["reply"]["played"])
        self.assertEqual(result["ros_response"], response)


if __name__ == "__main__":
    unittest.main()
