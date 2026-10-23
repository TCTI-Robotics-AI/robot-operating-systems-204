<div dir="rtl" lang="ar">

# إعداد <span dir="ltr">Raspberry Pi 5</span>

المسار المقترح: <span dir="ltr">Ubuntu 24.04 arm64.</span> النظام المثبت غير معروف ولم تختبر تجارب المشروع على الجهاز.

1. سجل موديل اللوحة والنظام الفعلي؛ لا تستخدم خطوات <span dir="ltr">Ubuntu 20.04</span> المباشرة على <span dir="ltr">Pi 5.</span>
2. للتجربة النصية اتبع البيئة الافتراضية في الدليل الرئيسي؛ لا تحتاج <span dir="ltr">ROS</span> أو صوتًا أو <span dir="ltr">GPIO</span>.
3. اختر المايك ومخرج الصوت ومكتبة <span dir="ltr">GPIO</span> بعد التحقق من دعم الجهاز والنظام، وسجل القطع والإصدارات.
4. أكمل [مثال الإعداد](environment.example.json) محليًا. لا توجد أطراف أو أجهزة صوت محددة مسبقًا؛ البرنامج الحالي لا يقرأ الملف.
5. اختبر مسار <span dir="ltr">ROS</span> مستقلًا. تشغيل <span dir="ltr">Ubuntu 24.04</span> لا يثبت تشغيل <span dir="ltr">ROS 1</span> أو <span dir="ltr">Catkin</span>. لا توجد حاوية <span dir="ltr">ROS</span> معتمدة.
6. سجل النتائج والفروق عن <span dir="ltr">Pi 4</span> في [التحقق](../../validation/README.md).

</div>

<div dir="ltr" lang="en">

## English

Proposed target: arm64 Ubuntu 24.04. The installed OS is unknown and hardware validation is pending. Record the actual board and OS; native Ubuntu 20.04 instructions do not apply. The text demo uses the root README setup without audio, GPIO, or ROS. Select compatible audio devices and a GPIO library, and record models and versions. Complete the JSON example locally; pins and audio devices are unselected and the demo does not load it. Validate ROS separately: OS support does not prove ROS 1 or Catkin support, and no ROS container is validated. Record results and differences from Pi 4.

</div>
