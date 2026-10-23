# إعداد Linux والبيئة

**الأسبوع:** 1 إلى 5 · **الحالة:** مخطط؛ لا يوجد تطبيق قابل للتشغيل بعد

## الهدف

تجهيز النظام والأدوات وبيئة Python وتسجيل مواصفات اللوحة.

## المتطلبات والقطع

لوحة Pi 4 أو Pi 5 ومزود طاقة وتخزين وشبكة؛ أو حاسب للتجارب العامة.

**ROS:** مطلوب في جزء تثبيت ROS فقط؛ يحدد الإصدار عند التنفيذ.

## إعداد الجهازين

- **Pi 4:** راجع [مسار Ubuntu 20.04](../../environments/pi4-ubuntu2004/README.md). تحدد مكتبات هذا التمرين والتوصيل وأجهزة الصوت عند تنفيذه.
- **Pi 5:** راجع [مسار Ubuntu 24.04 المقترح](../../environments/pi5-ubuntu2404/README.md). لا يفترض أن إعداد Pi 4 صالح للجهاز الثاني.

لم يسجل اختبار فعلي لهذا التمرين على اللوحتين. تملأ مواصفات القطع والطاقة والإعدادات وأرقام الأطراف والإصدارات طبقًا لـ[قالب التمرين](../../docs/lesson-template.md)، وتسجل النتائج في [مصفوفة التوافق](../../validation/compatibility.md). لا توجد أوامر أجهزة أو تثبيت ROS معتمدة في هذا الدليل المبدئي.

## English

**Course weeks:** 1 to 5 · **Status:** Planned; no runnable implementation yet

**Objective:** Prepare the OS, tools, Python environment, and board inventory.

**Hardware:** A Pi 4 or Pi 5, suitable PSU, storage, network, or a computer for general exercises.

**ROS:** Required only for the ROS setup section; version to be selected.

Use the linked Pi 4 Ubuntu 20.04 and proposed Pi 5 Ubuntu 24.04 guides. Select this lab's dependencies, audio settings, GPIO library, and wiring per board rather than assuming interchangeability. No hardware runs are recorded on either board. Follow the lab template to specify actual parts, PSU, settings, pins, and versions, then record results in the compatibility matrix. This initial guide contains no validated hardware or ROS installation commands.
