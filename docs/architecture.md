# تصميم المشروع

الهدف فصل فهم الأوامر عن مصدرها وعن طريقة تنفيذها، حتى نستطيع شرح كل جزء وتجربته ثم ربط الأجزاء تدريجيًا.

## مسار الطلب المستهدف

```text
مايك → تحويل الكلام إلى نص → فهم الأمر → تنفيذ على الجهاز → نتيجة ورد
                            ↑
                  إدخال نصي للتجربة
```

التجربة الحالية تنفذ الإدخال النصي وفهم أوامر محددة وعرض نتيجة افتراضية فقط. لا تستخدم نموذج ذكاء اصطناعي.

## حدود الأجزاء

- الصوت: استقبال التسجيل وتحويله إلى نص، مع توثيق اللغة والنموذج والتكلفة والاتصال عند اختيار التقنية.
- الأوامر: تحويل العبارات المدعومة إلى طلب تشغيل أو إطفاء واضح. العبارة غير المعروفة لا تنفذ أمرًا.
- الأجهزة: تنفيذ الطلب باستخدام برنامج افتراضي أو موصل GPIO مناسب للجهاز، بعد تحديد التوصيلات.
- ROS: ربط الأجزاء بعقد ورسائل وخدمات في دروس ROS، مع بقاء منطق فهم الأوامر قابلًا للتجربة مستقلًا.
- الرد: بيان نجاح التنفيذ أو فشله؛ لا يُعلن نجاح التحكم الفعلي قبل استلام نتيجته.
- التكاملات: مصادر إضافية للطلبات مثل WhatsApp، وتظل منفصلة عن أساس المشروع.

## معايير المرحلة

لكل جزء واجهة موثقة، وتجربة مستقلة، ومثال تشغيل، ونتيجة متوقعة. تختار المكتبات وإصداراتها عند تنفيذ المرحلة والتحقق من توافق بيئة المتدرب.

## English

The design separates command interpretation from input sources and device execution. This lets learners study and run each component independently before integration.

The target flow is microphone → speech to text → command interpretation → device execution → result and response. Text input provides an alternative entry point for development. Only text input, explicit command matching, and simulated output are implemented today; the demo does not use an AI model.

- Speech captures audio and produces text. The selected model, language support, connectivity, and cost will be documented in its lesson.
- Commands map supported phrases to explicit on or off requests. Unknown input must not trigger device actions.
- Device adapters will execute requests through simulation or a GPIO library validated for the board.
- ROS lessons will connect components using nodes, messages, and services, while keeping command logic independently runnable.
- Responses will report the execution result. Physical success must follow confirmation from the device adapter.
- Optional integrations, including WhatsApp, will supply additional request sources independently of the core.

Each implemented component needs an interface description, standalone example, expected result, and dependencies validated against the learner environment.
