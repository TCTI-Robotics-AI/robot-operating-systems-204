<div dir="rtl" lang="ar">

# الاختبارات

تختبر هذه الملفات معالجة الأوامر والتأكيدات والاتصال، ولا تستبدل تجارب القطع. يختبر ملف المتحكم منطق البروتوكول بمضاعف بسيط لواجهة اللوحة؛ ليس محاكيًا للمعالج أو الراديو.

</div>

<div dir="ltr" lang="en">

## Portable checks

The current Python suite has 37 behavioral tests. Date/weather cases cover Saudi midnight, exact intent separation from ROS, confidence rejection, stale/future/invalid readings, network failure and Arabic number speech. They use fixed clock/API data; real network, sound output and voice observations are recorded separately in [the Pi 5 run](../validation/runs/2026-10-25-pi5-date-weather.json).

```bash
python3 -m venv .venv-test
.venv-test/bin/python -m pip install '.[conversation,serial,gpio]'
.venv-test/bin/python -m unittest discover -s tests -v
g++ -std=c++17 -I tests/firmware -I shared/firmware tests/firmware/protocol_test.cpp -o /tmp/course204-protocol-test
/tmp/course204-protocol-test
```

## ROS and headless Gazebo

On a prepared Noetic/Gazebo 11 host with all package dependencies installed:

```bash
bash tools/build.sh ~/course204_ws
source ~/course204_ws/devel/setup.bash
python3 tools/verify_ros.py --output /tmp/course204-ros-results.json
```

The runner uses dedicated ROS/Gazebo ports and stops only its own processes. It refuses occupied ports. `--only CHECK_NAME` reruns an individual failed check. A failure exits nonzero and remains visible in JSON; consult the temporary logs printed by the runner. Physical Pi/USB/radio/audio and GUI validation are separate.

</div>
