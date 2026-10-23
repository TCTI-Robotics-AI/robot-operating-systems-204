<div dir="rtl" lang="ar">

# مستوى نظام الملفات

**مرجع الخطة:** <code dir="ltr">2.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

تحتوي الحزمة ملف <span dir="ltr">package.xml</span> للاعتماديات و<span dir="ltr">CMakeLists.txt</span> للبناء. يجمع مجلد <span dir="ltr">src</span> المصادر، و<span dir="ltr">launch</span> التشغيل، و<span dir="ltr">urdf</span> وصف الروبوت. منطقة <span dir="ltr">Catkin</span> منفصلة عن المستودع: تربط أداة المشروع الحزم بها دون نسخها أو استبدال حزم موجودة. يقرأ <span dir="ltr">rospack</span> المسارات المحملة في الطرفية.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر. هذا بند قراءة مع تجربة توضيحية؛ لا يضيف تقييما عمليا إلى الخطة.

<div dir="ltr">

```bash
source ~/course204_ws/devel/setup.bash
rospack find course_basics
roscd course_basics
ls
cat package.xml
```

</div>

## النتيجة المتوقعة والتحقق

تنتقل إلى الحزمة داخل مصادر المقرر وتتعرف على ملف البناء وملف التعريف، دون تعديل ملفات <span dir="ltr">ROS</span> المثبتة.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

حدد أين تضيف ملف تشغيل جديدا وأين تصرح عن اعتماديته، واشرح الفرق بين المستودع ومنطقة العمل. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)
- [Package source](../ros/course_basics/)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# ROS filesystem level

**Syllabus reference:** `2.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

A package declares dependencies in package.xml and build rules in CMakeLists.txt. Scripts, launch files and models live in separate directories. The workspace helper links packages into a dedicated Catkin workspace and refuses conflicting entries. rospack discovers packages from the sourced environment.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model. This reading item includes a demonstration; it does not add a syllabus assessment.

```bash
source ~/course204_ws/devel/setup.bash
rospack find course_basics
roscd course_basics
ls
cat package.xml
```

## Expected result and validation

Locate the course source package and identify its manifest and build file without changing the installed ROS tree.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Identify where a launch file and its dependency belong, and explain repository versus workspace. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [ROS concepts and tutorials](https://wiki.ros.org/ROS/Tutorials)
- [Package source](../ros/course_basics/)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
