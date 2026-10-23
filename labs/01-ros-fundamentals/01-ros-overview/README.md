<div dir="rtl" lang="ar">

# التعرف على <span dir="ltr">ROS</span> ومميزاته

**مرجع الخطة:** <code dir="ltr">1.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

<span dir="ltr">ROS</span> منظومة مكتبات وأدوات تعمل فوق نظام التشغيل. العقد برامج مستقلة، والرسائل تصف البيانات المتبادلة، والحزم تجمع الكود والاعتماديات. مثالنا عقدة تنشر تحية وأخرى تستقبلها؛ يمكن تعديل إحداهما دون دمج التطبيق كله في برنامج واحد. ندرس <span dir="ltr">ROS 1 Noetic</span> لتوافقه مع <span dir="ltr">Catkin</span> في الخطة، مع توثيق انتهاء دعمه.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر. هذا بند قراءة مع تجربة توضيحية؛ لا يضيف تقييما عمليا إلى الخطة.

<div dir="ltr">

```bash
source ~/course204_ws/devel/setup.bash
rosversion -d
roslaunch course_basics communication.launch
```

</div>

<div dir="ltr">

```bash
# In another sourced terminal
rosnode list
rostopic echo -n 2 /course/chatter
```

</div>

## النتيجة المتوقعة والتحقق

تظهر عقدتا النشر والاستقبال، وتصل رسالتان إلى الموضوع. هذا يثبت الاتصال البرمجي ولا يستخدم عتادا.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

ارسم العلاقة بين نظام التشغيل و<span dir="ltr">ROS</span> والعقدتين، واشرح ما يحدث عند إيقاف المستمع فقط. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# ROS overview and features

**Syllabus reference:** `1.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

ROS supplies libraries, tools and communication conventions above the operating system. Nodes are processes, messages define data and packages group source and dependencies. Our talker and listener demonstrate independent components. This course retains ROS 1 Noetic and Catkin as a documented legacy teaching environment.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model. This reading item includes a demonstration; it does not add a syllabus assessment.

```bash
source ~/course204_ws/devel/setup.bash
rosversion -d
roslaunch course_basics communication.launch
```

```bash
# In another sourced terminal
rosnode list
rostopic echo -n 2 /course/chatter
```

## Expected result and validation

The nodes appear and two topic messages arrive. This is software communication with no device hardware.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Draw the OS, ROS and both nodes. Explain what changes when only the listener stops. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
