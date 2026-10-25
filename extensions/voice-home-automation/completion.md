<div dir="rtl" lang="ar">

# محضر إكمال المساعد الصوتي التعليمي

**الحالة: مكتمل للنطاق المتفق عليه على الرازبيري 5.**

**تاريخ الإكمال:** 25 أكتوبر 2026. **اعتماد المستخدم:** «وثق ويعتبر مكتمل» بعد تأكيد مشاهدة اللمبة وسماع الردود خلال التجارب.

## النتيجة المسلمة

مساعد محلي يستمع للنداء «يا مساعد»، ويرد «تفضل»، ثم يلتقط طلبا مدته **خمس ثوان** ويحوّله إلى نص عربي. يعالج الطلب المحدد ويرد صوتيا عبر سماعة أبل، ثم يعود إلى انتظار النداء عند تشغيل الوضع المستمر.

| الوظيفة | العبارة | نتيجة التحقق |
| --- | --- | --- |
| التنبيه والجاهزية | يا مساعد | نجح النداء ورد «تفضل»؛ أكد المستخدم تجاهل أمر لمبة دون نداء |
| تشغيل المؤشر الفعلي | شغل اللمبة | نجح الطلب عبر ROS ثم «تم تشغيل اللمبة»؛ أكد المستخدم الإضاءة والرد |
| إطفاء المؤشر الفعلي | أطفئ اللمبة | نجح الطلب عبر ROS ثم «تم إطفاء اللمبة»؛ أكد المستخدم الإطفاء والرد |
| التاريخ الميلادي | كم التاريخ اليوم | تعرف على السؤال وأجاب من ساعة الجهاز بتوقيت السعودية؛ أكد المستخدم سماع التاريخ |
| حرارة جدة الحالية | كم درجة الحرارة اليوم | جلب البيانات من الإنترنت وأجاب بالعربية؛ أكد المستخدم سماع الرد في المحاولة الناجحة |
| العرض التعليمي | شاشة الأوامر المباشرة | عرض التجهيز والتعرف والنتائج؛ نجح العرض على شاشة الرازبيري سابقا وعلى شاشة الحاسب في الجلسة الأخيرة |

## بيئة التنفيذ والقطع

<span dir="ltr">Raspberry Pi 5، 2 GB RAM، Ubuntu 24.04.5 arm64</span>؛ سماعة <span dir="ltr">Apple EarPods USB-C</span> للإدخال والإخراج. كسب الالتقاط <span dir="ltr">100% / +32 dB</span>، والتسجيل <span dir="ltr">48 kHz، mono، 16-bit PCM</span>، دون تكبير ملف التسجيل. المؤشر موصل عبر مقاومة <span dir="ltr">330 Ω</span> إلى <span dir="ltr">BCM17 / physical pin 11</span>، والعودة إلى <span dir="ltr">GND / physical pin 6</span>.

التعرف محلي باستخدام نموذجي <span dir="ltr">Whisper base / small</span>، والرد الصوتي باستخدام <span dir="ltr">Piper ar_JO-kareem-medium</span>. خدمة اللمبة <span dir="ltr">ROS Noetic</span> داخل حاوية، مع وكيل <span dir="ltr">GPIO</span> أصلي. مصدر الطقس <span dir="ltr">Open-Meteo</span> لإحداثيات مدينة جدة التي حددها المستخدم. التفاصيل وأوامر إعادة التشغيل في [دليل اللمبة والنداء](pi5-voice-led.md) و[دليل التاريخ والطقس](date-weather.md).

## التحقق والحفظ

اجتازت **37 حالة اختبار برمجية** على الحاسب، واجتازت **7 حالات جديدة للمعلومات** على الرازبيري. أكدت تجارب المستخدم التشغيل والإطفاء والردود الصوتية والتاريخ والحرارة. حفظت أيضا إخفاقات التعرف وتصحيحها: رفض نص «الحرار» في محاولة الطقس الأولى، ثم نجحت الإعادة بعد تحسين سياق مفردات السؤال؛ لم يضف مرادف للنص الخاطئ.

الأدلة: [النداء](../../validation/runs/2026-10-24-pi5-wake-assistant.json)، [التحكم الصوتي الفعلي](../../validation/runs/2026-10-24-pi5-earpods-voice-led.json)، [ردود اللمبة](../../validation/runs/2026-10-24-pi5-earpods-spoken-replies.json)، [التاريخ والطقس](../../validation/runs/2026-10-25-pi5-date-weather.json).

عند إنهاء الجلسة بطلب المستخدم: **الاستماع متوقف واللمبة مطفأة**. تحقق عدم وجود تسجيل جار، وأكدت خدمة ROS الإطفاء ثم قراءة الوكيل الحقيقي الحالة نفسها. الكود والتوثيق محفوظان محليا وعلى الرازبيري؛ تحفظ نسخة Git محلية لهذا التسليم. لم ينشر تحديث GitHub في خطوة الإكمال. لا تشمل الملفات كلمات مرور أو نماذج كبيرة أو تسجيلات صوت المستخدم.

## حدود هذا الإكمال

يشمل الإكمال الوظائف المسلمة أعلاه على الجهاز المختبر. يظل اختبار هذا الامتداد على جهاز <span dir="ltr">Pi 4</span> فعلي، وقياس دقة التعرف العامة، والتشغيل التلقائي عند الإقلاع، والتاريخ الهجري، وتكاملات النموذج اللغوي وواتساب أعمالا مستقلة عند طلبها. استخدم حد الثقة صفر في العرض التعليمي مع مطابقة العبارة الكاملة؛ لا يمثل ذلك معايرة تشغيل عام. تبقى نتائج بقية تمارين المقرر كما هي في سجلاتها.

</div>

<div dir="ltr" lang="en">

## Completion record — English

**Status: COMPLETE for the agreed Pi 5 educational assistant scope, accepted by the user on 2026-10-25.**

Delivered: local `يا مساعد` wake gating, spoken readiness, five-second Arabic command capture, physical ROS LED ON/OFF with spoken success only after acknowledgement, Gregorian date at Saudi time, current Jeddah temperature from Open-Meteo, dynamic local Arabic speech, continuous-mode return to wake listening, and visible terminal commands/results.

The observed setup is Pi 5 2 GB / Ubuntu 24.04.5 arm64, Apple EarPods USB-C input/output at native capture gain 100% (+32 dB), mono 48 kHz 16-bit PCM, and BCM17 LED through 330 ohms to ground. Whisper base/small and Piper run locally; a Noetic container communicates with the native GPIO agent. See the [lamp/wake guide](pi5-voice-led.md) and [date/weather guide](date-weather.md) for dependencies and reproducible commands.

37 local behavioral tests and seven new information tests on Pi passed. User observations confirmed physical LED changes and hearing the lamp/date/weather replies. The [validation records](../../validation/README.md) preserve failures as well as successful trials; the first weather transcript was rejected and the vocabulary-context retry passed. These trials do not establish general recognition accuracy.

Final shutdown was verified: no assistant/capture process remained, the ROS service acknowledged OFF, and the real device agent reported OFF. Source and bilingual documentation are saved on the laptop and Pi, with a local Git checkpoint for delivery. This completion step did not publish a GitHub update. Credentials, private audio and model binaries are excluded.

Physical Pi 4 validation, calibrated recognition benchmarks, boot startup, Hijri dates, language-model and WhatsApp integrations remain separate future work. Completion of this extension does not mark every course exercise physically validated. Threshold zero remains an explicit supervised demonstration setting.

</div>
