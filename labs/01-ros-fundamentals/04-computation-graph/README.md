<div dir="rtl" lang="ar">

# شبكة معالجة البيانات

**مرجع الخطة:** <code dir="ltr">2.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يعرف <span dir="ltr">ROS Master</span> أسماء العقد وواجهات الاتصال، ثم تتبادل العقد بيانات المواضيع مباشرة. الموضوع تدفق غير متزامن يمكن أن يملك عدة مشتركين. الخدمة طلب ورد. معاملات التشغيل إعدادات مشتركة وليست قناة مناسبة لبث بيانات الحساسات. الرسم البياني يصف البرامج أثناء التشغيل، وليس ترتيب مجلدات الكود.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر. هذا بند قراءة مع تجربة توضيحية؛ لا يضيف تقييما عمليا إلى الخطة.

<div dir="ltr">

```bash
roslaunch course_basics communication.launch
```

</div>

<div dir="ltr">

```bash
# Another sourced terminal
rosnode info /course_talker
rostopic info /course/chatter
rqt_graph
```

</div>

## النتيجة المتوقعة والتحقق

يظهر الناشر والمشترك وموضوع الرسائل. يحتاج <span dir="ltr">rqt_graph</span> شاشة رسومية؛ تكفي أوامر الفحص النصي في بيئة بلا شاشة.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

أوقف المستمع وسجل اختلاف الرسم. فسر لماذا يستطيع الناشر الاستمرار. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)
- [Node implementations](../ros/course_basics/scripts/)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Computation graph

**Syllabus reference:** `2.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

The ROS master provides discovery; nodes then exchange topic data directly. Topics stream asynchronous messages, services provide request/reply, and parameters hold configuration. The runtime computation graph differs from the package directory structure.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model. This reading item includes a demonstration; it does not add a syllabus assessment.

```bash
roslaunch course_basics communication.launch
```

```bash
# Another sourced terminal
rosnode info /course_talker
rostopic info /course/chatter
rqt_graph
```

## Expected result and validation

The graph shows publisher, subscriber and topic. rqt_graph needs a graphical session; CLI inspection also works headlessly.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Stop the listener, record the graph change and explain why the publisher can continue. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)
- [Node implementations](../ros/course_basics/scripts/)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
