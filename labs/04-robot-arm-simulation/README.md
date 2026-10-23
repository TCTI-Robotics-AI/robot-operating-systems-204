# محاكاة ذراع روبوت

**الأسبوع:** 8 إلى 10 · **الحالة:** مخطط؛ لا يوجد تطبيق قابل للتشغيل بعد

## الهدف

Xacro وmesh وURDF لذراع بثلاثة أجزاء وقابض والتحكم باستخدام rqt.

## المتطلبات والقطع

جهاز مناسب للمحاكاة؛ لا يشمل ذراعًا فعليًا في هذه المرحلة.

**ROS:** مطلوب؛ يثبت توافق rqt والمحاكاة لكل مسار.

## إعداد الجهازين

- **Pi 4:** راجع [مسار Ubuntu 20.04](../../environments/pi4-ubuntu2004/README.md). تحدد مكتبات هذا التمرين والتوصيل وأجهزة الصوت عند تنفيذه.
- **Pi 5:** راجع [مسار Ubuntu 24.04 المقترح](../../environments/pi5-ubuntu2404/README.md). لا يفترض أن إعداد Pi 4 صالح للجهاز الثاني.

لم يسجل اختبار فعلي لهذا التمرين على اللوحتين. تملأ مواصفات القطع والطاقة والإعدادات وأرقام الأطراف والإصدارات طبقًا لـ[قالب التمرين](../../docs/lesson-template.md)، وتسجل النتائج في [مصفوفة التوافق](../../validation/compatibility.md). لا توجد أوامر أجهزة أو تثبيت ROS معتمدة في هذا الدليل المبدئي.

## English

**Course weeks:** 8 to 10 · **Status:** Planned; no runnable implementation yet

**Objective:** Xacro, meshes, and URDF for a three part arm with gripper and rqt control.

**Hardware:** A simulation capable computer; no physical arm is included at this stage.

**ROS:** Required; validate rqt and simulation compatibility per environment.

Use the linked Pi 4 Ubuntu 20.04 and proposed Pi 5 Ubuntu 24.04 guides. Select this lab's dependencies, audio settings, GPIO library, and wiring per board rather than assuming interchangeability. No hardware runs are recorded on either board. Follow the lab template to specify actual parts, PSU, settings, pins, and versions, then record results in the compatibility matrix. This initial guide contains no validated hardware or ROS installation commands.
