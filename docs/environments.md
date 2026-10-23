# سياسة توافق الأجهزة والأنظمة

Pi 4 وPi 5 متوفران للمدرب والمتدربين؛ لا نقسم الأجهزة حسب دور صاحبها. يستهدف كل تمرين الجهازين، وتكتب الفروقات كمسارات إعداد داخل التمرين نفسه.

| المسار | الجهاز والنظام | الاستخدام | الحالة |
| --- | --- | --- | --- |
| pi4-ubuntu2004 | Pi 4 وUbuntu 20.04 arm64 | مواءمة المنهج القديم | مستهدف، لم يختبر |
| pi5-ubuntu2404 | Pi 5 وUbuntu 24.04 arm64 | مسار مقترح للجهاز الأحدث | مستهدف، لم يختبر |

يدعم [Ubuntu 20.04 جهاز Pi 4](https://documentation.ubuntu.com/release-notes/20.04/). يظهر دعم Ubuntu 24.04 للجهازين في [مصفوفة Canonical](https://ubuntu.com/hardware/docs/boards/how-to/ubuntu_supported/raspberry-pi/). لا يعتمد المشروع تثبيت Ubuntu 20.04 مباشرة على Pi 5.

اختيار Ubuntu 24.04 هدف توثيقي مقترح لمسار Pi 5، وليس وصفًا لنظام الجهاز الحالي أو إثباتًا لتوافق البرامج. لا تتضمن البنية الحالية مثبّتًا للنظام أو أمرًا لتغييره.

## ROS والمنهج

Catkin وAIML جزء من المنهج. نحتفظ بمسار ROS 1 التعليمي المناسب لهما. انتهى الدعم الرسمي لـROS Noetic في 31 مايو 2025 حسب [إعلان ROS](https://discourse.openrobotics.org/t/ros-noetic-end-of-life-may-31-2025/43160)، لذلك يوثق كبيئة منهج قديمة وليس كخيار حديث مدعوم.

مسار ROS 1 على Pi 5 لم يعتمد. فصل تشغيل ROS عن منفذ GPIO أو استخدام حاوية احتمالات تحتاج تجارب، خصوصًا للصوت والأجهزة. لا نعمم أوامر Catkin على نظام أحدث، ولا نستبدل المنهج تلقائيًا بـROS 2.

## معنى التوافق

- مستهدف: مطلوب تصميم التمرين للجهاز؛ لا يوجد سجل تشغيل مثبت.
- تم التحقق: سجل فعلي يحدد الجهاز والنظام والقطع والإصدارات والنتيجة.
- متعذر: عائق موثق مع السبب والخطوة اللازمة أو البديل.
- غير منطبق: جزء لا يحتاج تلك الوظيفة؛ مثل غياب GPIO عن التمرين النصي.

راجع [ملفات البيئات](../environments/README.md) و[مصفوفة التحقق](../validation/compatibility.md). قيم null في أمثلة الإعداد تعني أنها لم تحدد بعد.

## English

Pi 4 and Pi 5 are both instructor and learner boards. Every lab targets both with separate setup paths where needed. Pi 4 uses the arm64 Ubuntu 20.04 course track; Pi 5 has a proposed arm64 Ubuntu 24.04 track. Both are untested with this project.

The linked Ubuntu release notes establish Pi 4 support on 20.04; Canonical's matrix lists both boards on 24.04. Native Ubuntu 20.04 is not the Pi 5 path. The proposed OS is not a claim about the installed OS or application compatibility. No installer changes a board OS here.

Retain Catkin and AIML course coverage. Noetic reached official end of life on May 31, 2025, per the linked ROS announcement, and is a legacy course environment. A ROS 1 path on Pi 5 is not validated. Containers or separating ROS execution from GPIO remain possibilities to test. Do not assume Catkin works on a newer OS or silently substitute ROS 2.

Targeted means intended support without a recorded run. Verified requires actual hardware, OS, versions, and results. Blocked records a failure and next step. Not applicable means that function is not used, without implying GPIO support. JSON null values indicate unselected settings.
