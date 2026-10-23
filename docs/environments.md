<div dir="rtl" lang="ar">

# سياسة توافق الأجهزة والأنظمة

<span dir="ltr">Pi 4</span> و<span dir="ltr">Pi 5</span> متوفران للمدرب والمتدربين؛ لا نقسم الأجهزة حسب دور صاحبها. يستهدف كل تمرين الجهازين، وتكتب الفروقات كمسارات إعداد داخل التمرين نفسه.

| المسار | الجهاز والنظام | الاستخدام | الحالة |
| --- | --- | --- | --- |
| <span dir="ltr">pi4-ubuntu2004</span> | <span dir="ltr">Pi 4</span> و<span dir="ltr">Ubuntu 20.04 arm64</span> | مواءمة المنهج القديم | مستهدف، لم يختبر |
| <span dir="ltr">pi5-ubuntu2404</span> | <span dir="ltr">Pi 5</span> و<span dir="ltr">Ubuntu 24.04 arm64</span> | مسار مقترح للجهاز الأحدث | مستهدف، لم يختبر |

يدعم [<span dir="ltr">Ubuntu 20.04</span> جهاز <span dir="ltr">Pi 4</span>](https://documentation.ubuntu.com/release-notes/20.04/). يظهر دعم <span dir="ltr">Ubuntu 24.04</span> للجهازين في [مصفوفة <span dir="ltr">Canonical</span>](https://ubuntu.com/hardware/docs/boards/how-to/ubuntu_supported/raspberry-pi/). لا يعتمد المشروع تثبيت <span dir="ltr">Ubuntu 20.04</span> مباشرة على <span dir="ltr">Pi 5</span>.

اختيار <span dir="ltr">Ubuntu 24.04</span> هدف توثيقي مقترح لمسار <span dir="ltr">Pi 5</span>، وليس وصفًا لنظام الجهاز الحالي أو إثباتًا لتوافق البرامج. لا تتضمن البنية الحالية مثبّتًا للنظام أو أمرًا لتغييره.

## <span dir="ltr">ROS</span> والمنهج

<span dir="ltr">Catkin</span> و<span dir="ltr">AIML</span> جزء من المنهج. نحتفظ بمسار <span dir="ltr">ROS 1</span> التعليمي المناسب لهما. انتهى الدعم الرسمي لـ<span dir="ltr">ROS Noetic</span> في 31 مايو 2025 حسب [إعلان <span dir="ltr">ROS</span>](https://discourse.openrobotics.org/t/ros-noetic-end-of-life-may-31-2025/43160)، لذلك يوثق كبيئة منهج قديمة وليس كخيار حديث مدعوم.

مسار <span dir="ltr">ROS 1</span> على <span dir="ltr">Pi 5</span> لم يعتمد. فصل تشغيل <span dir="ltr">ROS</span> عن منفذ <span dir="ltr">GPIO</span> أو استخدام حاوية احتمالات تحتاج تجارب، خصوصًا للصوت والأجهزة. لا نعمم أوامر <span dir="ltr">Catkin</span> على نظام أحدث، ولا نستبدل المنهج تلقائيًا بـ<span dir="ltr">ROS 2</span>.

## معنى التوافق

- مستهدف: مطلوب تصميم التمرين للجهاز؛ لا يوجد سجل تشغيل مثبت.
- تم التحقق: سجل فعلي يحدد الجهاز والنظام والقطع والإصدارات والنتيجة.
- متعذر: عائق موثق مع السبب والخطوة اللازمة أو البديل.
- غير منطبق: جزء لا يحتاج تلك الوظيفة؛ مثل غياب <span dir="ltr">GPIO</span> عن التمرين النصي.

راجع [ملفات البيئات](../environments/README.md) و[مصفوفة التحقق](../validation/compatibility.md). قيم <span dir="ltr">null</span> في أمثلة الإعداد تعني أنها لم تحدد بعد.

</div>

<div dir="ltr" lang="en">

## English

Pi 4 and Pi 5 are both instructor and learner boards. Every lab targets both with separate setup paths where needed. Pi 4 uses the arm64 Ubuntu 20.04 course track; Pi 5 has a proposed arm64 Ubuntu 24.04 track. Both are untested with this project.

The linked Ubuntu release notes establish Pi 4 support on 20.04; Canonical's matrix lists both boards on 24.04. Native Ubuntu 20.04 is not the Pi 5 path. The proposed OS is not a claim about the installed OS or application compatibility. No installer changes a board OS here.

Retain Catkin and AIML course coverage. Noetic reached official end of life on May 31, 2025, per the linked ROS announcement, and is a legacy course environment. A ROS 1 path on Pi 5 is not validated. Containers or separating ROS execution from GPIO remain possibilities to test. Do not assume Catkin works on a newer OS or silently substitute ROS 2.

Targeted means intended support without a recorded run. Verified requires actual hardware, OS, versions, and results. Blocked records a failure and next step. Not applicable means that function is not used, without implying GPIO support. JSON null values indicate unselected settings.

</div>
