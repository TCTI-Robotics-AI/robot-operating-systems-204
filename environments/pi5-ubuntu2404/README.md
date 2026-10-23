<div dir="rtl" lang="ar">

# إعداد <span dir="ltr">Raspberry Pi 5</span>

المسار المستهدف <span dir="ltr">Ubuntu 24.04 arm64.</span> لا يصف ذلك نظام جهازك الحالي؛ افحصه أولا. لم تنفذ اختبارات قطع المشروع على هذا الجهاز بعد.

استخدم [الحاوية](../noetic-container/README.md) أو مضيف <span dir="ltr">ROS</span> منفصلا. يعمل وكيل <span dir="ltr">GPIO</span> على النظام الأصلي باستخدام <span dir="ltr">lgpio</span>؛ لا تستخدم <span dir="ltr">RPi.GPIO</span> على الخامس. حدد رقم <span dir="ltr">gpiochip</span> الفعلي من <span dir="ltr">gpiodetect</span> بدل افتراض رقم ثابت. تفاصيل الأوامر في تمرين الرازبيري.

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

# Raspberry Pi 5 setup

Target: Ubuntu 24.04 arm64. This is not a claim about your installed OS, and physical project testing remains pending. Use the Noetic container or a separate ROS host. Run the native GPIO agent using lgpio; do not use RPi.GPIO on Pi 5. Identify the real gpiochip using gpiodetect rather than assuming its number. The Pi lab gives commands.

```bash
python3 tools/diagnose.py
cat /etc/os-release
uname -m
```

Follow the [Pi lesson](../../labs/06-embedded-systems/03-raspberry-pi/README.md) and [hardware guide](../../hardware/README.md), complete the [profile template](environment.example.json), and record [validation](../../validation/README.md). JSON documents intended/observed settings and does not configure the system. Validate ROS, GPIO and audio separately.

</div>
