<div dir="rtl" lang="ar">

# المكتبات والأدوات والمحاكاة

**مرجع الخطة:** <code dir="ltr">3.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

تجمع <span dir="ltr">rostopic</span> و<span dir="ltr">rosservice</span> أدلة الاتصال، ويعرض <span dir="ltr">RViz</span> الروبوت والبيانات والتحويلات، بينما يحسب <span dir="ltr">Gazebo</span> التصادم والحركة والفيزياء. يستخدم المقرر <span dir="ltr">Gazebo Classic 11</span> مع <span dir="ltr">Noetic</span> لأن هذا اقتران المنهج القديم. انتهى دعم هذه البيئة؛ لا تعني صلاحيتها للتدريس أنها بيئة إنتاج حديثة مدعومة.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر. هذا بند قراءة مع تجربة توضيحية؛ لا يضيف تقييما عمليا إلى الخطة.

<div dir="ltr">

```bash
rosversion rviz
gazebo --version
roslaunch course_mobile display.launch
```

</div>

<div dir="ltr">

```bash
# Stop the previous launch before starting this
roslaunch course_mobile gazebo.launch gui:=false
```

</div>

## النتيجة المتوقعة والتحقق

عرض النموذج لا يعني أنه يخضع للفيزياء. المحاكاة دون واجهة رسومية تنشر بيانات فعلية داخل <span dir="ltr">ROS.</span>

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

قارن وظيفة كل أداة، وحدد الأدلة التي تستخدمها لاختبار الحركة دون شاشة. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Model and launch files](../../03-mobile-robot-simulation/ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)
- [Gazebo and ROS version pairing](https://classic.gazebosim.org/tutorials?tut=ros_wrapper_versions)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Libraries, tools and simulators

**Syllabus reference:** `3.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

rostopic and rosservice inspect communication. RViz visualizes models, messages and transforms; Gazebo simulates physics and collisions. The syllabus path uses Gazebo Classic 11 with Noetic, a legacy pairing whose upstream support has ended.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model. This reading item includes a demonstration; it does not add a syllabus assessment.

```bash
rosversion rviz
gazebo --version
roslaunch course_mobile display.launch
```

```bash
# Stop the previous launch before starting this
roslaunch course_mobile gazebo.launch gui:=false
```

## Expected result and validation

A displayed model is not proof of physics. The headless Gazebo launch publishes actual simulation data to ROS.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Compare the tools and identify evidence for testing motion without a GUI. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Model and launch files](../../03-mobile-robot-simulation/ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)
- [Gazebo and ROS version pairing](https://classic.gazebosim.org/tutorials?tut=ros_wrapper_versions)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
