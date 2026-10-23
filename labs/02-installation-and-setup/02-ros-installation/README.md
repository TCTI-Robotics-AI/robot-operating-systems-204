<div dir="rtl" lang="ar">

# المفاتيح وتثبيت <span dir="ltr">ROS</span>

**مرجع الخطة:** <code dir="ltr">4.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

بعد إضافة المصدر تثبت الحزم الثنائية المناسبة للمعمارية. تتضمن القائمة <span dir="ltr">ROS</span> وأدوات العرض ومحاكاة الحركة والتحكم بالذراع. يتطلب التطبيق حسابا يستطيع استخدام <span dir="ltr">sudo</span> وشبكة عاملة. راجع أخطاء <span dir="ltr">APT</span> الفعلية؛ لا تعتبر وجود نظام <span dir="ltr">Ubuntu</span> دليلا على تثبيت <span dir="ltr">ROS.</span>

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
bash labs/02-installation-and-setup/02-ros-installation/install-noetic.sh
# Apply only on Ubuntu 20.04:
bash labs/02-installation-and-setup/02-ros-installation/install-noetic.sh --apply
source /opt/ros/noetic/setup.bash
rosversion -d
gazebo --version
```

</div>

## النتيجة المتوقعة والتحقق

يعرض <span dir="ltr">ROS</span> توزيعة <span dir="ltr">noetic</span>، ويعرض <span dir="ltr">Gazebo</span> الإصدار <span dir="ltr">11.</span> إذا تعذر الحصول على حزمة من البيئة القديمة فسجل اسمها والخطأ.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

ميز بين تنزيل الحزمة وتثبيتها وتحميل بيئتها، ثم أثبت إصدار الأدوات. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Package installation helper](install-noetic.sh)
- [Official Noetic installation](https://wiki.ros.org/noetic/Installation/Ubuntu)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Keys and ROS installation

**Syllabus reference:** `4.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

After configuring the signed repository, install architecture-matched binary packages for ROS, visualization, simulation and arm control. Applying requires sudo access and network connectivity. Inspect actual APT results rather than assuming ROS is installed because Ubuntu boots.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
bash labs/02-installation-and-setup/02-ros-installation/install-noetic.sh
# Apply only on Ubuntu 20.04:
bash labs/02-installation-and-setup/02-ros-installation/install-noetic.sh --apply
source /opt/ros/noetic/setup.bash
rosversion -d
gazebo --version
```

## Expected result and validation

ROS reports noetic and Gazebo reports version 11. Record any unavailable legacy package and its actual error.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Distinguish downloading, installing and sourcing a package, and demonstrate tool versions. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Package installation helper](install-noetic.sh)
- [Official Noetic installation](https://wiki.ros.org/noetic/Installation/Ubuntu)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
