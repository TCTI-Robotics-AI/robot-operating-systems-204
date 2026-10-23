#!/usr/bin/env python3
"""Compile all reference firmware; this does not flash or test hardware."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
results = []
for folder, board in [("01-arduino/firmware", "Arduino UNO R3"),
                      ("02-stm32/firmware", "STM32 NUCLEO-F446RE"),
                      ("02-stm32/wifi-firmware", "STM32 B-L475E-IOT01A")]:
    directory = root / "labs/06-embedded-systems" / folder
    command = [sys.executable, "-m", "platformio", "run", "-d", str(directory)]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, encoding="utf-8", errors="replace", timeout=600)
    with tempfile.NamedTemporaryFile(prefix="course204-firmware-", suffix=".log", delete=False) as logfile:
        logfile.write(result.stdout.encode("utf-8"))
    files = [directory / "platformio.ini", root / "shared/firmware/led_protocol.h"]
    files += sorted(path for path in (directory / "src").rglob("*") if path.is_file() and path.name != "secrets.h")
    digest = hashlib.sha256()
    for path in files:
        digest.update(str(path.relative_to(root)).replace("\\", "/").encode("utf-8"))
        digest.update(path.read_bytes().replace(b"\r\n", b"\n"))
    entry = {"board": board, "path": str(directory.relative_to(root)).replace("\\", "/"),
             "status": "passed" if result.returncode == 0 else "failed", "source_sha256": digest.hexdigest(),
             "memory": re.findall(r"(?:RAM|Flash):[^\n]+", result.stdout),
             "packages": re.findall(r"^ - .+$", result.stdout, re.M)}
    results.append(entry)
    print(json.dumps(entry), flush=True)
    if result.returncode:
        print(result.stdout[-4000:], flush=True)

report = {"date": datetime.now(timezone.utc).date().isoformat(), "test": "PlatformIO firmware compilation only",
          "physical_hardware_tested": False, "checks": results}
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
raise SystemExit(0 if all(item["status"] == "passed" for item in results) else 1)
