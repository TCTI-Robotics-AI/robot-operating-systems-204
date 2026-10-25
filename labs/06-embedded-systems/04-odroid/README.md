<div dir="rtl" lang="ar">

# الربط بين <span dir="ltr">ROS</span> و<span dir="ltr">Odroid</span>

**مرجع الخطة:** <code dir="ltr">16.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

اللوحة المرجعية <span dir="ltr">ODROID-C4</span> مع نظام <span dir="ltr">Linux</span> متوافق مع إصدار اللوحة و<span dir="ltr">Python 3.8</span> أو أحدث و<span dir="ltr">SSH.</span> نربطها بمضيف <span dir="ltr">ROS</span> دون اشتراط تثبيت <span dir="ltr">Noetic</span> عليها. يعمل وكيل على <span dir="ltr">Odroid</span> ويعيد معلومات النظام مع حالة خرج افتراضي، ويصل مضيف <span dir="ltr">ROS</span> إليه عبر نفق <span dir="ltr">SSH.</span> هذا ربط شبكي للوحة فعلية عند تنفيذها، لكنه ليس تجربة <span dir="ltr">GPIO</span> حقيقي على <span dir="ltr">Odroid.</span>

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
# On Odroid, after cloning the repository
python3 -m venv .venv-agent
.venv-agent/bin/python -m pip install .
.venv-agent/bin/course204-agent --driver mock
```

</div>

<div dir="ltr">

```bash
# On the ROS host; replace both account and address with actual values
ssh -N -L 8765:127.0.0.1:8765 learner@ODROID_IP
```

</div>

<div dir="ltr">

```bash
# Another sourced ROS-host terminal
roslaunch course_devices lamp.launch backend:=network
```

</div>

<div dir="ltr">

```bash
# Another sourced ROS terminal
rosservice call /lamp/set true
rostopic echo -n 1 /device/status
rostopic echo -n 1 /lamp/simulated
rosservice call /lamp/set false
```

</div>

## النتيجة المتوقعة والتحقق

تظهر معمارية ونظام واسم جهاز <span dir="ltr">Odroid</span> من الوكيل ويكون <span dir="ltr">simulated=true.</span> أثناء الاختبار المحلي على الحاسب تظهر معلومات الحاسب؛ لا تسمها نتيجة <span dir="ltr">Odroid.</span> راجع عنوان <span dir="ltr">SSH</span> وجدار الحماية وتعارض المنفذ عند فشل الاتصال. اختر مزود الطاقة والتخزين وفق دليل إصدار اللوحة قبل الشراء.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

سجل معلومات <span dir="ltr">Odroid</span> المستقبلة داخل <span dir="ltr">ROS</span>، ثم أوقف النفق واختبر فشل الطلب. فسر الفرق بين الربط باللوحة والتحكم في أطرافها. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Agent](../../../shared/ros/course_common/src/course204/agent.py)
- [ROS bridge](../ros/course_devices/)
- [Hardkernel board documentation](https://wiki.odroid.com/odroid-c4/odroid-c4)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# ROS and Odroid integration

**Syllabus reference:** `16.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Reference board: ODROID-C4 with an appropriate vendor Linux image, Python 3.8+ and SSH. Noetic stays on the ROS host. The Odroid agent returns actual system metadata and a simulated output state over an SSH tunnel. A physical run demonstrates board networking, not real Odroid GPIO.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
# On Odroid, after cloning the repository
python3 -m venv .venv-agent
.venv-agent/bin/python -m pip install .
.venv-agent/bin/course204-agent --driver mock
```

```bash
# On the ROS host; replace both account and address with actual values
ssh -N -L 8765:127.0.0.1:8765 learner@ODROID_IP
```

```bash
# Another sourced ROS-host terminal
roslaunch course_devices lamp.launch backend:=network
```

```bash
# Another sourced ROS terminal
rosservice call /lamp/set true
rostopic echo -n 1 /device/status
rostopic echo -n 1 /lamp/simulated
rosservice call /lamp/set false
```

## Expected result and validation

The agent reports Odroid system/machine/hostname with simulated=true. A local desktop run reports desktop metadata and must not be labeled an Odroid test. Check SSH address, firewall and port conflicts. Choose PSU/storage from the exact board revision documentation.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Record board metadata received by ROS, stop the tunnel and test request failure. Explain network integration versus physical GPIO control. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Agent](../../../shared/ros/course_common/src/course204/agent.py)
- [ROS bridge](../ros/course_devices/)
- [Hardkernel board documentation](https://wiki.odroid.com/odroid-c4/odroid-c4)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
