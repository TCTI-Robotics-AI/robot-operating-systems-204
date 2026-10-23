<div dir="rtl" lang="ar">

# إعداد مخازن <span dir="ltr">Ubuntu</span>

**مرجع الخطة:** <code dir="ltr">4.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

تقرأ <span dir="ltr">APT</span> قائمة مصادر الحزم ومفاتيحها. يستخدم سكربت المقرر مستودع <span dir="ltr">ROS</span> الرسمي ومفتاحا مخصصا عبر <span dir="ltr">signed-by</span>، ويقصر التثبيت المباشر على <span dir="ltr">Ubuntu 20.04.</span> راجع خطة التغييرات أولا؛ يبدأ السكربت بوضع المعاينة، ولا يعدل إعدادات النظام إلا عند إضافة --<span dir="ltr">apply.</span> مسار <span dir="ltr">Pi 5</span> هو الحاوية أو مضيف <span dir="ltr">ROS</span> منفصل.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
python3 tools/diagnose.py
bash labs/02-installation-and-setup/01-ubuntu-repositories/configure-apt.sh
# Only on the dedicated Ubuntu 20.04 course host:
bash labs/02-installation-and-setup/01-ubuntu-repositories/configure-apt.sh --apply
```

</div>

## النتيجة المتوقعة والتحقق

تعرض المعاينة ما سيضاف. بعد التطبيق تنجح قراءة مصدر <span dir="ltr">ROS</span> عند تحديث <span dir="ltr">APT.</span> هذه خطوة إعداد، ولا تختبر <span dir="ltr">GPIO</span> أو الميكروفون.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

اشرح وظيفة المفتاح و<span dir="ltr">signed-by</span>، واحفظ إصدار النظام ونتيجة تحديث المصادر. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Repository setup script](configure-apt.sh)
- [ROS Ubuntu installation](https://wiki.ros.org/noetic/Installation/Ubuntu)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Ubuntu repositories and sources

**Syllabus reference:** `4.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

APT uses configured repositories and signing keys. The helper uses the official ROS source with a dedicated signed-by key and guards native installation to Ubuntu 20.04. It defaults to a plan; --apply performs the changes. Pi 5 uses the container or a separate ROS host.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
python3 tools/diagnose.py
bash labs/02-installation-and-setup/01-ubuntu-repositories/configure-apt.sh
# Only on the dedicated Ubuntu 20.04 course host:
bash labs/02-installation-and-setup/01-ubuntu-repositories/configure-apt.sh --apply
```

## Expected result and validation

The plan explains repository changes. After applying, APT should read the ROS package source. This does not validate GPIO or audio.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Explain the signing key and signed-by restriction, then record OS version and repository update output. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Repository setup script](configure-apt.sh)
- [ROS Ubuntu installation](https://wiki.ros.org/noetic/Installation/Ubuntu)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
