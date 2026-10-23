<div dir="rtl" lang="ar">

# إضافة القابض والمجسمات

**مرجع الخطة:** <code dir="ltr">9.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يضيف الشرط إصبعا ثابتا وآخر بمفصل انزلاقي. يستعمل الشكل المرئي ملف <span dir="ltr">STL</span> أصليا داخل المستودع، والتصادم صندوقا بسيطا لتقليل حساب الفيزياء. مدى حركة الإصبع <span dir="ltr">0</span> إلى <span dir="ltr">0.035</span> متر. انتبه لوحدات المجسمات؛ استيراد ملليمترات على أنها أمتار يفسد حجم النموذج.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
xacro "$(rospack find course_arm)/urdf/arm.urdf.xacro" gripper:=true > /tmp/course204-arm-gripper.urdf
check_urdf /tmp/course204-arm-gripper.urdf
roslaunch course_arm display.launch gripper:=true
```

</div>

## النتيجة المتوقعة والتحقق

تضاف أصابع القابض والمفصل الانزلاقي. ملف المجسم محلي، ولا يتطلب تنزيل نموذج مجهول الترخيص.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

قارن <span dir="ltr">visual</span> و<span dir="ltr">collision</span> لأحد الأصابع واشرح اختيار الشكل المبسط، ثم وثق وحدة <span dir="ltr">STL.</span> أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Model, controllers and scripts](../ros/course_arm/)
- [Gazebo ROS control](https://classic.gazebosim.org/tutorials?tut=ros_control)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Gripper and meshes

**Syllabus reference:** `9.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

The gripper adds a fixed finger and a prismatic finger. Visuals use an original repository STL while collision geometry remains a simple box. Finger travel is 0 to 0.035 m. Verify mesh units when importing geometry.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
xacro "$(rospack find course_arm)/urdf/arm.urdf.xacro" gripper:=true > /tmp/course204-arm-gripper.urdf
check_urdf /tmp/course204-arm-gripper.urdf
roslaunch course_arm display.launch gripper:=true
```

## Expected result and validation

The fingers and prismatic joint appear. The mesh is local and original, with no third-party model download.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Compare a finger visual/collision and justify simplified collision geometry; document STL units. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Model, controllers and scripts](../ros/course_arm/)
- [Gazebo ROS control](https://classic.gazebosim.org/tutorials?tut=ros_control)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
