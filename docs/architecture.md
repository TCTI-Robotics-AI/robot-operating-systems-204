<div dir="rtl" lang="ar">

# تنظيم مستودع المقرر

المستودع حاوية المقرر كاملة. التمرين وحدة مستقلة لها هدف ومجلد وشرح وكود وإعدادات وتحقق. تكامل عدة تمارين يوثق كتمرين إضافي له متطلبات سابقة واضحة.

- <code dir="ltr">labs/</code>: مرجع التمارين؛ يوضع الشرح والكود وحزم <span dir="ltr">ROS</span> والمحاكاة التابعة لتمرين معه.
- <code dir="ltr">environments/</code>: بيئات الأجهزة والأنظمة المشتركة.
- <code dir="ltr">hardware/</code>: قائمة القطع المشتركة. التوصيل المحدد وأرقام الأطراف داخل التمرين.
- <code dir="ltr">validation/</code>: نتائج التوافق وسجلات التشغيل الفعلية.
- <code dir="ltr">docs/</code>: خريطة المنهج والقرارات والقالب والخطة.

يوضح كل تمرين إن كان <span dir="ltr">ROS</span> مطلوبًا أو اختياريًا أو غير مستخدم، مع الإصدار وطريقة البناء. تحفظ أمثلة <span dir="ltr">Catkin</span> منفصلة عن أي مسار <span dir="ltr">ROS 2</span> مستقبلي.

## تطبيق التحكم المنزلي بالصوت

<div dir="ltr">

```text
الصوت → نص عربي → تفسير الأوامر → GPIO → نتيجة التنفيذ
                       ↑
                 إدخال نصي للتعلم
```

</div>

التطبيق التجميعي في <code dir="ltr">labs/11-voice-home-automation/</code>. الكود الحالي يطابق عبارات محددة ويعرض حالة افتراضية داخل تمرين <span dir="ltr">GPIO</span>. نتيجة منفذ الأمر تحدد نجاح التنفيذ الفعلي. الأمر غير المعروف لا يشغّل الجهاز.

</div>

<div dir="ltr" lang="en">

## English

The repository contains the entire course. Each lab owns its objective, explanation, code, configuration, and validation. Integration across labs is a separate lab with prerequisites.

The labs directory owns lab source, ROS packages, and simulation assets. Environments owns shared board and OS profiles. Hardware lists common parts while precise wiring belongs to the lab. Validation records actual runs. Docs contains course decisions and templates.

Each lab states whether ROS is required, optional, or unused, including version and build steps. Keep Catkin examples distinct from future ROS 2 examples. The voice home automation lab will integrate speech, command interpretation, and GPIO. Only text phrase matching and simulated output exist today. Unknown input must not trigger switching; actual device results determine execution success.

</div>
