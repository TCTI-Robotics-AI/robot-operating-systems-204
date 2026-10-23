<div dir="rtl" lang="ar">

# ربط التجارب بخطة المقرر

مقرر أنظمة تشغيل الروبوتات 204 روبوت يتضمن 32 ساعة تدريبية موزعة على 16 أسبوعًا تدريبيًا، والاختبار النهائي في الأسبوع 17. هذه الخريطة تنظيم مقترح لتطبيقاته داخل المشروع.

| الأسابيع | موضوع الخطة | تطبيق المشروع المستهدف |
| --- | --- | --- |
| 1 إلى 3 | أساسيات <span dir="ltr">ROS</span> ومستوياته والاتصال والأدوات | [تمرين أساسيات <span dir="ltr">ROS</span>](../labs/01-ros-fundamentals/README.md) |
| 4 إلى 5 | التثبيت و<span dir="ltr">rosdep</span> و<span dir="ltr">rosinstall</span> و<span dir="ltr">Catkin</span> | [تجهيز البيئة](../labs/02-installation-and-setup/README.md) |
| 6 إلى 7 | روبوت بعجلتين و<span dir="ltr">RViz</span> و<span dir="ltr">URDF</span> و<span dir="ltr">Gazebo</span> و<span dir="ltr">SDF</span> | [محاكاة الروبوت المتحرك](../labs/03-mobile-robot-simulation/README.md) |
| 8 إلى 10 | ذراع روبوت و<span dir="ltr">Xacro</span> و<span dir="ltr">mesh</span> و<span dir="ltr">rqt</span> | [محاكاة الذراع](../labs/04-robot-arm-simulation/README.md) |
| 11 إلى 13 | <span dir="ltr">AIML</span> و<span dir="ltr">PyAIML</span> والصوت و<span dir="ltr">Client</span> و<span dir="ltr">Server</span> | [الصوت](../labs/05-conversation-and-speech/06-speech-recognition/README.md) و[المحادثة](../labs/05-conversation-and-speech/README.md) |
| 14 | ربط <span dir="ltr">Arduino</span> و<span dir="ltr">STM32</span> | [ربط الأنظمة المدمجة](../labs/06-embedded-systems/README.md) |
| 15 | ربط <span dir="ltr">Raspberry Pi</span> | [التحكم بالأطراف](../labs/06-embedded-systems/03-raspberry-pi/README.md) |
| 16 | ربط <span dir="ltr">Odroid</span> والمراجعة | [ربط الأنظمة المدمجة](../labs/06-embedded-systems/README.md) والمراجعة |

13 تقييمًا عمليًا أسبوعيًا لا تعني 13 تمرينًا تفصيليًا. الأنظمة المدمجة وحدها تحتوي أربعة تمارين ربط. راجع [فهرس البنود المفصل](exercises-index.md) للعدد حسب الموضوع ومراجع الخطة.

## إضافات المشروع

النموذج اللغوي الحديث وتكامل <span dir="ltr">WhatsApp</span> إضافات، بينما يبقى درس <span dir="ltr">AIML</span> موجودًا لتغطية موضوع الخطة. استخدام <span dir="ltr">Pi 4</span> و<span dir="ltr">Pi 5</span> تكييف للتجربة التي تذكر <span dir="ltr">Raspberry Pi 2</span> في الخطة.

المصدر: ملف المدرب وتوصيف المقرر المحلي، الصفحات 2 و4 و5. بيانات الوصول إليه في [فهرس المراجع](../references/README.md).

معرفات التمارين لا تمثل أرقام الأسابيع. كل روابط التطبيقات تشير إلى نطاقات عمل مخططة باستثناء التجربة النصية المحددة في الفهرس. راجع [فهرس التمارين باللغتين](../labs/README.md) للحالة وروابط كل موضوع.

</div>

<div dir="ltr" lang="en">

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

Weekly practical assessment count is not the number of detailed exercises. Embedded systems contains four separate board integrations; see the [detailed index](exercises-index.md).

Modern language models and WhatsApp are extensions. The AIML lesson remains part of course coverage. Pi 4 and Pi 5 adapt the course example, which names Pi 2. Source: pages 2, 4, and 5 of the local trainer course outline; see the [reference index](../references/README.md).


Lab IDs are not week numbers. The bilingual [lab catalog](../labs/README.md) links implemented teaching materials and source; actual execution evidence is recorded separately in validation reports.

</div>
