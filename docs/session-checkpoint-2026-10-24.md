<div dir="rtl" lang="ar">

# نقطة متابعة المشروع — 24 أكتوبر 2026

## ما نجح فعليًا

- <span dir="ltr">Pi 5 / Ubuntu 24.04.5 arm64 / RAM 2 GB</span>، وخدمة لمبة <span dir="ltr">ROS Noetic</span> داخل حاوية <code dir="ltr">course204-lamp</code> ووكيل GPIO أصلي.
- سماعة <span dir="ltr">Apple EarPods USB-C</span>، ومدخل <code dir="ltr">hw:CARD=EarPods,DEV=0</code>، وكسب العتاد <span dir="ltr">100% / +32 dB</span>، دون تكبير ملف التسجيل أو فلتر.
- الاستماع في حالة الجاهزية لعبارة «يا مساعد»؛ يرد «تفضل»، ثم يسجل الأمر خمس ثوان. نجح «شغل اللمبة» و«أطفئ اللمبة» مع التنفيذ الفعلي ورد النجاح المناسب. أكد المستخدم المشاهدة وسماع الردود. وأكد تجاهل أمر التشغيل دون النداء.
- كشف النداء يستخدم <span dir="ltr">Whisper base</span> مع تقسيم الصوت، والأوامر تستخدم <span dir="ltr">Whisper small</span>. كلاهما محلي <code dir="ltr">int8</code>، ويبقيان محملين لتجنب إعادة التحميل لكل أمر. الاستماع يتوقف مؤقتا أثناء المعالجة والرد.
- عرض التجهيز والنتائج على شاشة HDMI للرازبيري، في <code dir="ltr">tty2</code> عبر جلسة <code dir="ltr">course204:voice</code> للعرض فقط. أكد المستخدم ظهورها.
- اجتازت اختبارات Python الثلاثون المسجلة. راجع [سجل النداء](../validation/runs/2026-10-24-pi5-wake-assistant.json) و[الدليل العملي](../extensions/voice-home-automation/pi5-voice-led.md).

## حالة التوقف

طلب المستخدم الحفظ والمتابعة لاحقا. أوقف الاستماع وأرسل أمر إطفاء للمؤشر. لم يثبت تشغيل تلقائي عند الإقلاع. المصدر محفوظ في المشروع على الحاسب وعلى الرازبيري؛ لا تحفظ كلمات المرور أو المفاتيح أو التسجيلات الخاصة في Git. ما زالت دقة النداء العامة ومسار <span dir="ltr">Pi 4</span> وإعادة التشغيل بحاجة للتحقق.

أكد النظام الإطفاء ثم انقطع اتصال الرازبيري أثناء إنهاء الجلسة. أحدث التوثيق وملف المتابعة محفوظان على الحاسب؛ زامنهما مع الرازبيري عند الرجوع. الحفظ النهائي نسخة Git محلية؛ لم يحدث GitHub في خطوة الحفظ هذه. تبقى تغييرات الموقع في <code dir="ltr">docs/index.html</code> و<code dir="ltr">docs/sitemap.txt</code> خارج نقطة الحفظ الخاصة بهذا العمل لأنها من عمل متزامن آخر.

## إعادة التشغيل عند الرجوع

راجع تشغيل الوكيل والحاوية في [دليل الرازبيري](../labs/06-embedded-systems/03-raspberry-pi/pi5-first-run.md). تأكد من بطاقة الصوت ووجود النماذج والردود المحلية. استخدم الطرفية على شاشة الرازبيري؛ نفذ من جذر المستودع. لا تبدأ التقاط الميكروفون قبل إبلاغ المستخدم.

</div>

```bash
arecord -l
amixer -c EarPods sset Headset capture 100% cap
sudo .venv-agent/bin/python tools/wake_assistant.py \
  --wake-model models/faster-whisper-base \
  --command-model models/faster-whisper-small \
  --device hw:CARD=EarPods,DEV=0 \
  --playback-device plughw:CARD=EarPods,DEV=0 \
  --reply-dir "$HOME/.local/state/course204/replies" \
  --minimum-confidence 0
```

<div dir="rtl" lang="ar">

انتظر <code dir="ltr">LISTENING_FOR_WAKE</code>، قل «يا مساعد» وحدها، وانتظر «تفضل»، ثم قل الأمر مباشرة. حد الثقة صفر مستخدم في العرض التعليمي مع المطابقة الكاملة؛ ليس عتبة معايرة للتشغيل العام. ينهي <span dir="ltr">Ctrl+C</span> البرنامج من الطرفية المتحكمة. شاشة العرض الحالية للقراءة فقط؛ يمكن إيقاف الجلسة من اتصال التحكم.

## الخطوة التالية المطلوبة من المستخدم

إضافة **التاريخ ودرجة الحرارة** مع رد عربي صوتي:

1. تحديد مدينة الطقس عند الرجوع؛ لم يحدد المستخدم مدينة بعد، فلا تستنتجها من المنطقة الزمنية.
2. أخذ التاريخ من ساعة الجهاز المضبوطة على <code dir="ltr">Asia/Riyadh</code>؛ اسأل إن كان يريد الميلادي فقط أم الهجري أيضا.
3. جلب درجة الحرارة من مصدر منظم مثل <span dir="ltr">Open-Meteo</span>، مع مهلة اتصال ورسالة تعذر واضحة؛ لا تختلق قراءة عند انقطاع الشبكة.
4. توسيع توليد الرد من الملفين الثابتين إلى نص عربي ديناميكي، مع الحفاظ على كتم استقبال الأوامر أثناء الرد.
5. الحفاظ على بوابة «يا مساعد» وضوابط ROS الحالية، وتوثيق كل إضافة بالعربي والإنجليزي واختبارها على الشاشة الفعلية.

### تفضيلات مهمة

أبلغ المستخدم قبل الاختبار أو التسجيل. مدة تسجيل الأمر خمس ثوان. في تشخيص الميكروفون، شغل التسجيل نفسه قبل تحويله للنص؛ لا تعتبر تفضيل نسخة على أخرى اعتمادا نهائيا. لا تبدل العبارات المطلوبة: يقول المستخدم «شغل اللمبة». لا تنفذ عبارة يكتبها أثناء اختبار التعرف على أنها أمر جهاز دون فهم السياق.

</div>

<div dir="ltr" lang="en">

## English handoff

The live Pi 5 prototype passed wake → readiness reply → five-second command → physical ROS lamp control → spoken acknowledgement. The user confirmed ON/OFF observations and hearing, and reported that a command without the wake phrase was ignored. See the linked evidence; these limited trials are not a general wake accuracy benchmark.

At the user's request, stop listening and leave the lamp OFF for the saved checkpoint. No boot-start service was installed. The physical HDMI console is a read-only view of `course204:voice`. Resume using the explicit EarPods device and the command above after notifying the user.

OFF was acknowledged before the Pi connection dropped. The latest documentation/checkpoint is on the laptop and should be synced when reconnecting. This save creates a local Git checkpoint, not a GitHub update. Preserve the concurrent website edits in `docs/index.html` and `docs/sitemap.txt`; they are outside this checkpoint.

Next requested work: Arabic date and weather replies. Ask for the weather city; do not infer it from the timezone. Use the Pi clock with `Asia/Riyadh` for date, a structured online weather source with a timeout/error response for temperature, and dynamic local Arabic TTS. Preserve wake gating, ROS acknowledgement checks, the five-second command window, bilingual documentation, and the user's requirement to see commands on the Pi display. Do not commit credentials, model binaries or private audio.

</div>
