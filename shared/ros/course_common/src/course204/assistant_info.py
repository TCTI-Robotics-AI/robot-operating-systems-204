"""Exact assistant intents and Arabic date/current-weather answers (no GPIO)."""
from datetime import datetime, timedelta, timezone
import json
import math
from urllib.parse import urlencode
from urllib.request import urlopen

from course204.commands import intent, normalize

SAUDI_TIME = timezone(timedelta(hours=3), "Asia/Riyadh")
WEATHER_SOURCE = "https://open-meteo.com/"
WEATHER_UNAVAILABLE = "عذرا، تعذر جلب درجة الحرارة الآن. حاول مرة أخرى."
MONTHS = ("يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر")
WEEKDAYS = ("الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت", "الأحد")


def assistant_intent(text):
    """Full-phrase matching; mixed, negated and unknown requests stay rejected."""
    lamp = intent(text)
    if lamp:
        return lamp
    phrases = {
        "كم التاريخ اليوم": "date", "ما هو تاريخ اليوم": "date",
        "ما تاريخ اليوم": "date", "وش التاريخ اليوم": "date",
        "ايش التاريخ اليوم": "date", "كم تاريخ اليوم": "date",
        "كم درجة الحرارة": "weather", "كم درجة الحرارة اليوم": "weather",
        "كم درجة الحرارة الان": "weather", "كم درجة الحراره اليوم": "weather",
        "كيف الجو اليوم": "weather", "كيف الطقس اليوم": "weather",
    }
    return phrases.get(normalize(text))


def arabic_integer(value):
    """Speak integer values instead of relying on a voice's digit pronunciation."""
    if isinstance(value, bool) or not isinstance(value, int) or abs(value) > 9999:
        raise ValueError("Expected an integer in -9999..9999")
    if value < 0:
        return "سالب " + arabic_integer(-value)
    small = ("صفر", "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة", "عشرة",
             "أحد عشر", "اثنا عشر", "ثلاثة عشر", "أربعة عشر", "خمسة عشر", "ستة عشر", "سبعة عشر", "ثمانية عشر", "تسعة عشر")
    if value < 20:
        return small[value]
    if value < 100:
        tens = ("", "", "عشرون", "ثلاثون", "أربعون", "خمسون", "ستون", "سبعون", "ثمانون", "تسعون")
        return (small[value % 10] + " و" if value % 10 else "") + tens[value // 10]
    if value < 1000:
        hundreds = ("", "مئة", "مئتان", "ثلاثمئة", "أربعمئة", "خمسمئة", "ستمئة", "سبعمئة", "ثمانمئة", "تسعمئة")
        prefix, remainder = hundreds[value // 100], value % 100
    else:
        thousands = ("", "ألف", "ألفان", "ثلاثة آلاف", "أربعة آلاف", "خمسة آلاف", "ستة آلاف", "سبعة آلاف", "ثمانية آلاف", "تسعة آلاف")
        prefix, remainder = thousands[value // 1000], value % 1000
    return prefix + (" و" + arabic_integer(remainder) if remainder else "")


def date_reply(now=None):
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("Date requires a timezone-aware clock")
    local = now.astimezone(SAUDI_TIME)
    return {"intent": "date", "ok": True, "source": "device_clock", "timezone": "Asia/Riyadh",
            "date": local.date().isoformat(), "calendar": "Gregorian",
            "text": "اليوم {}، {} {}، عام {} ميلادي.".format(
                WEEKDAYS[local.weekday()], arabic_integer(local.day), MONTHS[local.month-1], arabic_integer(local.year))}


def read_json(url):
    with urlopen(url, timeout=8) as response:
        body = response.read(65537)
    if len(body) > 65536:
        raise ValueError("Weather response exceeds size limit")
    return json.loads(body)


def validate_location(location):
    city = location["city"]
    if not isinstance(city, str) or not city.strip() or len(city) > 60:
        raise ValueError("An explicit weather city is required")
    for key, maximum in (("latitude", 90), ("longitude", 180)):
        value = location[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or abs(value) > maximum:
            raise ValueError("Invalid weather coordinates")
    return location


def weather_reply(location, now=None, fetch=None):
    """No fabricated/cached reading on network, schema or freshness failure."""
    validate_location(location)
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError("Weather freshness requires a timezone-aware clock")
    url = "https://api.open-meteo.com/v1/forecast?" + urlencode({
        "latitude": location["latitude"], "longitude": location["longitude"],
        "current": "temperature_2m", "temperature_unit": "celsius",
        "timezone": "Asia/Riyadh", "timeformat": "unixtime", "forecast_days": 1})
    result = {"intent": "weather", "source": WEATHER_SOURCE, "city": location["city"], "request_url": url}
    try:
        data = (fetch or read_json)(url)
        temperature, timestamp = data["current"]["temperature_2m"], data["current"]["time"]
        if (data["current_units"]["temperature_2m"] != "°C"
                or isinstance(temperature, bool) or not isinstance(temperature, (float, int))
                or not math.isfinite(temperature) or not -90 <= temperature <= 65
                or isinstance(timestamp, bool) or not isinstance(timestamp, (float, int))
                or not math.isfinite(timestamp) or not -900 <= now.timestamp() - timestamp <= 5400):
            raise ValueError("Invalid, future or stale current weather")
        tenths = round(temperature * 10)
        absolute = abs(tenths)
        spoken = ("سالب " if tenths < 0 else "") + arabic_integer(absolute // 10)
        if absolute % 10:
            spoken += " فاصلة " + arabic_integer(absolute % 10)
        result.update(ok=True, temperature_c=temperature,
                      valid_at=datetime.fromtimestamp(timestamp, SAUDI_TIME).isoformat(),
                      text="درجة الحرارة الآن في {}، {} درجة مئوية، حسب بيانات الطقس.".format(location["city"], spoken))
    except (OSError, ValueError, KeyError, TypeError, OverflowError) as error:
        result.update(ok=False, text=WEATHER_UNAVAILABLE, error=str(error))
    return result
