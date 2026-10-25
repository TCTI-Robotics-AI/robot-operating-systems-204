"""Exact Arabic commands; unknown phrases never become actuator requests."""

import re
import unicodedata


def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = text.translate(str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ـ": ""}))
    return " ".join(re.sub(r"[؟?!،,。.]", " ", text).split())


def intent(text):
    phrases = {
        "شغل اللمبة": "on", "شغل اللمبه": "on", "اشعل اللمبة": "on",
        "تشغيل اللمبة": "on", "تشغيل اللمبه": "on",
        "طفي اللمبة": "off", "طفي اللمبه": "off", "طف اللمبة": "off",
        "اطفئ اللمبة": "off", "اطفي اللمبة": "off",
        "اطفاء اللمبة": "off", "اطفاء اللمبه": "off",
    }
    return phrases.get(normalize(text))
