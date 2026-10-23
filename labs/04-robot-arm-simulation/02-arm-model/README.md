<div dir="rtl" lang="ar">

# تصميم ذراع من ثلاثة أجزاء

**مرجع الخطة:** <code dir="ltr">9.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يتكون الذراع من عضد وساعد ورسغ بأطوال <span dir="ltr">0.22</span> و<span dir="ltr">0.18</span> و<span dir="ltr">0.08</span> متر. يدور الكتف والمرفق حول المحور <span dir="ltr">Y</span>، ويدور الرسغ حول <span dir="ltr">Z.</span> القاعدة مثبتة بالعالم، ولكل جزء كتلة وعطالة وحدود للمفصل. يبقى عرض <span dir="ltr">RViz</span> مرحلة هندسية قبل اختبار التحكم الفيزيائي.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
roslaunch course_arm display.launch gripper:=false
```

</div>

<div dir="ltr">

```bash
# Another sourced terminal
rostopic echo -n 1 /arm/joint_states
rosparam get /robot_description
```

</div>

## النتيجة المتوقعة والتحقق

تظهر الأجزاء الثلاثة متصلة، وتنشر أسماء المفاصل الصحيحة. لا يوجد محرك فعلي في هذا التمرين.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

ارسم شجرة الروابط وحدد أصل كل مفصل ومحوره وحدوده، ثم احسب ارتفاع الذراع المستقيم. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Model, controllers and scripts](../ros/course_arm/)
- [Gazebo ROS control](https://classic.gazebosim.org/tutorials?tut=ros_control)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Three-part robot arm

**Syllabus reference:** `9.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

The upper arm, forearm and wrist measure 0.22, 0.18 and 0.08 m. Shoulder/elbow rotate around Y and wrist around Z. The base is fixed to world. Links have masses/inertias and joints have limits. RViz inspection precedes physical simulation.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
roslaunch course_arm display.launch gripper:=false
```

```bash
# Another sourced terminal
rostopic echo -n 1 /arm/joint_states
rosparam get /robot_description
```

## Expected result and validation

Three connected segments appear and joint names are published. This lab uses no physical motors.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Draw the link tree and annotate joint origins/axes/limits, then calculate the straight arm height. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Model, controllers and scripts](../ros/course_arm/)
- [Gazebo ROS control](https://classic.gazebosim.org/tutorials?tut=ros_control)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
