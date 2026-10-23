# تنظيم مستودع المقرر

المستودع حاوية المقرر كاملة. التمرين وحدة مستقلة لها هدف ومجلد وشرح وكود وإعدادات وتحقق. تكامل عدة تمارين يوثق كتمرين إضافي له متطلبات سابقة واضحة.

- `labs/`: مرجع التمارين؛ يوضع الشرح والكود وحزم ROS والمحاكاة التابعة لتمرين معه.
- `environments/`: بيئات الأجهزة والأنظمة المشتركة.
- `hardware/`: قائمة القطع المشتركة. التوصيل المحدد وأرقام الأطراف داخل التمرين.
- `validation/`: نتائج التوافق وسجلات التشغيل الفعلية.
- `docs/`: خريطة المنهج والقرارات والقالب والخطة.

يوضح كل تمرين إن كان ROS مطلوبًا أو اختياريًا أو غير مستخدم، مع الإصدار وطريقة البناء. تحفظ أمثلة Catkin منفصلة عن أي مسار ROS 2 مستقبلي.

## تطبيق التحكم المنزلي بالصوت

```text
الصوت → نص عربي → تفسير الأوامر → GPIO → نتيجة التنفيذ
                       ↑
                 إدخال نصي للتعلم
```

التطبيق التجميعي في `labs/11-voice-home-automation/`. الكود الحالي يطابق عبارات محددة ويعرض حالة افتراضية داخل تمرين GPIO. نتيجة منفذ الأمر تحدد نجاح التنفيذ الفعلي. الأمر غير المعروف لا يشغّل الجهاز.

## English

The repository contains the entire course. Each lab owns its objective, explanation, code, configuration, and validation. Integration across labs is a separate lab with prerequisites.

The labs directory owns lab source, ROS packages, and simulation assets. Environments owns shared board and OS profiles. Hardware lists common parts while precise wiring belongs to the lab. Validation records actual runs. Docs contains course decisions and templates.

Each lab states whether ROS is required, optional, or unused, including version and build steps. Keep Catkin examples distinct from future ROS 2 examples. The voice home automation lab will integrate speech, command interpretation, and GPIO. Only text phrase matching and simulated output exist today. Unknown input must not trigger switching; actual device results determine execution success.
