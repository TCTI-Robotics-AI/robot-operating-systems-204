# الصوت العربي وتحويله إلى نص

**الأسبوع:** 11 إلى 13 · **الحالة:** مخطط؛ لا يوجد تطبيق قابل للتشغيل بعد

## الهدف

التقاط الصوت وإنتاج نص عربي مع توثيق اللغة والنموذج والاتصال.

## المتطلبات والقطع

مايك متوافق؛ الموديل والتعريف ومعدل التسجيل لم تعتمد.

**ROS:** غير مطلوب للتجربة المستقلة؛ ربط ROS يضاف كمرحلة محددة.

## إعداد الجهازين

- **Pi 4:** راجع [مسار Ubuntu 20.04](../../environments/pi4-ubuntu2004/README.md). تحدد مكتبات هذا التمرين والتوصيل وأجهزة الصوت عند تنفيذه.
- **Pi 5:** راجع [مسار Ubuntu 24.04 المقترح](../../environments/pi5-ubuntu2404/README.md). لا يفترض أن إعداد Pi 4 صالح للجهاز الثاني.

لم يسجل اختبار فعلي لهذا التمرين على اللوحتين. تملأ مواصفات القطع والطاقة والإعدادات وأرقام الأطراف والإصدارات طبقًا لـ[قالب التمرين](../../docs/lesson-template.md)، وتسجل النتائج في [مصفوفة التوافق](../../validation/compatibility.md). لا توجد أوامر أجهزة أو تثبيت ROS معتمدة في هذا الدليل المبدئي.

## English

**Course weeks:** 11 to 13 · **Status:** Planned; no runnable implementation yet

**Objective:** Capture speech and produce Arabic text with documented language, model, and connectivity.

**Hardware:** A compatible microphone; model, driver, and sample rate pending.

**ROS:** Unused for the standalone exercise; ROS integration is a separate step.

Use the linked Pi 4 Ubuntu 20.04 and proposed Pi 5 Ubuntu 24.04 guides. Select this lab's dependencies, audio settings, GPIO library, and wiring per board rather than assuming interchangeability. No hardware runs are recorded on either board. Follow the lab template to specify actual parts, PSU, settings, pins, and versions, then record results in the compatibility matrix. This initial guide contains no validated hardware or ROS installation commands.
