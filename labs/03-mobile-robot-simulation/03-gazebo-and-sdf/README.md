<div dir="rtl" lang="ar">

# <span dir="ltr">Gazebo</span> والتحويل إلى <span dir="ltr">SDF</span>

**مرجع الخطة:** <code dir="ltr">7.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يضيف <span dir="ltr">SDF</span> وصف العالم والفيزياء والحساسات إلى وصف الأجسام. يحول <span dir="ltr">Gazebo</span> ملف <span dir="ltr">URDF</span> عند إدخاله، ويمكن فحص الناتج نصيا. مشهد المقرر أرض وضوء محليان، فلا يعتمد على تنزيل نماذج خارجية. قارن التحويل مع المصدر؛ قد تدمج المفاصل الثابتة أثناء التحويل.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
gz sdf -p "$(rospack find course_mobile)/urdf/mobile.urdf" > /tmp/course204-mobile.sdf
head -n 20 /tmp/course204-mobile.sdf
roslaunch course_mobile gazebo.launch gui:=false
```

</div>

<div dir="ltr">

```bash
# Another sourced terminal
rosservice list
rostopic echo -n 1 /odom
```

</div>

## النتيجة المتوقعة والتحقق

ينتج ملف <span dir="ltr">SDF</span>، ويضاف الروبوت إلى العالم وتصل رسالة تموضع. استخدم <span dir="ltr">gui:=true</span> على جهاز ذي جلسة رسومية مناسبة.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

قارن رابط عجلة قبل التحويل وبعده، وحدد إعدادات الفيزياء ومشغل <span dir="ltr">ROS.</span> أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Model and launch files](../ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)
- [SDFormat specification](https://sdformat.org/spec)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Gazebo and URDF to SDF conversion

**Syllabus reference:** `7.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

SDF represents worlds, physics and sensors as well as models. Gazebo converts URDF on insertion, and gz can print the conversion. The course world uses a local plane and light with no external model downloads. Fixed joints may be merged during conversion.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
gz sdf -p "$(rospack find course_mobile)/urdf/mobile.urdf" > /tmp/course204-mobile.sdf
head -n 20 /tmp/course204-mobile.sdf
roslaunch course_mobile gazebo.launch gui:=false
```

```bash
# Another sourced terminal
rosservice list
rostopic echo -n 1 /odom
```

## Expected result and validation

An SDF file is produced, the robot spawns and odometry arrives. Use gui:=true with a suitable graphical session.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Compare a wheel before/after conversion and locate physics and ROS plugin settings. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Model and launch files](../ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)
- [SDFormat specification](https://sdformat.org/spec)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
