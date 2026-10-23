#!/usr/bin/env python3
"""Report board and runtime details without changing the machine."""
import importlib.util
import json
import platform
from pathlib import Path
import shutil


def main():
    model = Path("/proc/device-tree/model")
    os_release = Path("/etc/os-release")
    data = {"board": model.read_text().rstrip("\0") if model.exists() else "not detected",
            "system": platform.system(), "machine": platform.machine(),
            "python": platform.python_version(),
            "os_release": os_release.read_text() if os_release.exists() else None,
            "commands": {name: shutil.which(name) for name in
                         ["roscore", "catkin_make", "gazebo", "rviz", "gpiodetect", "arecord"]},
            "modules": {name: importlib.util.find_spec(name) is not None for name in
                        ["rospy", "aiml", "vosk", "serial", "gpiozero"]}}
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
