<div dir="rtl" lang="ar">

# التعرف على <span dir="ltr">Xacro</span>

**مرجع الخطة:** <code dir="ltr">8.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يقلل <span dir="ltr">Xacro</span> تكرار وصف الروبوت باستخدام خصائص وماكرو وشروط. يعرف النموذج ماكرو للأجزاء وآخر لنقل الحركة، ويتيح إضافة القابض أو حذفه. التوسيع ينتج <span dir="ltr">URDF</span> عاديا؛ نفحص الناتج قبل تحميله في <span dir="ltr">ROS</span> أو <span dir="ltr">Gazebo.</span>

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
xacro "$(rospack find course_arm)/urdf/arm.urdf.xacro" gripper:=false > /tmp/course204-arm.urdf
check_urdf /tmp/course204-arm.urdf
roslaunch course_arm display.launch gripper:=false
```

</div>

## النتيجة المتوقعة والتحقق

ينتج ذراع بثلاثة مفاصل متحركة دون قابض. تظهر الحدود والمحاور في ملف <span dir="ltr">URDF</span> الموسع.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

عدل طول جزء من خلال مدخل الماكرو، واشرح أثره على أصل المفصل التالي والعطالة. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Model, controllers and scripts](../ros/course_arm/)
- [Gazebo ROS control](https://classic.gazebosim.org/tutorials?tut=ros_control)
- [Xacro documentation](https://wiki.ros.org/xacro)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Xacro introduction

**Syllabus reference:** `8.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Xacro reduces repeated XML using properties, macros and conditions. The arm defines reusable segment and transmission macros and a conditional gripper. Expansion produces ordinary URDF, which should be checked before loading.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
xacro "$(rospack find course_arm)/urdf/arm.urdf.xacro" gripper:=false > /tmp/course204-arm.urdf
check_urdf /tmp/course204-arm.urdf
roslaunch course_arm display.launch gripper:=false
```

## Expected result and validation

The expansion contains three movable arm joints and no gripper. Inspect joint limits and axes in the expanded URDF.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Change a segment macro length and explain implications for the next joint origin and inertia. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Model, controllers and scripts](../ros/course_arm/)
- [Gazebo ROS control](https://classic.gazebosim.org/tutorials?tut=ros_control)
- [Xacro documentation](https://wiki.ros.org/xacro)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
