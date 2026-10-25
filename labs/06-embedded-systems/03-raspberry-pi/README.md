<div dir="rtl" lang="ar">

# الربط بين <span dir="ltr">ROS</span> و<span dir="ltr">Raspberry Pi</span>

**مرجع الخطة:** <code dir="ltr">15.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

نستهدف <span dir="ltr">Pi 4</span> و<span dir="ltr">Pi 5</span> في التمرين نفسه. يبدأ الاختبار بسائق افتراضي، ثم يستخدم <span dir="ltr">LED</span> خارجيا ومقاومة <span dir="ltr">330</span> أوم. التوصيل: الطرف الفيزيائي <span dir="ltr">11</span> أي <span dir="ltr">BCM17</span> إلى المقاومة ثم موجب <span dir="ltr">LED</span>، والسالب إلى <span dir="ltr">GND</span> بالطرف الفيزيائي <span dir="ltr">6.</span> افصل الطاقة عند التوصيل. لا توصل لمبة كهرباء منزلية أو جهد الشبكة إلى <span dir="ltr">GPIO.</span> تأكيد السائق يعني حالة الخرج ولا يقيس الضوء.

## المتطلبات والخطوات

للبداية على الرازبيري الخامس بذاكرة محدودة، استخدم [دليل أول تشغيل](pi5-first-run.md) و[حاوية ربط الأجهزة الخفيفة](../../../environments/noetic-device/README.md). يبني هذا المسار حزمتين فقط، ثم يفصل اختبار الربط الافتراضي عن اختبار المؤشر الحقيقي.

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
# Works without GPIO hardware, inside the sourced Noetic host/container
roslaunch course_devices lamp.launch backend:=mock
```

</div>

<div dir="ltr">

```bash
# Native Pi 4 / Ubuntu 20.04 hardware path; first install the GPIO driver
python3 -m pip install --user '.[gpio]' RPi.GPIO==0.7.1
roslaunch course_devices lamp.launch backend:=gpio factory:=rpigpio bcm:=17
```

</div>

<div dir="ltr">

```bash
# Pi 5 native Ubuntu 24.04 terminal (ROS runs separately)
sudo apt-get install python3-venv python3-lgpio gpiod
python3 -m venv --system-site-packages .venv-agent
.venv-agent/bin/python -m pip install '.[gpio]'
gpiodetect
# Example only: replace 0 with the gpiochip number for the Pi header controller
.venv-agent/bin/course204-agent --driver gpio --factory lgpio --chip 0 --bcm 17
```

</div>

<div dir="ltr">

```bash
# ROS host/container terminal on the same Pi 5, or through an SSH tunnel
roslaunch course_devices lamp.launch backend:=network
```

</div>

<div dir="ltr">

```bash
# Another ROS terminal
rosservice call /lamp/set true
rostopic echo -n 1 /lamp/state
rostopic echo -n 1 /lamp/simulated
rosservice call /lamp/set false
```

</div>

## النتيجة المتوقعة والتحقق

لا تشغل مساري <span dir="ltr">mock</span> و<span dir="ltr">gpio</span> معا. لا يستخدم <span dir="ltr">Pi 5</span> مكتبة <span dir="ltr">RPi.GPIO</span>؛ حدد متحكم <span dir="ltr">GPIO</span> الفعلي من <span dir="ltr">gpiodetect</span> وراجع صلاحياته. عند فصل مضيف <span dir="ltr">ROS</span> استخدم نفق <span dir="ltr">SSH</span> كما في تمرين <span dir="ltr">Odroid.</span> الحاوية تتصل بالوكيل الأصلي عبر الشبكة المحلية ولا تحتاج منحها وصولا واسعا للأجهزة. حالات <span dir="ltr">Pi</span> الفعلية غير مختبرة بعد.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

نفذ الافتراضي ثم الحقيقي عند توفر القطع، وسجل الجهاز والنظام ومتحكم <span dir="ltr">GPIO</span> والمقاومة. قارن <span dir="ltr">simulated</span> بين المسارين وأرفق صورة التوصيل. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Pi environment setup](../../../environments/README.md)
- [GPIO Zero pin factories](https://gpiozero.readthedocs.io/en/stable/api_pins.html)
- [Text preparation](01-text-lamp/README.md)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# ROS and Raspberry Pi integration

**Syllabus reference:** `15.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Both Pi 4 and Pi 5 use the same exercise. Start with a mock driver, then wire physical pin 11 (BCM17) through a 330-ohm resistor to LED anode, and cathode to physical pin 6 GND. Disconnect power while wiring. Never connect mains lighting to GPIO. Driver feedback confirms output state, not optical brightness.

## Requirements and procedure

For a low-memory Pi 5, use the [first-run guide](pi5-first-run.md) and [lightweight device container](../../../environments/noetic-device/README.md). This path builds only two packages and keeps the mock communication test separate from physical LED validation.

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
# Works without GPIO hardware, inside the sourced Noetic host/container
roslaunch course_devices lamp.launch backend:=mock
```

```bash
# Native Pi 4 / Ubuntu 20.04 hardware path; first install the GPIO driver
python3 -m pip install --user '.[gpio]' RPi.GPIO==0.7.1
roslaunch course_devices lamp.launch backend:=gpio factory:=rpigpio bcm:=17
```

```bash
# Pi 5 native Ubuntu 24.04 terminal (ROS runs separately)
sudo apt-get install python3-venv python3-lgpio gpiod
python3 -m venv --system-site-packages .venv-agent
.venv-agent/bin/python -m pip install '.[gpio]'
gpiodetect
# Example only: replace 0 with the gpiochip number for the Pi header controller
.venv-agent/bin/course204-agent --driver gpio --factory lgpio --chip 0 --bcm 17
```

```bash
# ROS host/container terminal on the same Pi 5, or through an SSH tunnel
roslaunch course_devices lamp.launch backend:=network
```

```bash
# Another ROS terminal
rosservice call /lamp/set true
rostopic echo -n 1 /lamp/state
rostopic echo -n 1 /lamp/simulated
rosservice call /lamp/set false
```

## Expected result and validation

Run one driver at a time. Pi 5 does not use RPi.GPIO; identify the actual header GPIO chip using gpiodetect and check permissions. A separate ROS host uses an SSH tunnel as in the Odroid lab. The container contacts the native loopback agent without broad device privileges. Both physical Pi paths are untested.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Run mock first, then physical GPIO when available. Record board/OS/GPIO chip/resistor, compare simulated flags and attach a wiring photo. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Pi environment setup](../../../environments/README.md)
- [GPIO Zero pin factories](https://gpiozero.readthedocs.io/en/stable/api_pins.html)
- [Text preparation](01-text-lamp/README.md)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
