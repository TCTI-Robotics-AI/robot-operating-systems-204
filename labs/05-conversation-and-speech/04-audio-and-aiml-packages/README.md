<div dir="rtl" lang="ar">

# حزم الصوت والمحادثة

**مرجع الخطة:** <code dir="ltr">12.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

تنشر عقدة التفاعل الرد النصي في /<span dir="ltr">conversation/reply.</span> يمكن تشغيل عقدة إخراج صوتي اختيارية تستدعي <span dir="ltr">espeak-ng</span> بصوت عربي إن كان مثبتا. فصل الصوت عن الخادم يسمح باختبار الحوار دون بطاقة صوت. لا ينشر المشروع تسجيلات المتدربين أو يرفعها لخدمة سحابية.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
espeak-ng --voices=ar
roslaunch course_conversation conversation.launch speaker:=true
```

</div>

<div dir="ltr">

```bash
# Another sourced terminal
rostopic pub -1 /speech/text std_msgs/String "data: 'مرحبا'"
rostopic echo -n 1 /conversation/reply
```

</div>

## النتيجة المتوقعة والتحقق

ينشر الرد نصيا، ويحاول المخرج قراءته إذا توفر الصوت العربي ومخرج صوت صالح. وصول النص لا يثبت أن صوتا خرج من السماعة.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

شغل الاختبار دون السماعة ثم معها، وسجل دليل الصوت منفصلا عن دليل وصول الرسالة. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Course conversation package](../ros/course_conversation/)
- [Python AIML interpreter](https://github.com/paulovn/python-aiml)
- [eSpeak NG](https://github.com/espeak-ng/espeak-ng)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Audio playback and AIML packages

**Syllabus reference:** `12.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Interaction publishes /conversation/reply. An optional node invokes local espeak-ng with the Arabic voice when available. Separating speech output from dialogue allows headless tests without an audio device. Learner recordings are not committed or uploaded.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
espeak-ng --voices=ar
roslaunch course_conversation conversation.launch speaker:=true
```

```bash
# Another sourced terminal
rostopic pub -1 /speech/text std_msgs/String "data: 'مرحبا'"
rostopic echo -n 1 /conversation/reply
```

## Expected result and validation

The text reply is published and playback is attempted if the voice and audio output exist. Topic delivery does not establish audible playback.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Test without and with an audio output and record playback evidence separately from message delivery. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Course conversation package](../ros/course_conversation/)
- [Python AIML interpreter](https://github.com/paulovn/python-aiml)
- [eSpeak NG](https://github.com/espeak-ng/espeak-ng)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
