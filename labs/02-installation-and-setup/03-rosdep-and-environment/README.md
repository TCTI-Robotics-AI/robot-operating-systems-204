<div dir="rtl" lang="ar">

# تهيئة الاعتماديات والبيئة

**مرجع الخطة:** <code dir="ltr">5.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يحول <span dir="ltr">rosdep</span> أسماء اعتماديات <span dir="ltr">ROS</span> إلى حزم النظام. لا يبني المشروع بنفسه، ولا يغني عن مكتبات <span dir="ltr">Python</span> المثبتة وفق دليل البدء. يهيئ السكربت قاعدة <span dir="ltr">rosdep</span> مرة واحدة ويحدث بيانات <span dir="ltr">Noetic</span> بما يشمل التوزيعات المنتهية، ثم يحل اعتماديات منطقة العمل عند تمرير مسارها.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
source /opt/ros/noetic/setup.bash
bash labs/02-installation-and-setup/03-rosdep-and-environment/initialize.sh
python3 tools/workspace.py --workspace ~/course204_ws
bash labs/02-installation-and-setup/03-rosdep-and-environment/initialize.sh ~/course204_ws
printenv ROS_DISTRO
```

</div>

## النتيجة المتوقعة والتحقق

تظهر بيانات <span dir="ltr">Noetic</span>، وتصبح الاعتماديات قابلة للحل. لا تتجاهل اعتماديات مجهولة؛ صحح الاسم أو وثق بديله.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

افتح طرفية جديدة دون تحميل البيئة، ثم قارن نتيجة الفحص قبل التحميل وبعده. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Initialization helper](initialize.sh)
- [rosdep documentation](https://docs.ros.org/en/independent/api/rosdep/html/)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# rosdep and environment initialization

**Syllabus reference:** `5.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

rosdep maps ROS dependency keys to system packages; it does not build the project or replace Python dependency installation. The script initializes rosdep if needed, updates Noetic including end-of-life distributions, then installs workspace dependencies when a path is supplied.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
source /opt/ros/noetic/setup.bash
bash labs/02-installation-and-setup/03-rosdep-and-environment/initialize.sh
python3 tools/workspace.py --workspace ~/course204_ws
bash labs/02-installation-and-setup/03-rosdep-and-environment/initialize.sh ~/course204_ws
printenv ROS_DISTRO
```

## Expected result and validation

Noetic environment variables are set and dependencies resolve. Investigate unknown keys instead of silently skipping them.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Compare a fresh terminal before and after sourcing ROS. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Initialization helper](initialize.sh)
- [rosdep documentation](https://docs.ros.org/en/independent/api/rosdep/html/)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
