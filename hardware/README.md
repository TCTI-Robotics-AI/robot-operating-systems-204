<div dir="rtl" lang="ar">

# الأجهزة والقطع والتوصيل

كل تمرين فعلي يجب أن يحدد القطع وعددها وموديلها وقيمها والتوصيل قبل اعتباره جاهزًا للمتدربين. هذه احتياجات مبدئية؛ القطع غير المجربة لا توصف بأنها معتمدة.

| الاستخدام | الاحتياج لكل محطة | الحالة |
| --- | --- | --- |
| تشغيل اللوحة | <span dir="ltr">Pi 4</span> أو <span dir="ltr">Pi 5</span> واحدة، مزود طاقة مناسب لموديلها، تخزين بالنظام، شبكة | تسجل الموديلات والسعة الفعلية |
| التجربة النصية | <span dir="ltr">Python 3.8</span> أو أحدث على حاسب أو لوحة | لا تحتاج قطعًا إضافية |
| الصوت العربي | مايك متوافق واحد؛ مخرج صوت وسماعة للرد المسموع | الموديلات والتعريف ومعدل التسجيل لم تحدد |
| <span dir="ltr">LED</span> | لوحة تجارب، <span dir="ltr">LED</span> واحدة، مقاومة مناسبة واحدة، أسلاك | المقاومة وأطراف <span dir="ltr">GPIO</span> لم تعتمد |
| <span dir="ltr">Arduino</span> و<span dir="ltr">STM32</span> | اللوحة المقصودة وكابل بيانات مناسب | الموديلات والبروتوكول لم تحدد |
| <span dir="ltr">Odroid</span> | اللوحة ومزود الطاقة وكابل الربط | يحدد في درس الربط |
| المحاكاة | جهاز يناسب المحاكاة المختارة | متطلبات الأداء تقاس عند التنفيذ |
| <span dir="ltr">WhatsApp</span> والنموذج اللغوي | حساب وخدمة واتصال حسب المزود | المزود لم يعتمد؛ لا يحتاج <span dir="ltr">GPIO</span> بحد ذاته |

## بيانات كل جهاز

سجل موديل <span dir="ltr">Pi</span> والرام والنظام والنواة، ومواصفات مزود الطاقة والتخزين والتبريد، وموديل كل جهاز صوت وواجهته. لا تفترض أن مزود الطاقة أو مكتبة <span dir="ltr">GPIO</span> يتبادلان بين اللوحتين دون تحقق.

لكل توصيل سجل الإشارة ورقم <span dir="ltr">BCM</span> والطرف الفيزيائي والأرضي والجهد وقيم المقاومة والمكونات الوسيطة ومخططًا واضحًا. لا تعطى أطراف تنفيذية قبل اعتماد الدائرة. يبدأ تمرين اللمبة بـ<span dir="ltr">LED</span> منخفضة الجهد؛ اللمبة المنزلية تحتاج درسًا وتجهيزات مستقلة.

أكمل [قالب القطع](inventory.example.json) واربط نسخته بسجل تشغيل التمرين. قيمة <span dir="ltr">null</span> تعني غير محدد.

</div>

<div dir="ltr" lang="en">

## English

Every physical lab must specify quantities, models, component values, and wiring before learner release. The list above is provisional, not validated product selection.

| Use | Requirements per station | Status |
| --- | --- | --- |
| Board | One Pi 4 or Pi 5, suitable PSU, OS storage, network | Record actual models and capacity |
| Text demo | Python 3.8 or newer on a computer or board | No extra parts |
| Speech | One compatible microphone; output device and speaker for spoken replies | Models, drivers, and sample rate pending |
| LED | Breadboard, one LED, one suitable resistor, wires | Resistance and GPIO pins pending |
| Arduino and STM32 | Selected board and data cable | Model and protocol pending |
| Odroid | Board, PSU, and link cable | Selected with its lab |
| Simulation | Computer suitable for selected simulator | Performance requirements to be measured |
| WhatsApp and model | Selected provider's account, service, connectivity | Provider pending; no inherent GPIO requirement |

Record model, RAM, OS, kernel, PSU, storage, cooling, and audio devices and interfaces. Do not assume PSU or GPIO library interchangeability. Wiring guides specify signal, BCM number, physical pin, ground, voltage, resistor and interface components, and a diagram. No pin assignment is selected yet. Start with a low voltage LED; mains lamps require a separately equipped lab. Complete the inventory JSON template and attach it to the run record; null means unselected.

</div>
