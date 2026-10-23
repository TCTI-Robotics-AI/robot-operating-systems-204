<div dir="rtl" lang="ar">

# تصميم المستودع

يمثل المستودع المقرر كاملًا. تتدرج المادة من الوحدة إلى البند التفصيلي ثم خطوات التجربة. رقم البند في الخطة هو مرجع الربط، بينما يظل عدد التقييمات الأسبوعية مستقلًا عن عدد التمارين.

| المستوى | موضعه | دوره |
| --- | --- | --- |
| المقرر | [الخريطة](../course/syllabus-map.md) و[الفهرس](../course/exercises-index.md) | تغطية المنهج وربط البنود بالمجلدات |
| الوحدة | [الوحدات الست](../labs/README.md) | تجميع الموضوعات المتصلة |
| البند أو التمرين | مجلد داخل الوحدة | الشرح والكود والإعدادات والتوصيلات ونتائج التنفيذ |
| التوسعة | [التطبيقات الإضافية](../extensions/README.md) | بناء تطبيقات فوق تمارين المقرر |
| البيئة | [دليل الأنظمة](../environments/README.md) | فروق الجهازين والإصدارات |
| الأجهزة والتحقق | [القطع](../hardware/README.md) و[النتائج](../validation/README.md) | المكونات الفعلية والأدلة على التوافق |

## الأنظمة المدمجة

أربعة تمارين ربط مستقلة: أردوينو، ومتحكمات <span dir="ltr">STM32</span>، والرازبيري، و<span dir="ltr">Odroid</span>. توزع تمارين الربط الأربعة على الأسابيع 14 و15 و16.

كود اللمبة الافتراضية داخل تمرين الرازبيري، ويثبت فهم الأوامر النصية فقط. التطبيق التجميعي للتحكم المنزلي بالصوت داخل التوسعات، ويعتمد على تمرين الصوت وتمرين الرازبيري بعد تنفيذهما.

يوثق كل تمرين دور <span dir="ltr">ROS</span> وإصداره وطريقة البناء. عند استخدام الرازبيري مضيفًا للوحة أخرى يسجل المضيف واللوحة المتصلة كل على حدة. لا تفترض قابلية نقل مكتبة أطراف أو إعداد صوت بين الجهازين دون اختبار.

</div>

<div dir="ltr" lang="en">

# Repository architecture

The hierarchy is course, unit, detailed syllabus item, then procedure. Syllabus references identify coverage; weekly assessment counts remain distinct from exercise counts. The table links course coverage, six units, individual labs, extensions, board environments, hardware and validation.

Embedded systems contains four distinct integration labs: Arduino, STM32, Raspberry Pi and Odroid across three weeks. The simulated lamp source belongs to the Pi lab and proves text interpretation only. Integrated voice home automation belongs to extensions and depends on implemented speech and Pi labs.

Each lab documents its ROS role, version and build method. When a Pi hosts another embedded board, record the host and connected device separately. Validate audio and GPIO settings per board rather than assuming interchangeability.

</div>
