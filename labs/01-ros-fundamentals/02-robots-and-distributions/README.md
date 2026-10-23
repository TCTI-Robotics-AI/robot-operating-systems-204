<div dir="rtl" lang="ar">

# الروبوتات وتوزيعات <span dir="ltr">ROS</span>

**مرجع الخطة:** <code dir="ltr">1.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

الروبوت المتنقل يحتاج حركة وتموضعا، والذراع يحتاج مفاصل وتحكما، والروبوت الاجتماعي يحتاج إدراكا وحوارا. التوزيعة تجمع إصدارات متوافقة من الحزم. تطابق اسم النظام وحده لا يكفي: تحقق من إصدار <span dir="ltr">Ubuntu</span> ومعمارية المعالج وتوزيعة <span dir="ltr">ROS</span> والمكتبات المستخدمة. ملف التهيئة يسجل الواقع ولا يغير النظام.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر. هذا بند قراءة مع تجربة توضيحية؛ لا يضيف تقييما عمليا إلى الخطة.

<div dir="ltr">

```bash
python3 tools/diagnose.py
source /opt/ros/noetic/setup.bash
rosversion -d
uname -m
```

</div>

## النتيجة المتوقعة والتحقق

تحصل على تقرير النظام والمعمارية. قارن مسار الرازبيري الرابع مع الخامس في دليل البيئات، دون محاولة تثبيت النظام القديم مباشرة على الخامس.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

أنشئ جدول توافق لجهازك يميز الدعم الرسمي للنظام ونتيجة تشغيل التمرين. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)
- [Environment policy](../../../docs/environments.md)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Robots and ROS distributions

**Syllabus reference:** `1.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Mobile robots emphasize motion and localization, arms emphasize joints, and social robots add perception and dialogue. A ROS distribution groups compatible package releases. Compatibility includes OS version, CPU architecture, ROS release and device libraries; an OS name alone is insufficient.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model. This reading item includes a demonstration; it does not add a syllabus assessment.

```bash
python3 tools/diagnose.py
source /opt/ros/noetic/setup.bash
rosversion -d
uname -m
```

## Expected result and validation

Inspect OS and architecture and compare the two Pi paths. Do not apply native Focal installation instructions to Pi 5.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Create a compatibility table separating OS support from observed lab behavior. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)
- [Environment policy](../../../docs/environments.md)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
