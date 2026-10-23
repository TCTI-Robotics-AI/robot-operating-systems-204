<div dir="rtl" lang="ar">

# إعداد <span dir="ltr">Raspberry Pi 4</span>

المسار المستهدف <span dir="ltr">Ubuntu 20.04 arm64.</span> لا يصف ذلك نظام جهازك الحالي؛ افحصه أولا. لم تنفذ اختبارات قطع المشروع على هذا الجهاز بعد.

استخدم [دليل البدء](../../course/getting-started.md) لتثبيت <span dir="ltr">Noetic</span> وتهيئة <span dir="ltr">Catkin</span> مباشرة على النظام. لا تستخدم بيئة <span dir="ltr">Python</span> مختلفة للبناء. تمرين الرازبيري يوضح <span dir="ltr">RPi.GPIO</span> كمسار <span dir="ltr">GPIO</span> للرابع، مع فحص المكتبة والصلاحيات على الجهاز الحقيقي.

<div dir="ltr">

```bash
python3 tools/diagnose.py
cat /etc/os-release
uname -m
```

</div>

راجع [تمرين الرازبيري](../../labs/06-embedded-systems/03-raspberry-pi/README.md)، و[القطع](../../hardware/README.md)، ثم أكمل [قالب الإعداد](environment.example.json) وسجل نتائجك في [التحقق](../../validation/README.md). <span dir="ltr">JSON</span> توثيق ولا يغير الإعداد تلقائيا. اختبر الصوت و<span dir="ltr">GPIO</span> و<span dir="ltr">ROS</span> كلا على حدة.

</div>

<div dir="ltr" lang="en">

# Raspberry Pi 4 setup

Target: Ubuntu 20.04 arm64. This is not a claim about your installed OS, and physical project testing remains pending. Use the getting started guide for native Noetic/Catkin installation. Build with the system Python. The Pi lesson documents RPi.GPIO on Pi 4; validate its library and permissions on actual hardware.

```bash
python3 tools/diagnose.py
cat /etc/os-release
uname -m
```

Follow the [Pi lesson](../../labs/06-embedded-systems/03-raspberry-pi/README.md) and [hardware guide](../../hardware/README.md), complete the [profile template](environment.example.json), and record [validation](../../validation/README.md). JSON documents intended/observed settings and does not configure the system. Validate ROS, GPIO and audio separately.

</div>
