<div dir="rtl" lang="ar">

# بناء الحزم وعرض الروبوت

**مرجع الخطة:** <code dir="ltr">6.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

تجمع <span dir="ltr">course_mobile</span> وصف الروبوت ومشهد المحاكاة وملفات العرض. يقرأ <span dir="ltr">robot_state_publisher</span> المفاصل وينشر التحويلات، ويعرض <span dir="ltr">RViz</span> النموذج داخل إطار <span dir="ltr">base_link.</span> وضع العرض يستخدم ناشر مفاصل فقط ولا يشغل فيزياء. أعد البناء بعد إضافة ملفات إلى قواعد التثبيت.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
bash tools/build.sh ~/course204_ws
source ~/course204_ws/devel/setup.bash
rospack find course_mobile
roslaunch course_mobile display.launch
```

</div>

## النتيجة المتوقعة والتحقق

تظهر قاعدة زرقاء وعجلتان ودعامتان في <span dir="ltr">RViz.</span> في بيئة بلا شاشة استخدم <span dir="ltr">rviz:=false</span> وافحص /<span dir="ltr">joint_states</span> و/<span dir="ltr">tf.</span>

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

غير لون القاعدة في نسخة تدريبية ثم سجل الفرق بين التغيير المرئي وتغيير الكتلة. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Model and launch files](../ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Package building and RViz

**Syllabus reference:** `6.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

course_mobile contains the robot, world and visualization files. robot_state_publisher produces transforms from joint states. RViz displays the model in base_link. The display launch uses a joint state publisher and has no physics.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
bash tools/build.sh ~/course204_ws
source ~/course204_ws/devel/setup.bash
rospack find course_mobile
roslaunch course_mobile display.launch
```

## Expected result and validation

RViz shows a blue base, two wheels and two support spheres. Headless users may set rviz:=false and inspect /joint_states and /tf.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Change the base color and explain why changing color differs from changing mass. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Model and launch files](../ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
