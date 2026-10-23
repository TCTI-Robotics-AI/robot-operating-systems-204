<div dir="rtl" lang="ar">

# الربط بين <span dir="ltr">ROS</span> و<span dir="ltr">STM32</span>

**مرجع الخطة:** <code dir="ltr">14.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

هدف البند ربط <span dir="ltr">ROS</span> بالمتحكم، واللمبة اختبار للفعل والرد. نوفر مسارين: <span dir="ltr">NUCLEO-F446RE</span> عبر منفذ <span dir="ltr">ST-LINK</span> التسلسلي، و<span dir="ltr">B-L475E-IOT01A</span> عبر وحدة الواي فاي المدمجة. لا تحتوي <span dir="ltr">F446RE</span> واي فاي. كلاهما يستخدم <span dir="ltr">LED</span> المدمج وبروتوكول الطلب والتأكيد نفسه. يعمل <span dir="ltr">ROS 1 Noetic</span> على الرازبيري أو الحاسب، وتنفذ اللوحة البرنامج الثابت؛ لا نخلط هذا مع <span dir="ltr">micro-ROS</span> الخاص بمسار <span dir="ltr">ROS 2.</span>

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
# USB path: NUCLEO-F446RE, ST-LINK data cable
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/02-stm32/firmware
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/02-stm32/firmware -t upload
ls -l /dev/serial/by-id/
roslaunch course_devices lamp.launch backend:=serial port:=/dev/ttyACM0
```

</div>

<div dir="ltr">

```bash
# Alternative Wi-Fi path: B-L475E-IOT01A only; stop the USB launch first
cp labs/06-embedded-systems/02-stm32/wifi-firmware/src/secrets.example.h labs/06-embedded-systems/02-stm32/wifi-firmware/src/secrets.h
# Edit secrets.h locally with a private lab SSID/password; it is ignored by Git
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/02-stm32/wifi-firmware
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/02-stm32/wifi-firmware -t upload
# Read the board IP from its 115200-baud USB monitor, then close the monitor
# Replace the sample IP with the board's actual lab-network IP
roslaunch course_devices lamp.launch backend:=wifi host:=192.168.1.50 network_port:=8766
```

</div>

<div dir="ltr">

```bash
# Another sourced terminal, for either transport
rosservice call /lamp/set "on: true"
rostopic echo -n 1 /lamp/state
rosservice call /lamp/set "on: false"
```

</div>

## النتيجة المتوقعة والتحقق

على <span dir="ltr">F446RE</span> يرتبط <span dir="ltr">USART2: PA3</span> للاستقبال و<span dir="ltr">PA2</span> للإرسال افتراضيا بجسر <span dir="ltr">ST-LINK</span> على لوحة <span dir="ltr">MB1136</span>؛ لا توصلها مباشرة بمنطق <span dir="ltr">5</span> فولت. تحقق من إصدار اللوحة والجسور وفق دليلها. مسار الواي فاي يحتاج شبكة مختبر خاصة تسمح بتواصل الأجهزة ومنفذ <span dir="ltr">TCP 8766</span>؛ البروتوكول تعليمي بلا مصادقة فلا تعرضه للإنترنت. وصول الرد داخل <span dir="ltr">ROS</span> هو دليل الربط، أما اختبار الراديو واللوحتين فعليا فما زال مطلوبا.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

اختر مسارا واحدا وسجل الطلب ورد اللوحة والموضوع المنشور داخل <span dir="ltr">ROS.</span> افصل وسيلة الاتصال واختبر الفشل. قارن الاتصالين دون افتراض أن نجاح التجميع يعني نجاح الواي فاي. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [USB firmware](firmware/)
- [Wi-Fi firmware](wifi-firmware/)
- [ROS bridge](../ros/course_devices/)
- [NUCLEO-F446RE](https://www.st.com/en/evaluation-tools/nucleo-f446re.html)
- [Wi-Fi board datasheet](https://www.st.com/resource/en/data_brief/b-l475e-iot01a.pdf)
- [Wi-Fi driver](https://github.com/stm32duino/WiFi-ISM43362-M3G-L44)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# ROS and STM32 integration

**Syllabus reference:** `14.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

The syllabus objective is ROS-to-STM32 integration; the LED tests command and feedback. Two implementations are provided: NUCLEO-F446RE over ST-LINK virtual serial, and B-L475E-IOT01A over its onboard Wi-Fi module. F446RE has no onboard Wi-Fi. Both use the onboard LED and the same sequence-checked protocol. Noetic runs on the host, firmware on the MCU; this is distinct from a ROS 2 micro-ROS setup.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
# USB path: NUCLEO-F446RE, ST-LINK data cable
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/02-stm32/firmware
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/02-stm32/firmware -t upload
ls -l /dev/serial/by-id/
roslaunch course_devices lamp.launch backend:=serial port:=/dev/ttyACM0
```

```bash
# Alternative Wi-Fi path: B-L475E-IOT01A only; stop the USB launch first
cp labs/06-embedded-systems/02-stm32/wifi-firmware/src/secrets.example.h labs/06-embedded-systems/02-stm32/wifi-firmware/src/secrets.h
# Edit secrets.h locally with a private lab SSID/password; it is ignored by Git
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/02-stm32/wifi-firmware
.venv-tools/bin/python -m platformio run -d labs/06-embedded-systems/02-stm32/wifi-firmware -t upload
# Read the board IP from its 115200-baud USB monitor, then close the monitor
# Replace the sample IP with the board's actual lab-network IP
roslaunch course_devices lamp.launch backend:=wifi host:=192.168.1.50 network_port:=8766
```

```bash
# Another sourced terminal, for either transport
rosservice call /lamp/set "on: true"
rostopic echo -n 1 /lamp/state
rosservice call /lamp/set "on: false"
```

## Expected result and validation

On the reference F446RE MB1136, USART2 PA3 RX/PA2 TX routes to ST-LINK by default; do not connect 5 V logic directly. Check revision/jumpers in the manual. Wi-Fi needs a private lab network with client-to-client TCP 8766 connectivity. This teaching protocol has no authentication and must not be exposed publicly. ROS acknowledgement demonstrates the integration; real board/radio validation remains required.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Choose one path and record request, board acknowledgement and ROS topic. Disconnect transport to test failure. Compare both paths without treating compilation as a radio test. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [USB firmware](firmware/)
- [Wi-Fi firmware](wifi-firmware/)
- [ROS bridge](../ros/course_devices/)
- [NUCLEO-F446RE](https://www.st.com/en/evaluation-tools/nucleo-f446re.html)
- [Wi-Fi board datasheet](https://www.st.com/resource/en/data_brief/b-l475e-iot01a.pdf)
- [Wi-Fi driver](https://github.com/stm32duino/WiFi-ISM43362-M3G-L44)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
