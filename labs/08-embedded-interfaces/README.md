# ربط الأنظمة المدمجة

**الأسبوع:** 14 و16 · **الحالة:** مخطط؛ لا يوجد تطبيق قابل للتشغيل بعد

## الهدف

تمارين مستقلة لربط Arduino وSTM32 وOdroid بالمقرر.

## المتطلبات والقطع

موديل اللوحة وكابل البيانات والطاقة وبروتوكول الربط يحدد لكل تمرين.

**ROS:** مطلوب للأمثلة المرتبطة بالمنهج؛ يحدد المسار لكل لوحة.

## إعداد الجهازين

- **Pi 4:** راجع [مسار Ubuntu 20.04](../../environments/pi4-ubuntu2004/README.md). تحدد مكتبات هذا التمرين والتوصيل وأجهزة الصوت عند تنفيذه.
- **Pi 5:** راجع [مسار Ubuntu 24.04 المقترح](../../environments/pi5-ubuntu2404/README.md). لا يفترض أن إعداد Pi 4 صالح للجهاز الثاني.

لم يسجل اختبار فعلي لهذا التمرين على اللوحتين. تملأ مواصفات القطع والطاقة والإعدادات وأرقام الأطراف والإصدارات طبقًا لـ[قالب التمرين](../../docs/lesson-template.md)، وتسجل النتائج في [مصفوفة التوافق](../../validation/compatibility.md). لا توجد أوامر أجهزة أو تثبيت ROS معتمدة في هذا الدليل المبدئي.

## English

**Course weeks:** 14 and 16 · **Status:** Planned; no runnable implementation yet

**Objective:** Separate course integration exercises for Arduino, STM32, and Odroid.

**Hardware:** Specify board model, data cable, PSU, and protocol per exercise.

**ROS:** Required for course integration examples; specify each board path.

Use the linked Pi 4 Ubuntu 20.04 and proposed Pi 5 Ubuntu 24.04 guides. Select this lab's dependencies, audio settings, GPIO library, and wiring per board rather than assuming interchangeability. No hardware runs are recorded on either board. Follow the lab template to specify actual parts, PSU, settings, pins, and versions, then record results in the compatibility matrix. This initial guide contains no validated hardware or ROS installation commands.
