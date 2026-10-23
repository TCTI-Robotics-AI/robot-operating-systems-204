<div dir="rtl" lang="ar">

# تطبيق التحكم المنزلي بالصوت

**الأسبوع:** تطبيق تجميعي · **الحالة:** مخطط؛ لا يوجد تطبيق قابل للتشغيل بعد

## الهدف

دمج الصوت والأوامر والتحكم والرد بعد اكتمال التمارين المستقلة.

## المتطلبات والقطع

قطع تمارين الصوت و<span dir="ltr">GPIO</span> المعتمدة، مع مخطط توصيل خاص بالتطبيق.

**<span dir="ltr">ROS</span>:** اختياري حسب نسخة التطبيق؛ يحدد صراحة عند التنفيذ.

## إعداد الجهازين

- **<span dir="ltr">Pi 4</span>:** راجع [مسار <span dir="ltr">Ubuntu 20.04</span>](../../environments/pi4-ubuntu2004/README.md). تحدد مكتبات هذا التمرين والتوصيل وأجهزة الصوت عند تنفيذه.
- **<span dir="ltr">Pi 5</span>:** راجع [مسار <span dir="ltr">Ubuntu 24.04</span> المقترح](../../environments/pi5-ubuntu2404/README.md). لا يفترض أن إعداد <span dir="ltr">Pi 4</span> صالح للجهاز الثاني.

لم يسجل اختبار فعلي لهذا التمرين على اللوحتين. تملأ مواصفات القطع والطاقة والإعدادات وأرقام الأطراف والإصدارات طبقًا لـ[قالب التمرين](../../docs/lesson-template.md)، وتسجل النتائج في [مصفوفة التوافق](../../validation/compatibility.md). لا توجد أوامر أجهزة أو تثبيت <span dir="ltr">ROS</span> معتمدة في هذا الدليل المبدئي.

</div>

<div dir="ltr" lang="en">

## English

**Course weeks:** Integration · **Status:** Planned; no runnable implementation yet

**Objective:** Combine speech, commands, device control, and replies after standalone labs are complete.

**Hardware:** Validated speech and GPIO lab hardware plus an integration wiring diagram.

**ROS:** Optional by application variant; explicitly selected during implementation.

Use the linked Pi 4 Ubuntu 20.04 and proposed Pi 5 Ubuntu 24.04 guides. Select this lab's dependencies, audio settings, GPIO library, and wiring per board rather than assuming interchangeability. No hardware runs are recorded on either board. Follow the lab template to specify actual parts, PSU, settings, pins, and versions, then record results in the compatibility matrix. This initial guide contains no validated hardware or ROS installation commands.

</div>
