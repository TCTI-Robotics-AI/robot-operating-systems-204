<div dir="rtl" lang="ar">

# تحليل الصوت وتشغيل المحادثة

**مرجع الخطة:** <code dir="ltr">13.3</code> · **الحالة:** الشرح والكود متوفران؛ حالة التشغيل محددة في سجل التحقق.

## الهدف والفكرة

يستخدم المسار <span dir="ltr">Vosk</span> محليا لتحويل ملف صوت أو تسجيل محدود إلى نص. نختار نموذج العربية <span dir="ltr">vosk-model-ar-mgb2-0.4</span> من صفحة النماذج الرسمية، ونفك ضغطه محليا داخل <span dir="ltr">models.</span> المدخل <span dir="ltr">WAV</span> أحادي القناة و<span dir="ltr">PCM</span> بدقة <span dir="ltr">16</span> بت وتردد <span dir="ltr">16000</span> هرتز. النموذج ليس ضمن المستودع، ودقة التعرف على اللهجة تحتاج قياسا فعليا.

## المتطلبات والخطوات

أكمل [دليل البدء](../../../course/getting-started.md) وابن الحزم أولا. نفذ الأوامر من جذر المستودع، وافتح طرفية جديدة لكل برنامج مستمر، ثم حمل بيئة منطقة العمل فيها. أوقف المحاكاة السابقة قبل تشغيل نموذج آخر.

<div dir="ltr">

```bash
# Install on the Ubuntu 20.04 ROS host (outside an isolated venv):
python3 -m pip install --user '.[speech]'
# Put your own 16 kHz mono PCM recording at recordings/command.wav
python3 tools/transcribe.py --model models/vosk-model-ar-mgb2-0.4 --wav recordings/command.wav
```

</div>

<div dir="ltr">

```bash
# Start conversation.launch in another terminal first
roslaunch course_conversation speech.launch model:="$PWD/models/vosk-model-ar-mgb2-0.4" wav:="$PWD/recordings/command.wav"
```

</div>

<div dir="ltr">

```bash
# Stop the previous speech launch; microphone capture lasts eight seconds
roslaunch course_conversation speech.launch model:="$PWD/models/vosk-model-ar-mgb2-0.4" duration:=8
```

</div>

## النتيجة المتوقعة والتحقق

ينشر النص غير الفارغ في /<span dir="ltr">speech/text</span> ويصله رد المحادثة. لا تفعل التحكم الفعلي قبل قياس التعرف على العبارات؛ قد يخطئ التعرف في النفي. استخدم <span dir="ltr">arecord -l</span> وفحص <span dir="ltr">sounddevice</span> عند غياب المايك.

سجل نتيجة جهازك وإصداراته في [سجل التحقق](../../../validation/README.md). نتائج الحاسب المحلي في [التقرير](../../../validation/runs/2026-10-23-wsl-amd64.json) تخص بيئة الاختبار فقط؛ تشغيل الرازبيري بنوعيه والقطع الفعلية يحتاج سجلا مستقلا.

## عند ظهور مشكلة

إذا لم توجد الحزمة، حمل <code dir="ltr">~/course204_ws/devel/setup.bash</code> وافحص <code dir="ltr">rospack find</code> باسم الحزمة. إذا لم يتصل عميل بخدمة، تحقق من تشغيل الخادم ومن تطابق <code dir="ltr">ROS_MASTER_URI</code>. عند اختبار العتاد، تحقق من الموديل والتوصيل والمنفذ قبل إعادة إرسال الأمر. راجع رسائل الطرفية قبل اعتبار العملية ناجحة.

## تطبيق المتدرب والتسليم

سجل عشر عبارات عربية مع النص الصحيح والناتج، واحسب نسبة المطابقة والأخطاء التي تغير المعنى. استخدم ملفاتك فقط وسجل المايك والنموذج. أرفق الأوامر والنتائج وتفسيرها، والإصدارات وسجل التحقق. لا تسجل نتيجة متوقعة على أنها مشاهدة فعلية.

## المراجع والملفات

- [Course conversation package](../ros/course_conversation/)
- [Python AIML interpreter](https://github.com/paulovn/python-aiml)
- [Vosk models and licenses](https://alphacephei.com/vosk/models)
- [Vosk Python examples](https://github.com/alphacep/vosk-api/tree/master/python/example)

[الوحدة](../README.md) · [فهرس المقرر](../../../course/exercises-index.md).

</div>

<div dir="ltr" lang="en">

# Speech recognition and conversation

**Syllabus reference:** `13.3` · **Status:** Instructions and source provided; runtime evidence is recorded separately.

## Objective and concept

Vosk transcribes a WAV or bounded microphone recording locally. Download/extract the Arabic vosk-model-ar-mgb2-0.4 model from the official catalog into models. WAV input must be mono, 16-bit PCM, 16000 Hz. Models are not committed; dialect accuracy requires measurement on real recordings.

## Requirements and procedure

Complete the [getting started guide](../../../course/getting-started.md) and build the packages first. Run repository-relative commands from the repository root. Use a separate terminal for each long-running process and source the workspace in every ROS terminal. Stop the previous simulation before launching another model.

```bash
# Install on the Ubuntu 20.04 ROS host (outside an isolated venv):
python3 -m pip install --user '.[speech]'
# Put your own 16 kHz mono PCM recording at recordings/command.wav
python3 tools/transcribe.py --model models/vosk-model-ar-mgb2-0.4 --wav recordings/command.wav
```

```bash
# Start conversation.launch in another terminal first
roslaunch course_conversation speech.launch model:="$PWD/models/vosk-model-ar-mgb2-0.4" wav:="$PWD/recordings/command.wav"
```

```bash
# Stop the previous speech launch; microphone capture lasts eight seconds
roslaunch course_conversation speech.launch model:="$PWD/models/vosk-model-ar-mgb2-0.4" duration:=8
```

## Expected result and validation

Nonempty recognition publishes /speech/text and receives a dialogue response. Keep physical execution disabled while evaluating recognition, especially negations. Inspect arecord -l and sounddevice devices for microphone problems.

Record your board, versions and observed results in the [validation guide](../../../validation/README.md). The [local report](../../../validation/runs/2026-10-23-wsl-amd64.json) covers only its stated environment. Pi 4, Pi 5 and physical device runs require separate records.

## Troubleshooting

If a package is missing, source `~/course204_ws/devel/setup.bash` and check `rospack find PACKAGE`. For service connection failures, start the server and compare `ROS_MASTER_URI` settings. For hardware, verify the board, wiring and device path before retrying. Read terminal errors before reporting success.

## Learner task and submission

Record ten Arabic phrases with reference/transcribed text and compute exact matches and meaning-changing errors. Use your own recordings and record microphone/model details. Submit commands, observations, explanations, software versions and the run record. Do not present expected output as observed evidence.

## Sources and files

- [Course conversation package](../ros/course_conversation/)
- [Python AIML interpreter](https://github.com/paulovn/python-aiml)
- [Vosk models and licenses](https://alphacephei.com/vosk/models)
- [Vosk Python examples](https://github.com/alphacep/vosk-api/tree/master/python/example)

[Unit](../README.md) · [Course index](../../../course/exercises-index.md).

</div>
