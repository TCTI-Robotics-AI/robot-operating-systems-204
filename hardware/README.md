<div dir="rtl" lang="ar">

# القطع المرجعية والتوصيل

هذه اختيارات مرجعية لإعداد التمارين وليست قائمة مشتريات إلزامية. لم تختبر القطع فعليا في سجلات المشروع بعد. يمكن البدء بالمحاكاة دون شراء اللوحات. [تمارين الربط](../labs/06-embedded-systems/README.md) توضح البرنامج والتوصيل لكل مسار.

| التمرين | اللوحة والقطع | وسيلة ربط <span dir="ltr">ROS</span> | الملاحظة |
| --- | --- | --- | --- |
| <span dir="ltr">Arduino</span> | <span dir="ltr">UNO R3</span> بمعالج <span dir="ltr">ATmega328P</span> وكابل بيانات <span dir="ltr">USB-B</span> | جسر تسلسلي وتأكيد الطلب | يستخدم <span dir="ltr">LED</span> المدمج <span dir="ltr">D13</span> |
| <span dir="ltr">STM32</span> عبر <span dir="ltr">USB</span> | <span dir="ltr">NUCLEO-F446RE</span> وكابل بيانات مطابق لموصل <span dir="ltr">ST-LINK</span> في إصدار اللوحة | <span dir="ltr">USART2</span> عبر <span dir="ltr">ST-LINK VCP</span> | لا تحتوي واي فاي مدمجا |
| <span dir="ltr">STM32</span> لاسلكيا | <span dir="ltr">B-L475E-IOT01A</span> وكابل <span dir="ltr">ST-LINK</span> وشبكة مختبر خاصة | <span dir="ltr">TCP</span> عبر وحدة <span dir="ltr">Wi-Fi</span> المدمجة | بديل ضمن التمرين نفسه، لا يلزم شراء اللوحتين |
| <span dir="ltr">Raspberry Pi</span> | <span dir="ltr">Pi 4</span> أو <span dir="ltr">Pi 5</span>، طاقة وتخزين وتبريد مناسب للموديل، <span dir="ltr">LED</span> أحمر ومقاومة <span dir="ltr">330</span> أوم وربع واط ولوحة تجارب وثلاث وصلات | <span dir="ltr">GPIO</span> مباشر أو وكيل أصلي مرتبط بـ<span dir="ltr">ROS</span> | <span dir="ltr">BCM17</span> وطرف <span dir="ltr">GND</span> |
| <span dir="ltr">Odroid</span> | <span dir="ltr">ODROID-C4</span>، طاقة وتخزين معتمدان حسب دليل اللوحة، شبكة و<span dir="ltr">SSH</span> | وكيل محلي ونفق <span dir="ltr">SSH</span> | معلومات النظام حقيقية؛ الخرج افتراضي |
| الصوت | ميكروفون <span dir="ltr">USB</span> متوافق مع <span dir="ltr">Linux</span> وسماعة أو مخرج صوت متوافق | <span dir="ltr">Vosk</span> و<span dir="ltr">espeak-ng</span> | اختر الموديل بعد اختبار نظام الجهاز |

## توصيل <span dir="ltr">LED</span> إلى الرازبيري

افصل الطاقة. وصل الطرف الفيزيائي <span dir="ltr">11</span> أي <span dir="ltr">BCM17</span> إلى مقاومة <span dir="ltr">330</span> أوم، ثم إلى الرجل الطويلة الموجبة للمؤشر. وصل الرجل السالبة إلى الطرف الفيزيائي <span dir="ltr">6</span> أي <span dir="ltr">GND.</span> الجهد المنطقي <span dir="ltr">3.3</span> فولت؛ لا تضف <span dir="ltr">5</span> فولت إلى <span dir="ltr">GPIO.</span> تقدير التيار لمؤشر هبوطه <span dir="ltr">2</span> فولت هو نحو <span dir="ltr">4</span> ملي أمبير. راجع مواصفات المؤشر الحقيقي قبل التنفيذ. هذا التوصيل لمؤشر منخفض الجهد، وليس لمبة كهرباء منزلية.

لوحتا <span dir="ltr">Arduino</span> و<span dir="ltr">STM32</span> تستخدمان المؤشر المدمج في التجربة الأساسية، فلا توصل مؤشرا خارجيا دون إضافة مقاومته وتوثيق أطرافه. منافذ <span dir="ltr">STM32</span> ليست افتراضيا آمنة لكل جهد؛ راجع ورقة الموديل.

## وصف الإصدارات

سجل اسم اللوحة الكامل وإصدارها ومبرمجها وموصل الكابل وموديل مصدر الطاقة وجهده وتياره. في <span dir="ltr">JSON</span> تعني <span dir="ltr">null</span> أن القيمة غير مسجلة. [قالب الجرد](inventory.example.json) يبقى قالبا للتعبئة ولا يمثل إعدادا اكتشفه البرنامج تلقائيا.

المراجع: [Arduino UNO](https://docs.arduino.cc/hardware/uno-rev3/)، [STM32 F446RE](https://www.st.com/en/evaluation-tools/nucleo-f446re.html)، [لوحة Wi-Fi](https://www.st.com/resource/en/data_brief/b-l475e-iot01a.pdf)، [Odroid C4](https://wiki.odroid.com/odroid-c4/odroid-c4)، [أطراف Raspberry Pi](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio).

</div>

<div dir="ltr" lang="en">

# Reference hardware and wiring

These are lab reference choices, not mandatory purchases or claims of physical validation. Start with software simulation before buying boards. [Embedded lessons](../labs/06-embedded-systems/README.md) give per-board procedures.

| Exercise | Reference hardware | ROS link | Notes |
| --- | --- | --- | --- |
| Arduino | UNO R3 ATmega328P, USB-B data cable | Sequence-checked serial bridge | Onboard D13 LED |
| STM32 USB | NUCLEO-F446RE, data cable matching its ST-LINK connector revision | USART2 via ST-LINK VCP | No onboard Wi-Fi |
| STM32 Wi-Fi | B-L475E-IOT01A, ST-LINK cable, private lab network | Onboard Wi-Fi TCP bridge | Alternative within the same exercise; both boards are not required |
| Raspberry Pi | Pi 4 or 5; model-appropriate PSU/storage/cooling, red LED, 330-ohm quarter-watt resistor, breadboard and wires | Native GPIO or native agent to ROS | BCM17 and GND |
| Odroid | ODROID-C4 with vendor-appropriate PSU/storage/network and SSH | Agent over SSH tunnel | Actual system telemetry, mock output |
| Audio | Linux-compatible USB microphone and speaker/output | Vosk and optional espeak-ng | Verify exact device with the board OS |

With Pi power disconnected, wire physical pin 11 (BCM17) through 330 ohms to LED anode; cathode goes to pin 6 GND. Logic is 3.3 V, never 5 V into GPIO. A 2 V red LED draws approximately 4 mA; check the actual LED specification. This is a low-voltage indicator, not mains lighting. Arduino/STM32 use onboard indicators in the basic procedure. Any external wiring needs its own pin/voltage/resistor record.

Record full board model/revision, debugger, cable connector and PSU model/voltage/current. Null in the [inventory template](inventory.example.json) means unrecorded, not auto-detected. Sources are linked in the Arabic section above.

</div>
