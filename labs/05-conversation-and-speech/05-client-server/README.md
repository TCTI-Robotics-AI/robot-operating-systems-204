<div dir="rtl" lang="ar">

# بناء عقد العميل والخادم

**مرجع الخطة:** <code dir="ltr">13.2</code> · **النوع:** عملي · **الحالة:** مخطط، غير منفذ.

## الهدف

تنفيذ أو شرح موضوع البند المحدد أعلاه من الخطة. هذا المجلد يحجز مكان الشرح والكود الخاص بهذا البند؛ لا يقدم أوامر تشغيل مكتملة حاليًا.

## القطع والبرامج

حدد جهاز الصوت والمايك والسماعة عند استخدام الصوت، وإصدارات المكتبات والنموذج أو محرك التعرف. البنود النصية لا تحتاج أجهزة صوت.

يحدد دور <span dir="ltr">ROS</span> وإصداره في خطوات التنفيذ؛ أمثلة <span dir="ltr">Catkin</span> الخاصة بالمنهج تبقى موثقة كمسار مستقل.

## إعداد الجهازين والتحقق

راجع [بيئات التشغيل](../../../environments/README.md) ثم وثق الفروق بين <span dir="ltr">Pi 4</span> و<span dir="ltr">Pi 5</span> عند استخدامهما. لا يعني دعم نظام التشغيل نجاح الصوت أو <span dir="ltr">GPIO</span> أو <span dir="ltr">ROS</span>. الأجهزة غير المستخدمة تسجل كغير منطبقة مع السبب.

استكمل هذا التمرين وفق [القالب](../../../docs/lesson-template.md)، مع قائمة القطع والتوصيل والإصدارات والأوامر والنتائج والأخطاء وتمرين المتدرب، ثم سجل النتائج في [التحقق](../../../validation/README.md).

[العودة إلى الوحدة](../README.md).

</div>

<div dir="ltr" lang="en">

# Client and server nodes

**Syllabus reference:** `13.2` · **Type:** Practical · **Status:** Planned, not implemented.

This directory owns the explanation and future code for the exact syllabus item above. It does not yet contain a complete runnable procedure.

Identify microphone and playback devices when used, library versions, and recognition engine. Text only steps do not require audio hardware.

Specify ROS requirements and version in the implementation. Keep course Catkin examples in their documented legacy path. Embedded interface exercises require ROS integration; when a Pi 4 or Pi 5 is the host, document and validate its setup separately. A board not used by an exercise is recorded as not applicable with an explanation.

Use the linked environment guide, lab template and validation guide to complete hardware, wiring, versions, commands, expected results, troubleshooting and learner exercises. OS support alone does not establish audio, GPIO or ROS compatibility. Return to the linked unit for context.

</div>
