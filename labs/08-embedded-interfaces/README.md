<div dir="rtl" lang="ar">

# ربط الأنظمة المدمجة

**الأسبوع:** 14 و16 · **الحالة:** مخطط؛ لا يوجد تطبيق قابل للتشغيل بعد

## الهدف

تمارين مستقلة لربط <span dir="ltr">Arduino</span> و<span dir="ltr">STM32</span> و<span dir="ltr">Odroid</span> بالمقرر.

## المتطلبات والقطع

موديل اللوحة وكابل البيانات والطاقة وبروتوكول الربط يحدد لكل تمرين.

**<span dir="ltr">ROS</span>:** مطلوب للأمثلة المرتبطة بالمنهج؛ يحدد المسار لكل لوحة.

## إعداد الجهازين

- **<span dir="ltr">Pi 4</span>:** راجع [مسار <span dir="ltr">Ubuntu 20.04</span>](../../environments/pi4-ubuntu2004/README.md). تحدد مكتبات هذا التمرين والتوصيل وأجهزة الصوت عند تنفيذه.
- **<span dir="ltr">Pi 5</span>:** راجع [مسار <span dir="ltr">Ubuntu 24.04</span> المقترح](../../environments/pi5-ubuntu2404/README.md). لا يفترض أن إعداد <span dir="ltr">Pi 4</span> صالح للجهاز الثاني.

لم يسجل اختبار فعلي لهذا التمرين على اللوحتين. تملأ مواصفات القطع والطاقة والإعدادات وأرقام الأطراف والإصدارات طبقًا لـ[قالب التمرين](../../docs/lesson-template.md)، وتسجل النتائج في [مصفوفة التوافق](../../validation/compatibility.md). لا توجد أوامر أجهزة أو تثبيت <span dir="ltr">ROS</span> معتمدة في هذا الدليل المبدئي.

</div>

<div dir="ltr" lang="en">

## English

**Course weeks:** 14 and 16 · **Status:** Planned; no runnable implementation yet

**Objective:** Separate course integration exercises for Arduino, STM32, and Odroid.

**Hardware:** Specify board model, data cable, PSU, and protocol per exercise.

**ROS:** Required for course integration examples; specify each board path.

Use the linked Pi 4 Ubuntu 20.04 and proposed Pi 5 Ubuntu 24.04 guides. Select this lab's dependencies, audio settings, GPIO library, and wiring per board rather than assuming interchangeability. No hardware runs are recorded on either board. Follow the lab template to specify actual parts, PSU, settings, pins, and versions, then record results in the compatibility matrix. This initial guide contains no validated hardware or ROS installation commands.

</div>
