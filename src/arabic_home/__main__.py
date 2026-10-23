"""Run one text command against a simulated lamp."""

import argparse
import unicodedata


def parse_command(text):
    """Return an explicit lamp state, or None for unsupported commands."""
    text = unicodedata.normalize("NFC", text)
    text = "".join(char for char in text if unicodedata.category(char) != "Mn")
    text = " ".join(text.replace("ـ", "").split())
    commands = {
        "شغل اللمبة": True,
        "شغل اللمبه": True,
        "طف اللمبة": False,
        "طفي اللمبة": False,
        "طفي اللمبه": False,
        "اطفئ اللمبة": False,
        "أطفئ اللمبة": False,
    }
    return commands.get(text)


def main():
    parser = argparse.ArgumentParser(description="Arabic text command demo")
    parser.add_argument("--command", required=True, help="An Arabic lamp command")
    args = parser.parse_args()
    state = parse_command(args.command)
    if state is None:
        print("الأمر غير معروف. جرّب: شغل اللمبة أو طفي اللمبة")
        return 2
    print("اللمبة الافتراضية: " + ("تعمل" if state else "مطفأة"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
