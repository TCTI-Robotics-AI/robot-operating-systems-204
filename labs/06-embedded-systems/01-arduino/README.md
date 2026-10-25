<div dir="rtl" lang="ar">

# الربط بين <span dir="ltr">ROS</span> و<span dir="ltr">Arduino</span>

**مرجع الخطة:** <code dir="ltr">14.2</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

اللوحة المرجعية <span dir="ltr">Arduino UNO R3</span> بمعالج <span dir="ltr">ATmega328P</span> وكابل بيانات <span dir="ltr">USB-B.</span> نستخدم <span dir="ltr">LED</span> المدمج <span dir="ltr">D13</span> فلا نحتاج مقاومة أو أسلاك إضافية لهذا التمرين. تعمل عقدة <span dir="ltr">ROS</span> على المضيف، ويشغل المتحكم برنامجا ثابتا يستقبل <span dir="ltr">GET</span> و<span dir="ltr">SET</span> ويعيد <span dir="ltr">STATE</span> مع رقم الطلب. هذا جسر بروتوكول تعليمي مخصص، وليس مكتبة <span dir="ltr">rosserial.</span> نجاح الرد يثبت حالة خرج الدبوس، ولا يقيس إضاءة اللمبة بحساس ضوئي.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
# Use a dedicated tools venv for firmware compilation
python3 -m venv .venv-tools
.venv-tools/bin/python -m pip install platformio==6.1.18
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/01-arduino/firmware
# Connect the board; choose its actual device path
ls -l /dev/serial/by-id/
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/01-arduino/firmware -t upload --upload-port /dev/ttyACM0
roslaunch course_devices lamp.launch backend:=serial port:=/dev/ttyACM0
```

</div>

<div dir="ltr">

```bash
# Another sourced ROS terminal
rosservice call /lamp/set true
rostopic echo -n 1 /lamp/state
rostopic echo -n 1 /lamp/simulated
rosservice call /lamp/set false
```

</div>

## النتيجة المتوقعة والتحقق

تستجيب خدمة <span dir="ltr">ROS</span> بنجاح وحالة مطابقة، ويكون <span dir="ltr">simulated=false.</span> إذا كان المنفذ محجوزا أغلق شاشة <span dir="ltr">Serial Monitor.</span> أضف المستخدم إلى <span dir="ltr">dialout</span> ثم سجل الخروج والدخول إذا ظهرت مشكلة صلاحيات. يبدأ خرج اللوحة مطفأ؛ يحاول الخادم إطفاءه عند الإغلاق، لكن انقطاع الاتصال لا يضمن وصول أمر الإطفاء.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

شغل وأطفئ من <span dir="ltr">ROS</span>، ثم افصل <span dir="ltr">USB</span> وسجل الفشل بدل عرض نجاح وهمي. أرفق نسخة البرنامج وموديل اللوحة والمنفذ. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Firmware](firmware/)
- [Shared protocol](../../../shared/firmware/led_protocol.h)
- [ROS device bridge](../ros/course_devices/)
- [Arduino UNO R3](https://docs.arduino.cc/hardware/uno-rev3/)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# ROS and Arduino integration

**Syllabus reference:** `14.2` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Reference hardware: Arduino UNO R3 (ATmega328P), USB-B data cable and onboard D13 LED; no external wiring/resistor is required. ROS runs on the host. Firmware receives GET/SET and returns STATE with the request sequence. This is an explicit teaching protocol bridge, not rosserial. Acknowledgements confirm pin output, not optical illumination.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
# Use a dedicated tools venv for firmware compilation
python3 -m venv .venv-tools
.venv-tools/bin/python -m pip install platformio==6.1.18
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/01-arduino/firmware
# Connect the board; choose its actual device path
ls -l /dev/serial/by-id/
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/01-arduino/firmware -t upload --upload-port /dev/ttyACM0
roslaunch course_devices lamp.launch backend:=serial port:=/dev/ttyACM0
```

```bash
# Another sourced ROS terminal
rosservice call /lamp/set true
rostopic echo -n 1 /lamp/state
rostopic echo -n 1 /lamp/simulated
rosservice call /lamp/set false
```

## Expected result and validation

ROS should return success with matching state and simulated=false. Close competing serial monitors. For permissions, add your user to dialout and log out/in. Output starts off; server shutdown attempts off, but a broken connection cannot guarantee delivery.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Switch output through ROS, disconnect USB and record the reported failure. Submit firmware revision, board model and port. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Firmware](firmware/)
- [Shared protocol](../../../shared/firmware/led_protocol.h)
- [ROS device bridge](../ros/course_devices/)
- [Arduino UNO R3](https://docs.arduino.cc/hardware/uno-rev3/)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
