<div dir="rtl" lang="ar">

# بيئة ربط الأجهزة الخفيفة

هذه الحاوية لتمرين اللمبة وربط الأجهزة. تبني حزمتين فقط، وتشغل <span dir="ltr">ROS Noetic</span> داخل الحاوية، بينما يعمل وكيل <span dir="ltr">GPIO</span> على نظام الرازبيري الأصلي. لا تثبت أدوات المحاكاة والعرض.

ابدأ بالوكيل الافتراضي. عند الانتقال إلى القطع الحقيقية، أوقف الوكيل، وافصل طاقة الرازبيري ووصل المؤشر وفق [دليل التمرين](../../labs/06-embedded-systems/03-raspberry-pi/README.md). حدد رقم متحكم الأطراف الفعلي من <code dir="ltr">gpiodetect</code> وافحص الصلاحيات قبل تفعيله.

</div>

<div dir="ltr" lang="en">

# Lightweight device integration environment

Run from the repository root. The native agent needs Python 3.8+; on Pi 5 Ubuntu 24.04 install `python3-venv python3-lgpio gpiod` first.

```bash
python3 -m venv --system-site-packages .venv-agent
.venv-agent/bin/python -m pip install '.[gpio]'
.venv-agent/bin/course204-agent --driver mock
```

Keep that terminal running. In another Pi terminal, build the two-package Noetic image and start the bridge:

```bash
sudo docker build -t course204:device -f environments/noetic-device/Dockerfile .
sudo docker run --rm -d --name course204-lamp --network host \
  -e ROS_IP=127.0.0.1 course204:device
sudo docker logs course204-lamp
```

Check the service and the explicitly simulated state:

```bash
sudo docker exec course204-lamp /course-entrypoint.sh rosservice call /lamp/set true
sudo docker exec course204-lamp /course-entrypoint.sh rostopic echo -n 1 /lamp/state
sudo docker exec course204-lamp /course-entrypoint.sh rostopic echo -n 1 /lamp/simulated
sudo docker exec course204-lamp /course-entrypoint.sh rosservice call /lamp/set false
```

Stop with `sudo docker stop course204-lamp`, then stop the native agent. To use real GPIO, follow the linked Pi lab and replace the mock agent with the confirmed GPIO backend/chip. The bridge must be restarted after changing agents. The image contains source copied at build time; rebuild after source changes. It does not require privileged mode or direct GPIO access from the container.

</div>
