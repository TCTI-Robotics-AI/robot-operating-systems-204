# ربط التجارب بخطة المقرر

مقرر أنظمة تشغيل الروبوتات 204 روبوت يتضمن 32 ساعة تدريبية موزعة على 16 أسبوعًا تدريبيًا، والاختبار النهائي في الأسبوع 17. هذه الخريطة تنظيم مقترح لتطبيقاته داخل المشروع.

| الأسابيع | موضوع الخطة | تطبيق المشروع المستهدف |
| --- | --- | --- |
| 1 إلى 3 | أساسيات ROS ومستوياته والاتصال والأدوات | [تمرين أساسيات ROS](../labs/02-ros-fundamentals/README.md) |
| 4 إلى 5 | التثبيت وrosdep وrosinstall وCatkin | [تجهيز البيئة](../labs/01-linux-and-setup/README.md) |
| 6 إلى 7 | روبوت بعجلتين وRViz وURDF وGazebo وSDF | [محاكاة الروبوت المتحرك](../labs/03-mobile-robot-simulation/README.md) |
| 8 إلى 10 | ذراع روبوت وXacro وmesh وrqt | [محاكاة الذراع](../labs/04-robot-arm-simulation/README.md) |
| 11 إلى 13 | AIML وPyAIML والصوت وClient وServer | [الصوت](../labs/05-arabic-speech/README.md) و[المحادثة](../labs/06-conversation/README.md) |
| 14 | ربط Arduino وSTM32 | [ربط الأنظمة المدمجة](../labs/08-embedded-interfaces/README.md) |
| 15 | ربط Raspberry Pi | [التحكم بالأطراف](../labs/07-gpio-control/README.md) |
| 16 | ربط Odroid والمراجعة | [ربط الأنظمة المدمجة](../labs/08-embedded-interfaces/README.md) والمراجعة |

## إضافات المشروع

النموذج اللغوي الحديث وتكامل WhatsApp إضافات، بينما يبقى درس AIML موجودًا لتغطية موضوع الخطة. استخدام Pi 4 وPi 5 تكييف للتجربة التي تذكر Raspberry Pi 2 في الخطة.

المصدر: ملف المدرب وتوصيف المقرر المحلي، الصفحات 2 و4 و5. بيانات الوصول إليه في [فهرس المراجع](../references/README.md).

## English

Robot Operating Systems course 204 contains 32 training hours over 16 teaching weeks, with the final assessment in week 17. The following is the proposed mapping to repository experiments.

| Weeks | Course topics | Planned application |
| --- | --- | --- |
| 1 to 3 | ROS fundamentals, levels, communication, tools | Components, nodes, messages, and command exchange |
| 4 to 5 | Installation, rosdep, rosinstall, Catkin | Learner setup and first package |
| 6 to 7 | Two wheel robot, RViz, URDF, Gazebo, SDF | Mobile robot simulation |
| 8 to 10 | Robot arm, Xacro, meshes, rqt | Arm modeling and control |
| 11 to 13 | AIML, PyAIML, audio, client and server nodes | Educational conversation, speech recognition, node integration |
| 14 | Arduino and STM32 integration | Separate examples when boards are available |
| 15 | Raspberry Pi integration | Arabic commands controlling an LED |
| 16 | Odroid and review | Integration lesson when hardware is available, project review |

Modern language models and WhatsApp are extensions. The AIML lesson remains part of course coverage. Pi 4 and Pi 5 adapt the course example, which names Pi 2. Source: pages 2, 4, and 5 of the local trainer course outline; see the [reference index](../references/README.md).

معرفات التمارين لا تمثل أرقام الأسابيع. كل روابط التطبيقات تشير إلى نطاقات عمل مخططة باستثناء التجربة النصية المحددة في الفهرس. راجع [فهرس التمارين باللغتين](../labs/README.md) للحالة وروابط كل موضوع.

Lab IDs are not week numbers. The linked applications are planned scopes except for the text demo identified in the bilingual [lab catalog](../labs/README.md), which provides current status and links for each topic.
