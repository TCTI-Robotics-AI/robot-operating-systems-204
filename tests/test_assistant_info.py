from datetime import datetime, timezone, timedelta
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import Mock

from course204.assistant_info import assistant_intent, arabic_integer, date_reply, weather_reply

spec = importlib.util.spec_from_file_location("wake_info_assistant", Path(__file__).resolve().parents[1]/"tools/wake_assistant.py")
assistant = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assistant)

LOCATION = {"city": "جدة", "latitude": 21.5, "longitude": 39.2}
NOW = datetime(2026, 10, 25, 17, tzinfo=timezone.utc)


class AssistantInformationTests(unittest.TestCase):
    def test_exact_questions_and_unsafe_mixed_requests(self):
        self.assertEqual(assistant_intent("كَم دَرَجَة الحرارة اليوم؟"), "weather")
        self.assertEqual(assistant_intent("وش التاريخ اليوم"), "date")
        for phrase in ("شغل اللمبة وكم التاريخ اليوم", "لا شغل اللمبة", "كم التاريخ اليوم شغل اللمبة", "مرحبا", ""):
            self.assertIsNone(assistant_intent(phrase))

    def test_date_uses_saudi_day_at_midnight_boundary(self):
        answer = date_reply(datetime(2026, 10, 24, 22, tzinfo=timezone.utc))
        self.assertEqual(answer["date"], "2026-10-25")
        self.assertIn("الأحد", answer["text"])
        self.assertIn("خمسة وعشرون أكتوبر", answer["text"])
        self.assertEqual(answer["calendar"], "Gregorian")
        with self.assertRaises(ValueError):
            date_reply(datetime(2026, 10, 25))

    def test_weather_units_freshness_and_negative_decimal_speech(self):
        def fetch(url):
            self.assertIn("current=temperature_2m", url)
            return {"current": {"temperature_2m": -2.5, "time": NOW.timestamp()}, "current_units": {"temperature_2m": "°C"}}
        answer = weather_reply(LOCATION, NOW, fetch)
        self.assertTrue(answer["ok"])
        self.assertIn("سالب اثنان فاصلة خمسة", answer["text"])
        self.assertEqual(answer["temperature_c"], -2.5)

    def test_weather_failures_never_present_a_temperature(self):
        valid = {"temperature_2m": 30, "time": NOW.timestamp()}
        for current, units in (({**valid, "time": (NOW-timedelta(hours=2)).timestamp()}, "°C"),
                               ({**valid, "time": (NOW+timedelta(hours=2)).timestamp()}, "°C"),
                               ({**valid, "temperature_2m": None}, "°C"),
                               ({**valid, "temperature_2m": float("nan")}, "°C"),
                               ({**valid, "temperature_2m": True}, "°C"), (valid, "°F")):
            with self.subTest(current=current, units=units):
                answer = weather_reply(LOCATION, NOW, lambda url: {"current": current, "current_units": {"temperature_2m": units}})
                self.assertFalse(answer["ok"])
                self.assertNotIn("temperature_c", answer)
        for fetch in (Mock(side_effect=TimeoutError("offline")), lambda url: {}, lambda url: None):
            self.assertFalse(weather_reply(LOCATION, NOW, fetch)["ok"])

    def test_weather_location_is_explicit_and_validated(self):
        fetch = Mock()
        for location in ({"city": "", "latitude": 21, "longitude": 39},
                         {"city": "جدة", "latitude": float("nan"), "longitude": 39}):
            with self.assertRaises(ValueError):
                weather_reply(location, NOW, fetch)
        fetch.assert_not_called()

    def test_information_and_unknown_requests_never_call_ros(self):
        lamp, info = Mock(), Mock(return_value={"text": "answer"})
        for phrase in ("كم التاريخ اليوم", "كم درجة الحرارة اليوم"):
            outcome = assistant.dispatch_command(phrase, 0.9, 0.8, lamp, info)
            self.assertFalse(outcome["executed"])
            self.assertIn("information", outcome)
        for phrase, confidence in (("لا شغل اللمبة", 1), ("شغل اللمبة", 0.1), ("شغل اللمبة", float("nan"))):
            self.assertIsNone(assistant.dispatch_command(phrase, confidence, 0.8, lamp, info)["intent"])
        lamp.assert_not_called()
        self.assertEqual(info.call_count, 2)
        lamp.return_value = {"executed": True}
        self.assertTrue(assistant.dispatch_command("شغل اللمبة", 0.9, 0.8, lamp, info)["executed"])
        lamp.assert_called_once_with("on")

    def test_number_speech_handles_years_and_zero(self):
        self.assertEqual(arabic_integer(2026), "ألفان وستة وعشرون")
        self.assertEqual(arabic_integer(0), "صفر")
        with self.assertRaises(ValueError):
            arabic_integer(10000)
