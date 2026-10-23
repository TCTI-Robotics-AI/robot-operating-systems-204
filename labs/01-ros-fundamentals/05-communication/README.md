<div dir="rtl" lang="ar">

# الاتصال بين أجزاء النظام

**مرجع الخطة:** <code dir="ltr">3.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

نقارن تدفق <span dir="ltr">String</span> في موضوع مع خدمة <span dir="ltr">SetBool.</span> الأولى تناسب الأخبار المتكررة، والثانية تناسب أمرا يحتاج ردا. الخدمة هنا افتراضية لتعلم الاتصال؛ لاحقا تعيد خدمة الأجهزة نجاح التنفيذ وحالة خرج اللوحة بدل الاكتفاء باستقبال الطلب.

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
rostopic type /course/chatter
rosservice type /course/set_demo
rosservice call /course/set_demo "data: true"
rostopic echo -n 1 /course/demo_state
rosservice call /course/set_demo "data: false"
```

</div>

## النتيجة المتوقعة والتحقق

يرجع الطلب نجاحا وتتغير الحالة المنشورة. تتضح بنية الرسالة والخدمة من نوعيهما.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

اشرح لماذا يجب ألا تعرض واجهة تحكم نجاح تشغيل جهاز لمجرد إرسال رسالة إليه. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)
- [Service implementation](../ros/course_basics/scripts/boolean_service.py)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Communication between components

**Syllabus reference:** `3.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Compare a String topic stream with a SetBool request/reply service. Repeated observations suit topics; acknowledged commands suit services. This first service is deliberately simulated. The embedded unit later returns board-confirmed output state.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model. This reading item includes a demonstration; it does not add a syllabus assessment.

```bash
roslaunch course_basics communication.launch
```

```bash
# Another sourced terminal
rostopic type /course/chatter
rosservice type /course/set_demo
rosservice call /course/set_demo "data: true"
rostopic echo -n 1 /course/demo_state
rosservice call /course/set_demo "data: false"
```

## Expected result and validation

The service succeeds and its published state changes. Inspect the topic and service types.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Explain why sending a command alone is insufficient evidence of device actuation. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)
- [Service implementation](../ros/course_basics/scripts/boolean_service.py)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
