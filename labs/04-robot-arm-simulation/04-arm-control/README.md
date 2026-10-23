<div dir="rtl" lang="ar">

# التحكم بالذراع باستخدام <span dir="ltr">ROS</span> و<span dir="ltr">rqt</span>

**مرجع الخطة:** <code dir="ltr">10.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يربط <span dir="ltr">gazebo_ros_control</span> مفاصل المحاكاة بمتحكمات <span dir="ltr">ros_control.</span> يحمل كل مفصل متحكم موضع يعمل بجهد مع <span dir="ltr">PID</span>، وينشر <span dir="ltr">joint_state_controller</span> المواضع المقاسة. وحدة الأمر راديان للمفاصل الدورانية ومتر للقابض. ترسل أداة <span dir="ltr">pose</span> هدفا داخل الحدود؛ ثم نقارن الحالة المقاسة بالهدف.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
roslaunch course_arm gazebo.launch gui:=false
```

</div>

<div dir="ltr">

```bash
# Another sourced terminal
rosservice call /arm/controller_manager/list_controllers
rosrun course_arm pose.py --shoulder 0.25 --elbow -0.4 --wrist 0.2 --gripper 0.02
rostopic echo -n 1 /arm/joint_states
rqt_publisher
```

</div>

## النتيجة المتوقعة والتحقق

تظهر المتحكمات في حالة <span dir="ltr">running</span> وتقترب المفاصل من الأهداف. في <span dir="ltr">rqt_publisher</span> اختر موضوع الكتف ونوع <span dir="ltr">std_msgs/Float64</span> وقيمة <span dir="ltr">0.2</span> وترددا منخفضا؛ أوقف النشر قبل تبديل أداة التحكم.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

قارن ثلاثة أهداف مسموحة، وسجل زمن الاقتراب والخطأ المتبقي، ثم فسر أثر تغيير <span dir="ltr">PID</span> في نسخة تدريبية. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Model, controllers and scripts](../ros/course_arm/)
- [Gazebo ROS control](https://classic.gazebosim.org/tutorials?tut=ros_control)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Arm control using ROS and rqt

**Syllabus reference:** `10.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

gazebo_ros_control exposes simulated joints to ros_control. Effort-based position controllers use PID and the joint state controller publishes measured positions. Revolute commands use radians; gripper commands use meters. Compare reported positions with the bounded pose command.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
roslaunch course_arm gazebo.launch gui:=false
```

```bash
# Another sourced terminal
rosservice call /arm/controller_manager/list_controllers
rosrun course_arm pose.py --shoulder 0.25 --elbow -0.4 --wrist 0.2 --gripper 0.02
rostopic echo -n 1 /arm/joint_states
rqt_publisher
```

## Expected result and validation

Controllers should be running and measured joints should approach their targets. In rqt_publisher choose the shoulder command topic, std_msgs/Float64, value 0.2 and a low rate. Stop publishing before switching command tools.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Compare three legal targets, record settling time/residual error, and explain a PID change in a training copy. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Model, controllers and scripts](../ros/course_arm/)
- [Gazebo ROS control](https://classic.gazebosim.org/tutorials?tut=ros_control)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
