<div dir="rtl" lang="ar">

# تطبيق التحكم المنزلي بالصوت

**الأسبوع:** تطبيق تجميعي · **الحالة:** مكتمل للنطاق المتفق عليه على <span dir="ltr">Pi 5</span> بتاريخ 25 أكتوبر 2026، باعتماد المستخدم. راجع [محضر الإكمال](completion.md).

## الهدف

دمج نداء «يا مساعد» والتقاط أمر مدته خمس ثوان وتحويله إلى نص، ثم إرساله إلى خدمة اللمبة في <span dir="ltr">ROS</span> والرد العربي عبر سماعة أبل بعد نجاح الخدمة. أضيف مسار [التاريخ وحرارة جدة](date-weather.md) مع توليد جواب عربي متغير محليا.

ابدأ من [الدليل العملي بالعربي والإنجليزي](pi5-voice-led.md). نجح تسجيلان جديدان بميكروفون <span dir="ltr">Apple EarPods USB-C</span> على <span dir="ltr">Ubuntu 24.04.5</span>؛ أكد المستخدم إضاءة المؤشر ثم إطفاءه. راجع [الإعدادات والنتائج والحدود](../../validation/runs/2026-10-24-pi5-earpods-voice-led.json).

أكد المستخدم لاحقا سماع «تم تشغيل اللمبة» و«تم إطفاء اللمبة» بوضوح عبر سماعة أبل بعد مشاهدة الحالتين. استعمل [اختبار الرد الصوتي](../../validation/runs/2026-10-24-pi5-earpods-spoken-replies.json) تسجيلات الأوامر السابقة.

نجح أيضا [اختبار النداء المباشر](../../validation/runs/2026-10-24-pi5-wake-assistant.json) مع رد «تفضل» ثم الأمر، وعرض النتائج على شاشة الرازبيري. حفظت [نقطة المتابعة](../../docs/session-checkpoint-2026-10-24.md) قبل توقف الجلسة بطلب المستخدم.

## المتطلبات والقطع

قطع تمارين الصوت و<span dir="ltr">GPIO</span> المعتمدة، مع مخطط توصيل خاص بالتطبيق.

**<span dir="ltr">ROS</span>:** يستخدم المسار المختبر حاوية <span dir="ltr">Noetic</span> لخدمة اللمبة ووكيل <span dir="ltr">GPIO</span> على النظام الأصلي.

## إعداد الجهازين

- **<span dir="ltr">Pi 4</span>:** راجع [مسار <span dir="ltr">Ubuntu 20.04</span>](../../environments/pi4-ubuntu2004/README.md). تحدد مكتبات هذا التمرين والتوصيل وأجهزة الصوت عند تنفيذه.
- **<span dir="ltr">Pi 5</span>:** راجع [مسار <span dir="ltr">Ubuntu 24.04</span> المقترح](../../environments/pi5-ubuntu2404/README.md). لا يفترض أن إعداد <span dir="ltr">Pi 4</span> صالح للجهاز الثاني.

سجل الاختبار الفعلي على <span dir="ltr">Pi 5</span> فقط. يظل <span dir="ltr">Pi 4</span> مسارا يحتاج التحقق، خصوصا إصدار <span dir="ltr">Python</span> واعتماديات التعرف. يتضمن الدليل القطع والتوصيل والكسب والأوامر؛ نجاح تجربتين لا يثبت دقة التعرف العامة.

</div>

<div dir="ltr" lang="en">

## English

**Course weeks:** Integration · **Status:** COMPLETE for the agreed Pi 5 scope, accepted by the user on 2026-10-25. See the [completion record](completion.md).

**Objective:** Wait for `يا مساعد`, speak the readiness prompt, capture a five-second Arabic command, send the exact command to the ROS service, and speak the matching acknowledgement after success. [Date and Jeddah temperature](date-weather.md) add locally generated dynamic Arabic answers. Use the [bilingual guide](pi5-voice-led.md), [wake validation](../../validation/runs/2026-10-24-pi5-wake-assistant.json), [fresh voice trials](../../validation/runs/2026-10-24-pi5-earpods-voice-led.json) and [spoken reply replay record](../../validation/runs/2026-10-24-pi5-earpods-spoken-replies.json). The user confirmed spoken replies and LED transitions. A [checkpoint](../../docs/session-checkpoint-2026-10-24.md) records the paused session and next work.

**Hardware:** Validated speech and GPIO lab hardware plus an integration wiring diagram.

**ROS:** The tested variant uses a Noetic service container and a native GPIO agent.

The observed run used Pi 5, Ubuntu 24.04.5 and Apple EarPods USB-C. The user confirmed both LED transitions. Pi 4 remains untested; the Whisper path requires Python 3.9+, so it cannot be assumed to work with Ubuntu 20.04's default Python 3.8. Two supervised trials do not establish general Arabic recognition accuracy.

</div>
