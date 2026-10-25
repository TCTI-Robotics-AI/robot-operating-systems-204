<div dir="rtl" lang="ar">

# التاريخ وحرارة جدة بالصوت

امتداد للمساعد التعليمي: قل «يا مساعد» وحدها، وانتظر «تفضل»، ثم اسأل خلال خمس ثوان: **«كم التاريخ اليوم»** أو **«كم درجة الحرارة اليوم»**. يبقى التحكم باللمبة عبر ROS ورد النجاح بعد تأكيد التنفيذ كما في [دليل اللمبة والنداء](pi5-voice-led.md).

## البيانات والرد

- التاريخ **ميلادي** من ساعة الجهاز بتوقيت السعودية، ويعمل دون إنترنت. افحص مزامنة الساعة قبل الاختبار. لم يضف التاريخ الهجري.
- المدينة **جدة** بطلب المستخدم. يحفظ [ملف الإعداد](../../environments/pi5-ubuntu2404/assistant-jeddah.json) إحداثيات المدينة العامة ومرجع خدمة البحث؛ لا يستخدم تحديد موقع الجهاز.
- الحرارة الحالية من [Open-Meteo](https://open-meteo.com/en/docs)، بالدرجة المئوية مع وقت صلاحية البيانات. هي بيانات طقس للمدينة، وليست قياس حساس داخل الغرفة. لا يطلب الصوت أو التسجيل من خدمة الطقس.
- مهلة الشبكة ثماني ثوان، وحجم الاستجابة محدود. ترفض القراءة الناقصة، والوحدة غير المئوية، والقيم غير الصالحة، والبيانات الأقدم من تسعين دقيقة أو المستقبلية بأكثر من خمس عشرة دقيقة. عند الفشل يقول: «عذرا، تعذر جلب درجة الحرارة الآن. حاول مرة أخرى». لا يستبدلها برقم قديم.
- تولد الإجابات المتغيرة محليا عبر نموذج Piper العربي الموجود. يشغل عامل منفصل عند كل جواب لتجنب إبقاء نموذج إضافي في الذاكرة طوال الوقت؛ توجد مهلة انتظار أثناء التوليد. الملفات الصوتية مؤقتة وتحذف بعد انتهاء الرد. يبقى الميكروفون مغلقا أثناء المعالجة والرد.
- المطابقة لعبارات كاملة؛ سؤال التاريخ أو الطقس لا يصل إلى خدمة اللمبة. الطلب المركب مثل «شغل اللمبة وكم التاريخ اليوم» يرفض.

## اختبار دون ميكروفون أو تحريك خرج

نفذ من جذر المشروع على الرازبيري. الأمران يعرضان الإجابة فقط. لفحص الإخراج الصوتي، أبلغ المستمع أولا ثم أضف خيارات الصوت الموضحة أدناه.

</div>

```bash
timedatectl show -p NTPSynchronized -p Timezone
.venv-agent/bin/python tools/assistant_answer.py --text 'كم التاريخ اليوم'
.venv-agent/bin/python tools/assistant_answer.py \
  --text 'كم درجة الحرارة اليوم' \
  --weather-config environments/pi5-ubuntu2404/assistant-jeddah.json

# Add to either answer command to speak through the connected EarPods:
# --tts-python .venv-tts/bin/python \
# --tts-model models/piper-ar/ar_JO-kareem-medium.onnx \
# --playback-device plughw:CARD=EarPods,DEV=0
```

<div dir="rtl" lang="ar">

## تشغيل المساعد

جهز الوكيل والحاوية والردود الثابتة كما في الدليل السابق. افحص وجود سماعة أبل والكسب. **أبلغ المستخدم قبل بدء الاستماع**. تعرض الأوامر والنتائج في الطرفية المباشرة على الشاشة المطلوبة. لا تسجل صوت الانتظار للأرشفة، ولا تستخدم خيار حفظ الأوامر إلا للتشخيص المتفق عليه.

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
  --weather-config environments/pi5-ubuntu2404/assistant-jeddah.json \
  --tts-python .venv-tts/bin/python \
  --tts-model models/piper-ar/ar_JO-kareem-medium.onnx \
  --minimum-confidence 0
```

<div dir="rtl" lang="ar">

عتبة الثقة صفر تخص العرض التعليمي السابق مع المطابقة الكاملة؛ لا تمثل معايرة لدقة التعرف. اختبر السؤالين كل واحد في دورة نداء مستقلة، وأكد ما سمعته. أوقف البرنامج من الطرفية المتحكمة باستخدام Ctrl+C. لا توجد خدمة تشغيل تلقائي مضافة.

## حدود التحقق

نجح السؤالان بصوت المستخدم بعد النداء على Pi 5، وأكد سماع الردين. أخفقت المحاولة الأولى لسؤال الحرارة بسبب نص «الحرار»؛ رفض الطلب، ثم نجحت إعادة المحاولة بعد توسيع سياق مفردات التعرف إلى السؤال الكامل. لم يضف مرادف يطابق النص الخاطئ. هذه تجارب محدودة ولا تقيس دقة التعرف العامة.

راجع [سجل التجربة](../../validation/runs/2026-10-25-pi5-date-weather.json) للتفريق بين الاختبارات الآلية، وجلب البيانات الفعلي، وتشغيل الصوت، وتجربة السؤال بصوت المستخدم. مسار Pi 4 لم يختبر فعليا؛ نموذج Whisper وPiper يتطلبان بيئة Python المناسبة كما في دليل الصوت.

</div>

<div dir="ltr" lang="en">

## English

Both fresh user questions passed after wake on Pi 5, with confirmed hearing. The first weather transcript was rejected; a retry passed after supplying full question vocabulary context. No misspelling alias was added. These limited trials do not establish general recognition accuracy.

The two-stage wake assistant now routes exact Arabic date/current-temperature questions separately from lamp actions. Say `يا مساعد`, wait for `تفضل`, then ask `كم التاريخ اليوم` or `كم درجة الحرارة اليوم` within five seconds. Mixed, negated and unknown requests remain rejected; lamp acknowledgements are unchanged.

Gregorian date uses the device clock at UTC+03:00 (Asia/Riyadh); verify clock synchronization. The explicitly selected city is Jeddah, with public city-center coordinates from Open-Meteo geocoding. Current Celsius temperature comes from the [Open-Meteo Forecast API](https://open-meteo.com/en/docs), not an indoor sensor. The request sends configured coordinates, not audio. Timeout, malformed data, wrong units, invalid values and stale/future data produce an Arabic unavailability reply instead of an invented/cached reading. The JSON answer includes source, validity time and numeric temperature.

Dynamic Arabic speech uses the existing local Piper model in a short-lived isolated worker, with bounded text, playback and process timeouts. Temporary reply WAVs are removed after playback. The microphone is closed during inference and answer playback. No startup service is installed. The commands above support text-only checks, optional EarPods playback and the live assistant; notify the user before playback/recording. Threshold zero remains an explicit supervised demo setting, not a calibrated recognition threshold. See the [run record](../../validation/runs/2026-10-25-pi5-date-weather.json) for actual evidence and untested paths. Physical Pi 4 remains untested.

</div>
