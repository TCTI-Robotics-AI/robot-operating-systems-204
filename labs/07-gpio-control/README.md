<div dir="rtl" lang="ar">

# التحكم بالأطراف ولمبة <span dir="ltr">LED</span>

**الأسبوع:** 15 · **الحالة:** تجربة نصية متوفرة؛ التحكم الفعلي قادم

## الهدف

التدرج من أمر نصي ولمبة افتراضية إلى <span dir="ltr">LED</span> فعلية وتسجيل نتيجة التنفيذ.

## المتطلبات والقطع

التجربة النصية دون قطع؛ الفعلية تحتاج <span dir="ltr">LED</span> ومقاومة ولوحة تجارب وأسلاك.

**<span dir="ltr">ROS</span>:** غير مستخدم حاليًا؛ يضاف ربط <span dir="ltr">ROS</span> لاحقًا.

## إعداد الجهازين

- **<span dir="ltr">Pi 4</span>:** راجع [مسار <span dir="ltr">Ubuntu 20.04</span>](../../environments/pi4-ubuntu2004/README.md). تحدد مكتبات هذا التمرين والتوصيل وأجهزة الصوت عند تنفيذه.
- **<span dir="ltr">Pi 5</span>:** راجع [مسار <span dir="ltr">Ubuntu 24.04</span> المقترح](../../environments/pi5-ubuntu2404/README.md). لا يفترض أن إعداد <span dir="ltr">Pi 4</span> صالح للجهاز الثاني.

لم يسجل اختبار فعلي لهذا التمرين على اللوحتين. تملأ مواصفات القطع والطاقة والإعدادات وأرقام الأطراف والإصدارات طبقًا لـ[قالب التمرين](../../docs/lesson-template.md)، وتسجل النتائج في [مصفوفة التوافق](../../validation/compatibility.md). لا توجد أوامر أجهزة أو تثبيت <span dir="ltr">ROS</span> معتمدة في هذا الدليل المبدئي.

ابدأ بـ[التجربة النصية للمبة الافتراضية](01-text-lamp/README.md). كودها في <code dir="ltr">src/arabic_home/</code> داخل هذا المجلد.

</div>

<div dir="ltr" lang="en">

## English

**Course weeks:** 15 · **Status:** Text demo available; physical control planned

**Objective:** Progress from text and a simulated lamp to a physical LED and execution feedback.

**Hardware:** No parts for text; physical control needs an LED, resistor, breadboard, and wires.

**ROS:** Unused in the current demo; ROS integration comes later.

Use the linked Pi 4 Ubuntu 20.04 and proposed Pi 5 Ubuntu 24.04 guides. Select this lab's dependencies, audio settings, GPIO library, and wiring per board rather than assuming interchangeability. No hardware runs are recorded on either board. Follow the lab template to specify actual parts, PSU, settings, pins, and versions, then record results in the compatibility matrix. This initial guide contains no validated hardware or ROS installation commands.

Start with the linked simulated lamp exercise. Its source is in this lab directory under `src/arabic_home/`.

</div>
