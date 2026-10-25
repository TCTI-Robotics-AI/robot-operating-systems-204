#!/usr/bin/env python3
"""Record a Pi 5 software bridge test; refuse to activate a physical backend."""
import argparse
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path
import platform
import re
import shutil
import subprocess


def run(command, timeout=60):
    result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--container", default="course204-lamp")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    model = Path("/proc/device-tree/model").read_text().rstrip("\0")
    if "Raspberry Pi 5" not in model:
        parser.error("This record is specifically for a real Raspberry Pi 5")
    docker = ["sudo", "-n", "docker"]
    payload = '''import json,platform,rospy
from std_msgs.msg import Bool,String
from course_common.srv import SetLamp
rospy.init_node("course204_pi5_setup_check",anonymous=True)
rospy.wait_for_service("/lamp/set",timeout=20)
simulated=rospy.wait_for_message("/lamp/simulated",Bool,timeout=10).data
assert simulated is True,"Refusing an actuator test: the bridge is not simulated"
lamp=rospy.ServiceProxy("/lamp/set",SetLamp)
on=lamp(True)
assert on.success and on.state
on_topic=rospy.wait_for_message("/lamp/state",Bool,timeout=10).data
assert on_topic is True
metadata=json.loads(rospy.wait_for_message("/device/status",String,timeout=10).data)
off=lamp(False)
assert off.success and not off.state
off_topic=rospy.wait_for_message("/lamp/state",Bool,timeout=10).data
assert off_topic is False
print(json.dumps({"service_on":on.success,"on_state":on_topic,"service_off":off.success,"off_state":off_topic,"simulated":simulated,"agent_system":metadata.get("system"),"agent_machine":metadata.get("machine"),"ros_version":rospy.get_param("/rosversion"),"container_machine":platform.machine()}))
'''
    observed = json.loads(run(docker + ["exec", args.container, "/course-entrypoint.sh", "python3", "-c", payload]))
    image = json.loads(run(docker + ["image", "inspect", "course204:device"]))[0]
    gpio = run(["sudo", "-n", "gpiodetect"])
    match = re.search(r"gpiochip(\d+) \[pinctrl-rp1\]", gpio)
    report = {
        "tested_at_utc": datetime.now(timezone.utc).isoformat(),
        "syllabus_reference": "15.2",
        "test": "Real Pi 5: native mock agent to Noetic container software bridge",
        "status": "passed",
        "board": model,
        "architecture": platform.machine(),
        "kernel": platform.release(),
        "os_release": dict(line.split("=", 1) for line in Path("/etc/os-release").read_text().splitlines() if "=" in line),
        "ram_kb": int(Path("/proc/meminfo").read_text().splitlines()[0].split()[1]),
        "free_disk_gb_after_setup": round(shutil.disk_usage("/").free / 1024**3, 2),
        "native_python": platform.python_version(),
        "gpiozero": importlib.metadata.version("gpiozero"),
        "lgpio_debian_package": run(["dpkg-query", "-W", "-f=${Version}", "python3-lgpio"]),
        "gpiochip_observed": int(match.group(1)) if match else None,
        "gpio_controller": "pinctrl-rp1" if match else None,
        "docker_version": run(docker + ["version", "--format", "{{.Server.Version}}"]),
        "image_id": image["Id"],
        "image_size_bytes": image["Size"],
        "checkout_revision": run(["git", "-c", "safe.directory=" + str(root), "-C", str(root), "rev-parse", "HEAD"]),
        "observed": observed,
        "gpio_output_activated": False,
        "physical_led_observed": False,
        "not_tested": ["Physical LED and resistor wiring", "Physical GPIO output", "microphone/audio", "Gazebo/RViz on this Pi", "Pi 4"],
        "privacy": "Network addresses, hostname and credentials intentionally excluded"
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "observed": observed, "gpiochip": report["gpiochip_observed"]}, indent=2))


if __name__ == "__main__":
    main()
