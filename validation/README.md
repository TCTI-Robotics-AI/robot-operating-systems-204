<div dir="rtl" lang="ar">

# سجلات التحقق وحدودها

اعتمد المستخدم [إكمال مرحلة المساعد الصوتي على الرازبيري 5](../extensions/voice-home-automation/completion.md) بتاريخ 25 أكتوبر 2026 للوظائف المحددة في المحضر. الاستماع متوقف واللمبة مطفأة عند التسليم. تبقى حدود التحقق لكل جهاز وتمرين كما توضح السجلات.

## النتائج المحلية المثبتة

| الدليل | ما اختبر بالفعل |
| --- | --- |
| [ربط اللمبة على جهاز Pi 5 فعلي](runs/2026-10-24-pi5-device-setup.json) | بناء الحاوية الخفيفة وتشغيلها وربطها بوكيل افتراضي على النظام الأصلي، ونجاح التشغيل والإطفاء في هذا الاختبار الأولي |
| [قياس GPIO](runs/2026-10-24-pi5-gpio-meter.json) و[المؤشر الفعلي](runs/2026-10-24-pi5-led.json) | أكد المستخدم قياس نحو <span dir="ltr">3.3 V / 0 V</span> وإضاءة المؤشر وإطفاءه |
| [سماعة أبل وتحويل النص](runs/2026-10-24-pi5-earpods-speech.json) | التعرف على عبارتي التشغيل والإطفاء، مع حفظ فشل الاسم قبل إضافة المفردة المساعدة |
| [الصوت إلى ROS والمؤشر الفعلي](runs/2026-10-24-pi5-earpods-voice-led.json) | تسجيلان جديدان، واستماع قبل التحويل، وتشغيل وإطفاء عبر الخدمة؛ أكد المستخدم الحالتين |
| [الرد الصوتي عبر سماعة أبل](runs/2026-10-24-pi5-earpods-spoken-replies.json) | إعادة معالجة التسجيلين السابقين، ورد عربي بعد تأكيد كل أمر؛ أكد المستخدم سماع الردين ووضوحهما ومشاهدة التشغيل والإطفاء |
| [نداء يا مساعد](runs/2026-10-24-pi5-wake-assistant.json) | استماع في حالة الجاهزية، ورد تفضل، والتقاط أمر جديد ثم تنفيذه والرد؛ أكد المستخدم الحالتين وتجاهل أمر دون نداء |
| [التاريخ وحرارة جدة](runs/2026-10-25-pi5-date-weather.json) | نجح السؤالان بصوت جديد بعد النداء، وجلب الطقس وتوليد الرد محليا؛ أكد المستخدم سماع الردين. حفظ فشل التعرف الأول على سؤال الحرارة وإعادة المحاولة الناجحة |
| [ROS وGazebo](runs/2026-10-23-wsl-amd64.json) | اتصال المواضيع والخدمات، ومحادثة <span dir="ltr">AIML</span> وربطها بخرج افتراضي، وجسر شبكي، وحركة المتنقل وتوقفه |
| [الذراع بعد الضبط](runs/2026-10-23-arm-amd64.json) | وصول المفاصل الثلاثة والقابض إلى الأهداف في محاكاة فعلية دون واجهة رسومية |
| [برامج المتحكمات](runs/2026-10-23-firmware-builds.json) | تجميع <span dir="ltr">UNO R3</span> و<span dir="ltr">NUCLEO-F446RE</span> و<span dir="ltr">B-L475E-IOT01A</span>، دون رفع إلى لوحة |
| [اختبارات المنطق](../tests/README.md) | <span dir="ltr">37</span> حالة <span dir="ltr">Python</span> تشمل النداء والرد والتاريخ والطقس، وبروتوكول المتحكم بمضاعف واجهة على الحاسب |

اختبارات المحاكاة بتاريخ 2026-10-23 استخدمت <span dir="ltr">WSL، Ubuntu 20.04، amd64، Noetic، Gazebo Classic 11</span> وبيئة مثبتة مسبقا مع إضافة اعتماديات ناقصة إلى مجلد مستخدم؛ لم ينفذ سكربت تثبيت النظام كاملا. بنيت لاحقا حاوية الجهاز الخفيفة على <span dir="ltr">Pi 5</span> فعلي. يحتفظ التقرير المجمع بفشل الذراع الأول وتصحيحه.

## ما لم يختبر بعد

نجح بتاريخ 2026-10-24 مسار الحاوية الخفيفة على <span dir="ltr">Pi 5 / Ubuntu 24.04.5 arm64</span>، ثم قياس الخرج وإضاءة المؤشر والتحكم به من تسجيلين صوتيين. لم تختبر الحاوية الكاملة التي تتضمن المحاكاة على الرازبيري. تخص ملاحظات الغياب في سجلات 2026-10-23 وقت تلك السجلات.

ما يزال غير مختبر: جهاز <span dir="ltr">Pi 4</span> فعلي، واتصال <span dir="ltr">USB / Wi-Fi</span> بالمتحكمات، و<span dir="ltr">Odroid</span>، وواجهات <span dir="ltr">RViz / Gazebo</span> التفاعلية، ودقة التعرف العربي العامة واستمرارية إعداد الصوت بعد إعادة التشغيل. نجاح تجربتي سماعة أبل لا يثبت دقة اللهجات أو الميكروفونات الأخرى. وجود الكود أو نجاح التجميع لا يثبت هذه النتائج.

## تسجيل تجربة جديدة

انسخ [قالب السجل](run-record.example.json) إلى ملف جديد، وحدد بند الخطة ورقم نسخة <span dir="ltr">Git</span> والجهاز والنظام والمعمارية والقطع وإصدارات المكتبات والأوامر، ثم أضف المتوقع والمشاهد ونتيجة كل خطوة. سجل الفشل أيضا. احذف بيانات الشبكة الخاصة وأسماء الأجهزة الشخصية من السجل المنشور.

استخدم [مصفوفة الجهازين](compatibility.md) لكل مسار اختبر فعلا. غير منطبق يتطلب سببا واضحا، ولا يستعمل بدل لم يختبر. أعد الاختبار عند تغيير السائق أو القطعة أو إعداد مؤثر.

راجع [إعادة تشغيل الاختبارات](../tests/README.md). أوامر <span dir="ltr">ROS</span> تحتاج بيئة <span dir="ltr">Noetic</span> مجهزة، وأوامر المتحكمات تحتاج <span dir="ltr">PlatformIO</span> بالإصدار الموضح في الأدلة.

</div>

<div dir="ltr" lang="en">

# Validation records and limits

## Observed local results

- [Real Pi 5 software bridge](runs/2026-10-24-pi5-device-setup.json): lightweight image built and run on Ubuntu 24.04.5 arm64; native mock-agent ON/OFF requests and ROS state topics passed in this initial run.
- [GPIO meter](runs/2026-10-24-pi5-gpio-meter.json) and [physical LED](runs/2026-10-24-pi5-led.json): user-confirmed approximately 3.3/0 V and observed LED transitions.
- [EarPods transcription](runs/2026-10-24-pi5-earpods-speech.json) and [voice-to-ROS LED trials](runs/2026-10-24-pi5-earpods-voice-led.json): two fresh recordings, playback before inference, and user-confirmed physical ON/OFF. Baseline transcription failures remain recorded.
- [Arabic spoken replies](runs/2026-10-24-pi5-earpods-spoken-replies.json): the previous speech files were replayed, each successful physical ROS request was followed by its matching reply through the EarPods, and the user confirmed clear speech and LED transitions.
- [Arabic wake assistant](runs/2026-10-24-pi5-wake-assistant.json): idle listening, wake/readiness, fresh command capture, ROS control and reply; user confirmed both cycles and reported ignoring a bare command. General wake accuracy remains unmeasured.
- [Date and Jeddah weather](runs/2026-10-25-pi5-date-weather.json): both fresh questions passed after wake, with live weather fetching, dynamic local speech and user-confirmed hearing. The initial rejected weather transcript and successful vocabulary-context retry are preserved.
- [ROS/Gazebo combined evidence](runs/2026-10-23-wsl-amd64.json): topic/service communication, actual AIML and mock-device interaction, TCP device bridge, mobile motion and stopping.
- [Independent corrected arm run](runs/2026-10-23-arm-amd64.json): three joints and gripper reached commanded positions in real headless Gazebo simulation.
- [Firmware builds](runs/2026-10-23-firmware-builds.json): UNO R3, NUCLEO-F446RE and B-L475E-IOT01A compilation only; no flashing.
- [Portable tests](../tests/README.md): 37 Python behavior checks, including wake gating, date/weather failure handling and spoken-reply ordering, and the C++ protocol tested with a minimal host interface double.

The 2026-10-23 ROS simulation tests ran on WSL Ubuntu 20.04 amd64, Noetic and Gazebo Classic 11. The existing installation was supplemented with user-cache dependencies; full native installation scripts were not exercised. The lightweight device container was subsequently built on a real Pi 5. The combined report preserves the initial arm failure and corrected run.

## Not physically validated

The 2026-10-24 Pi 5 measurements and voice-controlled LED observations supersede the earlier pending hardware checks. The full Gazebo image on Pi, physical Pi 4, USB/radio microcontroller connectivity, Odroid, interactive RViz/Gazebo GUIs, audio-profile reboot persistence and general Arabic recognition accuracy remain untested. Two successful EarPods command trials do not establish dialect or other-microphone accuracy. Source/build success does not validate these remaining paths.

Copy the [record template](run-record.example.json) for each run. Record syllabus reference, Git revision, board/OS/architecture, components, library versions, commands, expected/observed outcomes and failures. Remove private network/device identity details before publishing. Update the [board matrix](compatibility.md) only for actual device runs. Not applicable needs a reason and must not replace untested. See [reproduction instructions](../tests/README.md).

</div>
