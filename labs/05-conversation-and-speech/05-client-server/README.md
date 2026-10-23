<div dir="rtl" lang="ar">

# عقد العميل والخادم

**مرجع الخطة:** <code dir="ltr">13.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

ينتظر العميل خدمة المحادثة ثم يرسل طلبا واحدا. يستطيع خادمان وظيفيان مستقلان تقديم المحادثة والتحكم بالأجهزة. نربطهما عبر عقدة التفاعل لتبقى قواعد الحوار مستقلة عن السائق. نبدأ بسائق افتراضي، ثم نستبدله بسائق اللوحة في وحدة الأنظمة المدمجة.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
# Terminal 1
roslaunch course_devices lamp.launch backend:=mock
```

</div>

<div dir="ltr">

```bash
# Terminal 2
roslaunch course_conversation conversation.launch execute_lamp:=true
```

</div>

<div dir="ltr">

```bash
# Terminal 3
rostopic pub -1 /speech/text std_msgs/String "data: 'شغل اللمبة'"
rostopic echo -n 1 /lamp/state
rostopic echo -n 1 /lamp/simulated
rostopic pub -1 /speech/text std_msgs/String "data: 'طفي اللمبة'"
```

</div>

## النتيجة المتوقعة والتحقق

تتغير الحالة، ويكون <span dir="ltr">simulated=true</span> واضحا. عبارة غير معتمدة أو منفية لا تصل إلى أمر الجهاز.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

أوقف خادم الأجهزة واختبر الرسالة المعادة، ثم شغله مجددا وفسر الفرق بين الفهم والتنفيذ. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Course conversation package](../ros/course_conversation/)
- [Python AIML interpreter](https://github.com/paulovn/python-aiml)
- [Device server](../../06-embedded-systems/ros/course_devices/)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Client and server nodes

**Syllabus reference:** `13.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

The client waits for the dialogue service and sends one request. Separate servers implement dialogue and device control. The interaction node connects them while keeping conversational rules independent of drivers. Start with a mock driver, then substitute the board driver in the embedded unit.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
# Terminal 1
roslaunch course_devices lamp.launch backend:=mock
```

```bash
# Terminal 2
roslaunch course_conversation conversation.launch execute_lamp:=true
```

```bash
# Terminal 3
rostopic pub -1 /speech/text std_msgs/String "data: 'شغل اللمبة'"
rostopic echo -n 1 /lamp/state
rostopic echo -n 1 /lamp/simulated
rostopic pub -1 /speech/text std_msgs/String "data: 'طفي اللمبة'"
```

## Expected result and validation

State changes with simulated=true explicitly published. Unknown or negated phrases do not execute device commands.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Stop the device server, inspect the reply, restart it and distinguish understanding from execution. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Course conversation package](../ros/course_conversation/)
- [Python AIML interpreter](https://github.com/paulovn/python-aiml)
- [Device server](../../06-embedded-systems/ros/course_devices/)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
