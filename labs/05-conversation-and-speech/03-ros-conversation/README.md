<div dir="rtl" lang="ar">

# روبوت المحادثة داخل <span dir="ltr">ROS</span>

**مرجع الخطة:** <code dir="ltr">12.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

تعرض <span dir="ltr">talk_server</span> خدمة <span dir="ltr">Talk</span> مخصصة تستقبل نصا وتعيد ردا ونية. يتعامل العميل مع بنية الخدمة المولدة بواسطة <span dir="ltr">Catkin.</span> تشغيل <span dir="ltr">launch</span> يبدأ الخادم وعقدة التفاعل مع المواضيع، ويظل تنفيذ الأجهزة معطلا افتراضيا حتى يفعله المشغل صراحة.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
roslaunch course_conversation conversation.launch
```

</div>

<div dir="ltr">

```bash
# Another sourced terminal
rosrun course_conversation talk_client.py --text "مرحبا"
rosrun course_conversation talk_client.py --text "شغل اللمبة"
rossrv show course_common/Talk
```

</div>

## النتيجة المتوقعة والتحقق

يرجع الخادم <span dir="ltr">reply</span> و<span dir="ltr">intent</span> دون ادعاء تشغيل جهاز. لا حاجة للإنترنت بعد تثبيت المفسر.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

أضف نمطا واختبره من عميل <span dir="ltr">ROS</span>، ثم اشرح لماذا لا يعني <span dir="ltr">intent=on</span> أن اللمبة اشتغلت. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Course conversation package](../ros/course_conversation/)
- [Python AIML interpreter](https://github.com/paulovn/python-aiml)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# AIML conversation inside ROS

**Syllabus reference:** `12.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

talk_server exposes the generated Talk service, accepting text and returning reply/intent. The launch starts both server and topic interaction. Device execution defaults to disabled and must be explicitly enabled.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
roslaunch course_conversation conversation.launch
```

```bash
# Another sourced terminal
rosrun course_conversation talk_client.py --text "مرحبا"
rosrun course_conversation talk_client.py --text "شغل اللمبة"
rossrv show course_common/Talk
```

## Expected result and validation

The server returns reply and intent without claiming device actuation. Matching works offline after installing dependencies.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Add a pattern and test it via ROS; explain why intent=on is not proof of lamp actuation. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Course conversation package](../ros/course_conversation/)
- [Python AIML interpreter](https://github.com/paulovn/python-aiml)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
