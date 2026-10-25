<div dir="rtl" lang="ar">

# أول تشغيل للمبة على الرازبيري 5

يتبع هذا الدليل البند <code dir="ltr">15.2</code> من المقرر. جميع الأوامر تنفذ على الرازبيري نفسه، ويمكن الوصول إليه من الكمبيوتر عبر <span dir="ltr">SSH</span>. لا تكتب كلمات المرور في ملفات المشروع أو سجلاته.

تجربة التجهيز الأولى تستخدم <span dir="ltr">Ubuntu 24.04 arm64</span> وحاوية خفيفة لحزمتي الاتصال والتحكم. يعمل وكيل الأطراف على النظام الأصلي. يبقى اختبار المؤشر الحقيقي منفصلا عن نجاح اختبار الخرج الافتراضي.

## 1. تجهيز البرامج

ثبت <span dir="ltr">Docker Engine</span> من [دليله الرسمي](https://docs.docker.com/engine/install/ubuntu/)، ثم اتبع [دليل الحاوية الخفيفة](../../../environments/noetic-device/README.md). استخدم الطرفية الأولى لتشغيل الوكيل الافتراضي، وطرفية ثانية لبناء الحاوية واختبار خدمة التشغيل والإطفاء.

يجب أن تكون قيمة <code dir="ltr">/lamp/simulated</code> صحيحة في هذه المرحلة. هذا يعني أن الاختبار افتراضي، ولا يدعي إضاءة قطعة حقيقية.

## القياس بالملتيميتر بدلا من المؤشر

يمكن تأجيل توصيل المؤشر وفحص خرج الطرف مباشرة. اضبط الملتيميتر على قياس الجهد المستمر، ووصل المجس الأسود بمدخل <span dir="ltr">COM</span> وبالطرف الفيزيائي 6 للأرضي، والمجس الأحمر بمدخل الجهد وبالطرف الفيزيائي 11 الذي يمثل <span dir="ltr">GPIO17</span>. تجنب ملامسة طرفين متجاورين بالمجس. لا تستخدم مدخل قياس التيار أو وضع المقاومة في هذا الفحص.

بعد تشغيل الوكيل الحقيقي، أرسل أمر التشغيل الوارد أدناه؛ القراءة المتوقعة قرابة 3.3 فولت. أرسل أمر الإطفاء؛ القراءة المتوقعة قرابة صفر فولت. لا تعد استجابة الخدمة أو قراءة حالة البرنامج قياسا فعليا للجهد. سجل القيم التي تراها على جهاز القياس.

الأوامر تستخدم القيمة المنطقية مباشرة، مثل <code dir="ltr">rosservice call /lamp/set true</code>. الصيغة التي تكتب اسم الحقل <code dir="ltr">on</code> دون اقتباس داخلي قد تفسره بعض أدوات <span dir="ltr">YAML</span> كقيمة منطقية وتفشل.

## 2. توصيل المؤشر

أوقف الحاوية والوكيل. أطفئ الرازبيري من النظام، وانتظر توقفه، ثم افصل الطاقة قبل التوصيل. القطع: مؤشر أحمر، ومقاومة <span dir="ltr">330</span> أوم وربع واط، ولوحة تجارب، وسلكا توصيل أنثى إلى ذكر.

<div dir="ltr">

```text
GPIO17 (physical pin 11) --> 330 ohm resistor --> LED anode (+)
GND    (physical pin 6)  ---------------------> LED cathode (-)
```

</div>

الموجب عادة الرجل الطويلة للمؤشر، والسالب الرجل القصيرة قرب الجانب المسطح. استخدم مخطط أطراف اللوحة للتحقق من رقم الطرف؛ رقم الطرف الفيزيائي ليس رقم <span dir="ltr">GPIO</span>. هذا مؤشر منخفض الجهد، وليس لمبة كهرباء منزلية.

## 3. تحديد متحكم الأطراف والصلاحيات

بعد إعادة التشغيل، افحص المتحكم الذي يحمل الاسم <code dir="ltr">pinctrl-rp1</code>. سجل التجهيز الأول وجد هذا المتحكم باسم <code dir="ltr">gpiochip4</code>؛ قد يختلف الرقم على نظام آخر.

<div dir="ltr">

```bash
sudo gpiodetect
ls -l /dev/gpiochip*
id
```

</div>

إذا كانت مجموعة الجهاز هي <code dir="ltr">dialout</code> ولم تكن عضوا فيها، أضف حسابك إليها ثم أعد تسجيل الدخول. لا تغير صلاحيات الجهاز إلى وصول عام.

<div dir="ltr">

```bash
sudo usermod -aG dialout "$USER"
```

</div>

## 4. تشغيل الوكيل الحقيقي وربطه بالخدمة

في الطرفية الأولى، وبعد التأكد من التوصيل ورقم المتحكم، شغل الوكيل. المثال يستخدم الرقم الذي ظهر في التجربة الأولى؛ عدله إذا تغير المتحكم عندك.

<div dir="ltr">

```bash
cd ~/robot-operating-systems-204
.venv-agent/bin/course204-agent --driver gpio --factory lgpio --chip 4 --bcm 17
```

</div>

في طرفية ثانية شغل حاوية الربط، ثم أرسل الطلبين وافحص الحالة:

<div dir="ltr">

```bash
sudo docker run --rm -d --name course204-lamp --network host -e ROS_IP=127.0.0.1 course204:device
sudo docker exec course204-lamp /course-entrypoint.sh rosservice call /lamp/set true
sudo docker exec course204-lamp /course-entrypoint.sh rostopic echo -n 1 /lamp/state
sudo docker exec course204-lamp /course-entrypoint.sh rostopic echo -n 1 /lamp/simulated
sudo docker exec course204-lamp /course-entrypoint.sh rosservice call /lamp/set false
```

</div>

انتظر بدء الخدمة قبل إرسال أول طلب، وراجع سجل الحاوية عند الخطأ. في هذا المسار يجب أن تكون قيمة المحاكاة غير صحيحة، وأن تلاحظ إضاءة المؤشر وإطفاءه فعليا. تأكيد حالة الخرج وحده لا يقيس الضوء؛ سجل ملاحظتك أيضا. لا تحدث سجل نجاح المؤشر قبل مشاهدته.

أوقف الحاوية بالأمر <code dir="ltr">sudo docker stop course204-lamp</code> ثم أوقف الوكيل في الطرفية الأولى. [سجل التحقق](../../../validation/README.md) يميز نتائج البرامج عن نتائج القطع.

</div>

<div dir="ltr" lang="en">

# First Pi 5 LED run

This is part of syllabus item 15.2. Run every command on the Pi, optionally through SSH; never store credentials in the repository. Use native Ubuntu 24.04 arm64 with the [two-package Noetic container](../../../environments/noetic-device/README.md). Start with its mock-agent test, then stop both bridge and agent.

Alternatively, measure voltage directly before connecting an LED. Use DC-voltage mode, black lead in COM at physical pin 6 (GND), and red lead in the voltage input at physical pin 11 (BCM17). Avoid bridging adjacent pins. Expect about 3.3 V on and 0 V off; record actual meter readings separately from software acknowledgement. Use positional boolean ROS arguments (`rosservice call /lamp/set true` or `false`) to avoid YAML interpreting the unquoted field name `on` as a boolean.

Shut down and disconnect Pi power before wiring physical pin 11 (BCM17) through 330 ohms to LED anode, and cathode to pin 6 GND. Use a low-voltage indicator, not mains lighting.

After boot, identify the `pinctrl-rp1` device with `sudo gpiodetect`. The first observed setup used gpiochip4; other kernels can number it differently. Check device ownership and your groups. If the device belongs to dialout, add the intended user to dialout and log in again. Do not grant world access.

The command blocks above show starting the confirmed native GPIO agent, starting the bridge, calling on/off and inspecting state/simulated topics. Wait for the service to start before calling it. A real GPIO backend reports simulated=false; actual LED illumination still requires observation. Stop the container before stopping the agent. Record physical evidence separately from software acknowledgement in the [validation guide](../../../validation/README.md).

</div>
