<div dir="rtl" lang="ar">

# تشغيل مؤشر LED وإطفاؤه بالصوت العربي

نجحت تجربتان على جهاز <span dir="ltr">Raspberry Pi 5</span>: «شغل اللمبة» أضاءت المؤشر، ثم «أطفئ اللمبة» أطفأته. أكد المستخدم المشاهدة في الحالتين. [سجل التجربة وحدودها](../../validation/runs/2026-10-24-pi5-earpods-voice-led.json).

المسار التعليمي: **تسجيل خمس ثوان ← الاستماع إلى التسجيل ← تحويل الكلام إلى نص ← مطابقة عبارة كاملة ← خدمة ROS ← وكيل GPIO الأصلي ← المؤشر**. يسجل الميكروفون ويعمل النموذج على النظام الأصلي، وتعمل خدمة اللمبة داخل حاوية <span dir="ltr">Noetic</span>.

## الجهاز والقطع والإعدادات التي اختبرت

- جهاز <span dir="ltr">Pi 5، Ubuntu 24.04.5 LTS arm64، RAM 2 GB</span>. يحتاج مسار <span dir="ltr">Whisper</span> إلى <span dir="ltr">Python 3.9+</span>؛ لم يختبر على <span dir="ltr">Pi 4 / Ubuntu 20.04 / Python 3.8</span>.
- سماعة <span dir="ltr">Apple EarPods USB-C</span> عبر محول بيانات إلى منفذ <span dir="ltr">USB-A</span>؛ معرف الجهاز <code dir="ltr">05ac:110b</code>، ومدخل الصوت <code dir="ltr">hw:CARD=EarPods,DEV=0</code>.
- تسجيل أحادي القناة، <span dir="ltr">48 kHz، PCM 16-bit</span>، وكسب العتاد <span dir="ltr">100% / +32 dB</span>. لا تكبير إضافيا ولا فلتر في تجربتي أبل الناجحتين. لا تنقل إعدادات الميكروفون السابق إلى هذه السماعة.
- مؤشر صغير ومقاومة <span dir="ltr">330 Ω</span>: الطرف الفيزيائي <span dir="ltr">11 / BCM17</span> إلى المقاومة ثم موجب المؤشر، وسالبه إلى الطرف <span dir="ltr">6 / GND</span>. راجع [تمرين التوصيل والخدمة](../../labs/06-embedded-systems/03-raspberry-pi/pi5-first-run.md).
- الوكيل الحقيقي وحاوية <code dir="ltr">course204-lamp</code> يعملان قبل تجربة الصوت. يعرض السجل <code dir="ltr">simulated: false</code>.

## 1. تجهيز الصوت والنموذج

نفذ من جذر المشروع على الرازبيري. يعرض الفحص اسم البطاقة الفعلي؛ لا تعتمد على رقمها وحده. أمر الكسب التالي خاص بسماعة أبل المختبرة.

</div>

```bash
sudo apt-get install -y --no-install-recommends alsa-utils libatomic1 libportaudio2
.venv-agent/bin/python -m pip install '.[speech-whisper]'
sudo usermod -aG audio "$USER"
# Log in again after changing group membership.
arecord -l
cat /proc/asound/EarPods/stream0
amixer -c EarPods sset Headset capture 100% cap
```

<div dir="rtl" lang="ar">

حمل النموذج مرة واحدة من [مستودع Systran الرسمي](https://huggingface.co/Systran/faster-whisper-small) إلى المجلد المستثنى من Git. يستخدم التحويل بعد ذلك الملفات المحلية، ولا يرفع الصوت إلى خدمة سحابية.

</div>

```bash
mkdir -p models/faster-whisper-small
for file in config.json model.bin tokenizer.json vocabulary.txt; do
  curl -fL --retry 3 \
    "https://huggingface.co/Systran/faster-whisper-small/resolve/536b0662742c02347bc0e980a01041f333bce120/$file?download=true" \
    -o "models/faster-whisper-small/$file"
done
```

<div dir="rtl" lang="ar">

## 2. سجل خمس ثوان واستمع أولا

تشغل [أداة التسجيل](../../tools/capture_microphone.py) دون نموذج التعرف أو أوامر أجهزة. بعد الضغط على Enter يظهر عد تنازلي خمس ثوان. تحدث عند إشارة «تحدث الآن»؛ الملف المحفوظ **خمس ثوان بالضبط**. تستبعد الأداة تهيئة المدخل لمدة <span dir="ltr">100 ms</span> قبل إشارة التحدث لتجنب نبضة بدء التسجيل التي رصدت مع الميكروفون السابق.

قل «شغل اللمبة» مرة واحدة. بعد اكتمال التسجيل اكتب <code dir="ltr">q</code> للخروج. تحفظ الأداة الأصل ونسخة الاستماع في مجلد محلي خاص بصلاحيات المستخدم. خيارات الفلتر وكسب الالتقاط الإضافي غير مستخدمة مع سماعة أبل؛ خيار الكسب في الأداة يصف إعداد ALSA الموجود ولا يغير كسب العتاد.

</div>

```bash
python3 tools/capture_microphone.py --device hw:CARD=EarPods,DEV=0 --rate 48000
# After the recording, enter q to finish the capture session.
```

<div dir="rtl" lang="ar">

للاستماع من سماعة أبل الموصولة بالرازبيري، شغل الملف التالي. ويمكن نسخه إلى الحاسب للاستماع هناك؛ استبدل <code dir="ltr">PI_USER@PI_HOST</code> ببيانات الاتصال ونفذ أمر النسخ على الحاسب. كان الاستماع في التجربة المسجلة عبر مشغل محلي في الحاسب.

</div>

```bash
# On the Pi, to listen through the EarPods:
aplay -D plughw:CARD=EarPods,DEV=0 "$HOME/.local/state/course204/audio/microphone-gain-check.wav"

# Alternative: on the laptop, copy the same file, then play it locally:
scp PI_USER@PI_HOST:.local/state/course204/audio/microphone-gain-check.wav .
```

<div dir="rtl" lang="ar">

## 3. حول التسجيل نفسه إلى نص

تقرأ [أداة التعرف](../../tools/voice_lamp.py) الملف الأصلي بتردد <span dir="ltr">48 kHz</span> وتحوله في الذاكرة إلى <span dir="ltr">16 kHz</span> للنموذج. لا يتغير ملف الاستماع. الكلمة المساعدة «اللمبة» سياق للمفردات؛ ليست أمرا كاملا يفرض على النموذج. زيد عدد بدائل فك الترميز إلى خمسة بعد أن كتب النموذج «اللنبة» في إحدى المحاولات.

</div>

```bash
.venv-agent/bin/python tools/voice_lamp.py \
  --backend whisper --model models/faster-whisper-small \
  --wav "$HOME/.local/state/course204/audio/microphone-gain-check.wav" \
  --gain-db 0 --hotwords 'اللمبة' --minimum-confidence 0
```

<div dir="rtl" lang="ar">

اقرأ النص الخام أولا. لا تضف مطابقات تقريبية لتحويل جملة خاطئة إلى أمر. يقبل التطبيق العبارة المعتمدة الكاملة بعد تطبيع الكتابة، ويرفض النص الفارغ والمجهول والنفي وجمع التشغيل والإطفاء.

## 4. أرسل الأمر إلى ROS بعد فحص النص

ينفذ المثال التالي الأمر المطابق من التسجيل نفسه. يتحقق العميل من أن الوكيل حقيقي، ثم يفحص نجاح خدمة ROS والحالة التي أعادتها. يتيح هذا اختبار كل مرحلة على حدة.

</div>

```bash
sudo .venv-agent/bin/python tools/voice_lamp.py \
  --backend whisper --model models/faster-whisper-small \
  --wav "$HOME/.local/state/course204/audio/microphone-gain-check.wav" \
  --gain-db 0 --hotwords 'اللمبة' --minimum-confidence 0 --execute
```

<div dir="rtl" lang="ar">

أعد التسجيل والاستماع بعبارة «أطفئ اللمبة»، ثم نفذ التحويل والإرسال. شاهد المؤشر فعليا؛ استجابة البرنامج لا تستبدل المشاهدة. عند إنهاء الجلسة يمكن تأكيد الإطفاء بالأمر التالي.

</div>

```bash
sudo docker exec course204-lamp /course-entrypoint.sh rosservice call /lamp/set false
```

<div dir="rtl" lang="ar">

## 5. أضف الرد الصوتي بعد تأكيد ROS

يولد [برنامج تجهيز الردود](../../tools/prepare_spoken_replies.py) الملفين «تم تشغيل اللمبة» و«تم إطفاء اللمبة» مرة واحدة بمحرك [Piper المحلي](https://github.com/OHF-Voice/piper1-gpl) وصوت <code dir="ltr">ar_JO-kareem-medium</code>. تحفظ الملفات في مجلد المستخدم الخاص، وتفحص هوية النص وبصمة كل ملف قبل التشغيل. لا يحتاج كل أمر إلى تحميل نموذج توليد الصوت؛ يعاد تشغيل الملف الجاهز بعد نجاح الخدمة.

يعمل توليد الصوت في بيئة مستقلة. سجل المشروع بوضع قابل للتعديل في بيئة التعرف أيضا حتى تجد الوحدة الجديدة؛ لا تكفي نسخة قديمة مثبتة من الحزمة.

</div>

```bash
python3 -m venv .venv-tts
.venv-tts/bin/python -m pip install -e '.[speech-reply]'
.venv-agent/bin/python -m pip install --no-deps -e .
mkdir -p models/piper-ar
for file in ar_JO-kareem-medium.onnx ar_JO-kareem-medium.onnx.json MODEL_CARD; do
  curl -fL --retry 3 \
    "https://huggingface.co/rhasspy/piper-voices/resolve/5041a7a49ae5b3a0f30e6837769eb03fdbb231bd/ar/ar_JO/kareem/medium/$file?download=true" \
    -o "models/piper-ar/$file"
done
printf '9e95cab07b679da603bba17c4dec7ab3111320571964ee95c0379603c086491e  models/piper-ar/ar_JO-kareem-medium.onnx\n' | sha256sum -c -
.venv-tts/bin/python tools/prepare_spoken_replies.py \
  --model models/piper-ar/ar_JO-kareem-medium.onnx --volume 0.65
```

<div dir="rtl" lang="ar">

البس سماعة أبل المتصلة بالرازبيري، ثم نفذ الأمر التالي بعد تسجيل العبارة والاستماع إليها. تؤكد [وحدة الرد](../../shared/ros/course_common/src/course204/spoken_replies.py) نجاح الطلب والحالة المطلوبة وكون الوكيل حقيقيا قبل استدعاء <code dir="ltr">aplay</code>. فشل الإخراج الصوتي يسجل مستقلا عن نجاح تحكم ROS. يظهر أمر إخراج الصوت واستجابتا التحكم والرد في الطرفية.

</div>

```bash
sudo .venv-agent/bin/python tools/voice_lamp.py \
  --backend whisper --model models/faster-whisper-small \
  --wav "$HOME/.local/state/course204/audio/microphone-gain-check.wav" \
  --gain-db 0 --hotwords 'اللمبة' --minimum-confidence 0 --execute \
  --reply-dir "$HOME/.local/state/course204/replies" \
  --playback-device plughw:CARD=EarPods,DEV=0
```

<div dir="rtl" lang="ar">

## 6. النداء «يا مساعد» ثم الأمر

أضيف [مساعد النداء](../../tools/wake_assistant.py) واختبر على شاشة HDMI للرازبيري. يستخدم نموذج <span dir="ltr">Whisper base</span> لتحويل مقطع النداء إلى نص ومطابقته، ثم النموذج <span dir="ltr">small</span> للأمر. هذا كشف نداء قائم على التعرف على الكلام، وليس نموذج كلمة تنبيه مدربا مستقلا. يوقف استقبال الميكروفون أثناء المعالجة ورد النجاح، ويستبعد صوت «تفضل» من طابور التسجيل قبل فتح نافذة الأمر.

حمل نموذج النداء المثبت، وأعد تجهيز الردود مع رسالة الجاهزية. افحص بطاقة أبل وكسبها كما في الخطوات السابقة قبل تشغيل الاستماع.

</div>

```bash
mkdir -p models/faster-whisper-base
for file in config.json model.bin tokenizer.json vocabulary.txt; do
  curl -fL --retry 3 \
    "https://huggingface.co/Systran/faster-whisper-base/resolve/ebe41f70d5b6dfa9166e2c581c45c9c0cfc57b66/$file?download=true" \
    -o "models/faster-whisper-base/$file"
done
.venv-tts/bin/python tools/prepare_spoken_replies.py \
  --model models/piper-ar/ar_JO-kareem-medium.onnx --volume 0.65 --include-ready
sudo .venv-agent/bin/python tools/wake_assistant.py \
  --wake-model models/faster-whisper-base \
  --command-model models/faster-whisper-small \
  --device hw:CARD=EarPods,DEV=0 \
  --playback-device plughw:CARD=EarPods,DEV=0 \
  --reply-dir "$HOME/.local/state/course204/replies" --minimum-confidence 0
```

<div dir="rtl" lang="ar">

انتظر <code dir="ltr">LISTENING_FOR_WAKE</code>، وقل **«يا مساعد» وحدها**. عند سماع **«تفضل»** قل **«شغل اللمبة»** أو **«أطفئ اللمبة»** مباشرة خلال خمس ثوان. يعود البرنامج إلى انتظار النداء بعد النتيجة. لا تقل النداء والأمر في جملة واحدة في هذا المسار ذي المرحلتين. يوقف <span dir="ltr">Ctrl+C</span> البرنامج من الطرفية المتحكمة.

تستخدم المقاطع ملفات WAV مؤقتة محلية وتحذف عند الإيقاف السليم. خيار <code dir="ltr">--save-commands</code> اختياري لتشخيص الأوامر المفعلة فقط، وليس لحفظ صوت الانتظار. لم يثبت تشغيل تلقائي عند الإقلاع. اختبر التشغيل والإطفاء مع النداء، وأكد المستخدم تجاهل أمر تشغيل دون النداء؛ لم تقاس دقة تنبيه عامة. راجع [السجل الكامل](../../validation/runs/2026-10-24-pi5-wake-assistant.json) و[نقطة المتابعة للتاريخ والطقس](../../docs/session-checkpoint-2026-10-24.md).

## النتيجة وحدود التجربة

نجح تشغيل المؤشر وإطفاؤه من تسجيلين جديدين وسمع المستخدم كل تسجيل قبل التحويل. استغرق التعرف نحو <span dir="ltr">8–9</span> ثوان بعد التسجيل والاستماع؛ هذا ليس استماعا مستمرا. [سجل التعرف الأولي](../../validation/runs/2026-10-24-pi5-earpods-speech.json) يحفظ أيضا المحاولات غير الدقيقة والتعديل الذي صحح الاسم.

نجح لاحقا [اختبار الرد الصوتي](../../validation/runs/2026-10-24-pi5-earpods-spoken-replies.json) بإعادة معالجة التسجيلين السابقين. أكد المستخدم وضوح الردين في سماعة أبل بعد إضاءة المؤشر وإطفائه. بقي فشل الاستيراد الأول وتصحيحه موثقين في السجل، ولم ينفذ ذلك الفشل أي أمر ROS.

استخدم العرض التعليمي حد ثقة <span dir="ltr">0</span> مع المطابقة الكاملة لعبارتين والتحكم بمؤشر منخفض القدرة. يظل الحد الافتراضي للأداة <span dir="ltr">0.8</span>. درجات النموذج ليست نسبة دقة مقاسة؛ لم تعاير عتبة مناسبة للتشغيل العام، ولم تثبت تجربتان دقة اللهجات أو الميكروفونات الأخرى. لم تختبر استمرارية إعداد السماعة بعد إعادة التشغيل، ولا هذا المسار على جهاز <span dir="ltr">Pi 4</span> فعلي.

تبقى التسجيلات والنموذج محليين. لا ترفع ملفات الصوت أو بيانات الاتصال أو كلمات المرور إلى مستودع المقرر. إعداد [الميكروفون العام السابق](../../environments/pi5-ubuntu2404/course204-microphone.conf) خاص ببطاقة <code dir="ltr">Audio</code>؛ ليس مطلوبا لسماعة أبل في هذا الدليل.

</div>

<div dir="ltr" lang="en">

## English

Two fresh, supervised trials on a real Pi 5 passed: **شغل اللمبة → text → ROS → LED ON**, followed by **أطفئ اللمبة → text → ROS → LED OFF**. The user observed both transitions. See the [end-to-end record](../../validation/runs/2026-10-24-pi5-earpods-voice-led.json).

The tested host was Ubuntu 24.04.5 arm64 on a 2 GB Pi 5. The microphone was Apple EarPods USB-C, USB ID `05ac:110b`, input `hw:CARD=EarPods,DEV=0`, mono 48 kHz / 16-bit PCM. Its native Headset capture control was 100% / +32 dB. Additional software gain and filtering were disabled. This Whisper path needs Python 3.9+ and has not been tested on the Pi 4 Ubuntu 20.04 / Python 3.8 course environment.

Use the shared command blocks above in order. Install the native dependencies and pinned local model. Run `capture_microphone.py`, press Enter, wait for the five-second countdown, and say one phrase during the five-second recording. The tool discards 100 ms of device settling before the speaking cue, saves exactly five seconds, and preserves private raw recordings. Enter `q`, then play the latest file through the EarPods or copy it to the laptop. No audio is sent to cloud inference.

After listening, transcribe that same WAV with `voice_lamp.py`. The 48 kHz source is resampled to 16 kHz in memory. The noun `اللمبة` supplies vocabulary context and the decoder uses five beams; the complete command is not inserted as a prompt. Inspect the raw transcript before adding `--execute`. Execution uses the ROS service and native GPIO agent; the container does not directly own GPIO. Repeat with the OFF phrase, observe the actual LED, and finish with the explicit OFF command if necessary.

For spoken acknowledgements, follow step 5: install pinned Piper 1.8.0 in `.venv-tts`, register the project in the recognition environment, download the pinned Arabic Kareem voice and verify its SHA-256. `prepare_spoken_replies.py` renders the two fixed phrases once at volume 0.65 without playback or GPIO access. The private cache contains WAV files and a text/hash manifest. The voice model and generated audio remain outside version control.

The [spoken reply test](../../validation/runs/2026-10-24-pi5-earpods-spoken-replies.json) replayed the earlier successful recordings. The user confirmed clear ON/OFF replies through the EarPods and both LED transitions. An initial missing-module failure stopped before ROS execution; editable registration of the current project fixed it and the cache/import checks passed before retrying.

Wear the EarPods attached to the Pi. Add `--reply-dir` and the explicit `--playback-device plughw:CARD=EarPods,DEV=0` to the execution command. The client checks the cache before inference and speaks success only after a matching successful physical ROS acknowledgement. It logs the `aplay` command and reports audio playback failure separately from already successful device control. Invalid or rejected commands do not produce a success reply.

Step 6 adds the [two-stage wake assistant](../../tools/wake_assistant.py). It keeps base/small int8 Whisper models loaded, uses bounded voice-activity segmentation for wake transcription, and strictly matches `يا مساعد`. This is speech-recognition-based gating, not a separately trained keyword detector. Say the wake phrase alone, wait for `تفضل`, then say one command within five seconds. Input is paused during recognition and success replies; readiness playback is discarded before arming command capture. Private temporary WAVs are overwritten and removed on clean exit. Persistent command recording is optional, and no boot service is installed. The user confirmed both wake/LED/reply cycles and reported a bare lamp command was ignored; general false-accept/reject rates remain unmeasured. See the [wake record](../../validation/runs/2026-10-24-pi5-wake-assistant.json) and [resume checkpoint](../../docs/session-checkpoint-2026-10-24.md).

The measured demo used `--minimum-confidence 0` with an exact full-phrase allowlist. The CLI default remains 0.8; neither threshold has been calibrated as a general correctness guarantee. Empty, unknown, negated and combined phrases are rejected. Recognition took about 8–9 seconds after recording/playback. Two successful trials do not establish general Arabic accuracy, continuous listening, Pi 4 compatibility or reboot persistence. Preserve failures in the [speech record](../../validation/runs/2026-10-24-pi5-earpods-speech.json). Do not publish audio, models, credentials or private connection details.

</div>
