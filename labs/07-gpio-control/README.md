# التحكم بالأطراف ولمبة LED

**الأسبوع:** 15 · **الحالة:** تجربة نصية متوفرة؛ التحكم الفعلي قادم

## الهدف

التدرج من أمر نصي ولمبة افتراضية إلى LED فعلية وتسجيل نتيجة التنفيذ.

## المتطلبات والقطع

التجربة النصية دون قطع؛ الفعلية تحتاج LED ومقاومة ولوحة تجارب وأسلاك.

**ROS:** غير مستخدم حاليًا؛ يضاف ربط ROS لاحقًا.

## إعداد الجهازين

- **Pi 4:** راجع [مسار Ubuntu 20.04](../../environments/pi4-ubuntu2004/README.md). تحدد مكتبات هذا التمرين والتوصيل وأجهزة الصوت عند تنفيذه.
- **Pi 5:** راجع [مسار Ubuntu 24.04 المقترح](../../environments/pi5-ubuntu2404/README.md). لا يفترض أن إعداد Pi 4 صالح للجهاز الثاني.

لم يسجل اختبار فعلي لهذا التمرين على اللوحتين. تملأ مواصفات القطع والطاقة والإعدادات وأرقام الأطراف والإصدارات طبقًا لـ[قالب التمرين](../../docs/lesson-template.md)، وتسجل النتائج في [مصفوفة التوافق](../../validation/compatibility.md). لا توجد أوامر أجهزة أو تثبيت ROS معتمدة في هذا الدليل المبدئي.

ابدأ بـ[التجربة النصية للمبة الافتراضية](01-text-lamp/README.md). كودها في `src/arabic_home/` داخل هذا المجلد.

## English

**Course weeks:** 15 · **Status:** Text demo available; physical control planned

**Objective:** Progress from text and a simulated lamp to a physical LED and execution feedback.

**Hardware:** No parts for text; physical control needs an LED, resistor, breadboard, and wires.

**ROS:** Unused in the current demo; ROS integration comes later.

Use the linked Pi 4 Ubuntu 20.04 and proposed Pi 5 Ubuntu 24.04 guides. Select this lab's dependencies, audio settings, GPIO library, and wiring per board rather than assuming interchangeability. No hardware runs are recorded on either board. Follow the lab template to specify actual parts, PSU, settings, pins, and versions, then record results in the compatibility matrix. This initial guide contains no validated hardware or ROS installation commands.

Start with the linked simulated lamp exercise. Its source is in this lab directory under `src/arabic_home/`.
