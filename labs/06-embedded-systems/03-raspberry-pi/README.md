<div dir="rtl" lang="ar">

# الربط بين النظام وجهاز الرازبيري

**مرجع الخطة:** <code dir="ltr">15.2</code> · **الحالة:** التجربة النصية متوفرة، الربط الفعلي و<span dir="ltr">ROS</span> مخططان.

الخطة تذكر <span dir="ltr">Raspberry Pi 2</span>؛ نكيف التجربة لتستهدف <span dir="ltr">Pi 4</span> و<span dir="ltr">Pi 5</span> مع توثيق كل مسار والتحقق منه. التمرين الرسمي هدفه ربط الجهاز بـ<span dir="ltr">ROS</span>. التجربة النصية مرحلة تمهيدية ولا تعد دليلًا على اكتمال الربط.

## التجربة الحالية

ابدأ بـ[التحكم النصي بلمبة افتراضية](01-text-lamp/README.md). الكود داخل <code dir="ltr">src/arabic_home/</code> في مجلد هذا التمرين. أوامر التثبيت والتشغيل تنفذ من جذر المستودع.

## مسار الجهازين

- [<span dir="ltr">Pi 4</span> مع <span dir="ltr">Ubuntu 20.04</span>](../../../environments/pi4-ubuntu2004/README.md).
- [<span dir="ltr">Pi 5</span> مع <span dir="ltr">Ubuntu 24.04</span> المقترح](../../../environments/pi5-ubuntu2404/README.md).

لا يوجد ربط <span dir="ltr">ROS</span> أو <span dir="ltr">GPIO</span> معتمد بعد على أي منهما. تسجل مكتبة <span dir="ltr">GPIO</span> والأطراف الفيزيائية وترقيم <span dir="ltr">BCM</span> والمايك والصوت و<span dir="ltr">ROS</span> وإصداراتها في إعدادات كل مسار عند التنفيذ.

## القطع والتوصيل

التجربة النصية لا تحتاج قطعًا. مرحلة <span dir="ltr">LED</span> تحتاج لوحة تجارب و<span dir="ltr">LED</span> ومقاومة وأسلاك، مع مزود مناسب للرازبيري وتخزين وشبكة. الموديلات وقيمة المقاومة والتوصيل لم تعتمد بعد. راجع [قائمة القطع](../../../hardware/README.md) و[مصفوفة التحقق](../../../validation/compatibility.md).

[العودة إلى الأنظمة المدمجة](../README.md).

</div>

<div dir="ltr" lang="en">

# ROS and Raspberry Pi

**Syllabus reference:** `15.2`. The outline names Pi 2; the adaptation targets Pi 4 and Pi 5 with separate setup and validation. The current text demo is preparation and does not complete the ROS integration objective.

Start with the linked simulated lamp exercise. Its source is under this directory in `src/arabic_home/`; installation commands run from the repository root. Follow the linked Pi 4 Ubuntu 20.04 and proposed Pi 5 Ubuntu 24.04 profiles. Neither GPIO nor ROS integration is validated yet.

Document GPIO library, physical and BCM pins, audio devices, ROS and software versions per path. No circuit parts are needed for text. Physical LED work requires breadboard, LED, resistor, wires and suitable Pi power, storage and network. Models, resistor value and wiring remain unselected. Use the linked inventory and validation matrix before claiming compatibility.

</div>
