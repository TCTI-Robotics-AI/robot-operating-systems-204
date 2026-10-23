# إعداد Raspberry Pi 5

المسار المقترح: Ubuntu 24.04 arm64. النظام المثبت غير معروف ولم تختبر تجارب المشروع على الجهاز.

1. سجل موديل اللوحة والنظام الفعلي؛ لا تستخدم خطوات Ubuntu 20.04 المباشرة على Pi 5.
2. للتجربة النصية اتبع البيئة الافتراضية في الدليل الرئيسي؛ لا تحتاج ROS أو صوتًا أو GPIO.
3. اختر المايك ومخرج الصوت ومكتبة GPIO بعد التحقق من دعم الجهاز والنظام، وسجل القطع والإصدارات.
4. أكمل [مثال الإعداد](environment.example.json) محليًا. لا توجد أطراف أو أجهزة صوت محددة مسبقًا؛ البرنامج الحالي لا يقرأ الملف.
5. اختبر مسار ROS مستقلًا. تشغيل Ubuntu 24.04 لا يثبت تشغيل ROS 1 أو Catkin. لا توجد حاوية ROS معتمدة.
6. سجل النتائج والفروق عن Pi 4 في [التحقق](../../validation/README.md).

## English

Proposed target: arm64 Ubuntu 24.04. The installed OS is unknown and hardware validation is pending. Record the actual board and OS; native Ubuntu 20.04 instructions do not apply. The text demo uses the root README setup without audio, GPIO, or ROS. Select compatible audio devices and a GPIO library, and record models and versions. Complete the JSON example locally; pins and audio devices are unselected and the demo does not load it. Validate ROS separately: OS support does not prove ROS 1 or Catkin support, and no ROS container is validated. Record results and differences from Pi 4.
