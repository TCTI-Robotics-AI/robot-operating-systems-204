<div dir="rtl" lang="ar">

# منطقة <span dir="ltr">Catkin</span> وأداة <span dir="ltr">rosinstall</span>

**مرجع الخطة:** <code dir="ltr">5.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يعالج <span dir="ltr">Catkin</span> ترتيب بناء الحزم وتوليد الخدمات المخصصة. تنشئ أداة المشروع روابط للحزم الست داخل منطقة عمل مستقلة، وترفض استبدال مجلد موجود. أما <span dir="ltr">rosinstall</span> فيصف مستودعات مصادر متعددة؛ نعرض وظيفته دون تنزيل نسخة أخرى من <span dir="ltr">ROS</span>، لأن المقرر هنا مستودع واحد مع حزم متعددة.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
rosinstall --help
bash tools/build.sh ~/course204_ws
source ~/course204_ws/devel/setup.bash
rospack find course_common
rossrv show course_common/SetLamp
```

</div>

## النتيجة المتوقعة والتحقق

يبنى المشروع وتتولد خدمة تحمل طلب <span dir="ltr">on</span> وردا فيه <span dir="ltr">success</span> و<span dir="ltr">state</span> و<span dir="ltr">message.</span> بناء الكود لا يثبت تشغيل العتاد.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

اشرح مجلدات <span dir="ltr">src</span> و<span dir="ltr">build</span> و<span dir="ltr">devel</span>، وأعد بناء المشروع بعد تعديل وصف خدمة في نسخة تدريبية. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Workspace helper](../../../tools/workspace.py)
- [Catkin documentation](https://catkin-tools.readthedocs.io/en/latest/)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Catkin workspace and rosinstall

**Syllabus reference:** `5.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Catkin orders package builds and generates custom service bindings. The helper links six packages into a separate workspace and refuses conflicting directories. rosinstall describes multiple source repositories; this course already keeps its packages in one repository and does not need a duplicate ROS source checkout.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
rosinstall --help
bash tools/build.sh ~/course204_ws
source ~/course204_ws/devel/setup.bash
rospack find course_common
rossrv show course_common/SetLamp
```

## Expected result and validation

The build generates a service with on request and success/state/message response. Building source is not a physical device test.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Explain src/build/devel and rebuild a training copy after modifying a service definition. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Workspace helper](../../../tools/workspace.py)
- [Catkin documentation](https://catkin-tools.readthedocs.io/en/latest/)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
