<div dir="rtl" lang="ar">

# وصف الروبوت بملف <span dir="ltr">URDF</span>

**مرجع الخطة:** <code dir="ltr">6.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يصف <span dir="ltr">link</span> جسما صلبا و<span dir="ltr">joint</span> العلاقة بين جسمين. نفصل الشكل المرئي عن شكل التصادم والعطالة. وحدات النموذج متر وكيلوجرام وراديان. نصف قطر العجلة <span dir="ltr">0.06</span> متر والمسافة بين مركزي العجلتين <span dir="ltr">0.25</span> متر؛ يجب أن تتفق قيم الوصف مع إعداد مشغل الحركة.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
source ~/course204_ws/devel/setup.bash
check_urdf "$(rospack find course_mobile)/urdf/mobile.urdf"
roslaunch course_mobile display.launch
```

</div>

## النتيجة المتوقعة والتحقق

يعرض المدقق شجرة الروابط دون خطأ. صحة <span dir="ltr">XML</span> أو شجرة الروبوت لا تكفي لضمان اتزانه في الفيزياء.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

حدد محور كل عجلة، ثم احسب قطرها وقارن بالقيمة المستخدمة في مشغل الحركة. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Model and launch files](../ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)
- [URDF tutorials](https://wiki.ros.org/urdf/Tutorials)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# URDF mobile robot model

**Syllabus reference:** `6.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Links represent rigid bodies and joints connect them. Visual geometry, collision geometry and inertia have different roles. Units are meters, kilograms and radians. The 0.06 m wheel radius and 0.25 m wheel separation must match the drive plugin.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
source ~/course204_ws/devel/setup.bash
check_urdf "$(rospack find course_mobile)/urdf/mobile.urdf"
roslaunch course_mobile display.launch
```

## Expected result and validation

The validator prints a valid link tree. XML/tree validity alone does not establish physical stability.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Identify each wheel axis, calculate the wheel diameter and compare it with the drive plugin setting. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Model and launch files](../ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)
- [URDF tutorials](https://wiki.ros.org/urdf/Tutorials)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
