<div dir="rtl" lang="ar">

# التحكم بالروبوت داخل المحاكاة

**مرجع الخطة:** <code dir="ltr">7.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

تحمل رسالة <span dir="ltr">Twist</span> سرعة خطية وزاوية. يحول مشغل القيادة التفاضلية الطلب إلى دوران العجلتين، وينشر <span dir="ltr">odometry.</span> تحد أداة القيادة السرعة والزمن وترسل صفرا عند انتهاء التشغيل. نقيس تغير الموضع والتوقف بدل الاكتفاء بأن أمر النشر لم يظهر خطأ.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
roslaunch course_mobile gazebo.launch gui:=false
```

</div>

<div dir="ltr">

```bash
# Another sourced terminal
rosrun course_mobile drive.py --linear 0.1 --seconds 3
rostopic echo -n 1 /odom
rosrun course_mobile drive.py --angular 0.4 --seconds 2
```

</div>

## النتيجة المتوقعة والتحقق

يتقدم الروبوت قرابة <span dir="ltr">0.3</span> متر في الطلب الأول ثم يتوقف. تختلف النتيجة قليلا حسب خطوة الفيزياء والاحتكاك؛ سجل القياس الفعلي.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

نفذ مسارا من تقدم ودوران وتقدم، وقارن موضع النهاية مع التوقع، ثم اختبر رفض سرعة خارج الحدود. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Model and launch files](../ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Simulated mobile robot control

**Syllabus reference:** `7.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Twist specifies linear and angular velocity. The differential drive plugin actuates wheel joints and publishes odometry. The drive tool bounds speed/duration and sends zero on exit. Verify measured displacement and stopping rather than command publication alone.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
roslaunch course_mobile gazebo.launch gui:=false
```

```bash
# Another sourced terminal
rosrun course_mobile drive.py --linear 0.1 --seconds 3
rostopic echo -n 1 /odom
rosrun course_mobile drive.py --angular 0.4 --seconds 2
```

## Expected result and validation

The first command should move about 0.3 m then stop. Physics stepping/friction cause small differences; record actual measured displacement.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Run forward/turn/forward, compare the final pose with prediction, and test rejection of an out-of-range speed. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Model and launch files](../ros/course_mobile/)
- [Gazebo ROS plugins](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
