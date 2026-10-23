<div dir="rtl" lang="ar">

# سجلات التحقق وحدودها

## النتائج المحلية المثبتة

| الدليل | ما اختبر بالفعل |
| --- | --- |
| [ROS وGazebo](runs/2026-10-23-wsl-amd64.json) | اتصال المواضيع والخدمات، ومحادثة <span dir="ltr">AIML</span> وربطها بخرج افتراضي، وجسر شبكي، وحركة المتنقل وتوقفه |
| [الذراع بعد الضبط](runs/2026-10-23-arm-amd64.json) | وصول المفاصل الثلاثة والقابض إلى الأهداف في محاكاة فعلية دون واجهة رسومية |
| [برامج المتحكمات](runs/2026-10-23-firmware-builds.json) | تجميع <span dir="ltr">UNO R3</span> و<span dir="ltr">NUCLEO-F446RE</span> و<span dir="ltr">B-L475E-IOT01A</span>، دون رفع إلى لوحة |
| [اختبارات المنطق](../tests/README.md) | عشر حالات <span dir="ltr">Python</span>، وبروتوكول المتحكم بمضاعف واجهة على الحاسب |

بيئة <span dir="ltr">ROS</span> المحلية <span dir="ltr">WSL</span> و<span dir="ltr">Ubuntu 20.04</span> و<span dir="ltr">amd64</span> و<span dir="ltr">Noetic</span> و<span dir="ltr">Gazebo Classic 11.</span> استخدمت بيئة مثبتة مسبقا مع إضافة اعتماديات ناقصة إلى مجلد مستخدم للاختبار؛ لم ننفذ سكربت تثبيت النظام كاملا ولم نبن حاوية <span dir="ltr">Pi 5.</span> التقرير المجمع يحتفظ بفشل الذراع الأول وتصحيحه ولا يحوله إلى نجاح بلا دليل.

## ما لم يختبر بعد

<span dir="ltr">Pi 4</span> و<span dir="ltr">Pi 5</span> على أجهزة فعلية، و<span dir="ltr">GPIO</span> الحقيقي، واتصال <span dir="ltr">USB</span> أو <span dir="ltr">Wi-Fi</span> باللوحات، و<span dir="ltr">Odroid</span>، والميكروفون والسماعة ودقة التعرف العربي، وواجهات <span dir="ltr">RViz</span> و<span dir="ltr">Gazebo</span> التفاعلية. وجود الكود أو نجاح التجميع لا يثبت هذه النتائج. لا توجد صورة أو لقطة محاكاة مسجلة ضمن هذا التنفيذ؛ الأدلة الحالية قياسات ورسائل تشغيل.

## تسجيل تجربة جديدة

انسخ [قالب السجل](run-record.example.json) إلى ملف جديد، وحدد بند الخطة ورقم نسخة <span dir="ltr">Git</span> والجهاز والنظام والمعمارية والقطع وإصدارات المكتبات والأوامر، ثم أضف المتوقع والمشاهد ونتيجة كل خطوة. سجل الفشل أيضا. احذف بيانات الشبكة الخاصة وأسماء الأجهزة الشخصية من السجل المنشور.

استخدم [مصفوفة الجهازين](compatibility.md) لكل مسار اختبر فعلا. غير منطبق يتطلب سببا واضحا، ولا يستعمل بدل لم يختبر. أعد الاختبار عند تغيير السائق أو القطعة أو إعداد مؤثر.

راجع [إعادة تشغيل الاختبارات](../tests/README.md). أوامر <span dir="ltr">ROS</span> تحتاج بيئة <span dir="ltr">Noetic</span> مجهزة، وأوامر المتحكمات تحتاج <span dir="ltr">PlatformIO</span> بالإصدار الموضح في الأدلة.

</div>

<div dir="ltr" lang="en">

# Validation records and limits

## Observed local results

- [ROS/Gazebo combined evidence](runs/2026-10-23-wsl-amd64.json): topic/service communication, actual AIML and mock-device interaction, TCP device bridge, mobile motion and stopping.
- [Independent corrected arm run](runs/2026-10-23-arm-amd64.json): three joints and gripper reached commanded positions in real headless Gazebo simulation.
- [Firmware builds](runs/2026-10-23-firmware-builds.json): UNO R3, NUCLEO-F446RE and B-L475E-IOT01A compilation only; no flashing.
- [Portable tests](../tests/README.md): ten Python behavior checks and the C++ protocol tested with a minimal host interface double.

ROS tests ran on WSL Ubuntu 20.04 amd64, Noetic and Gazebo Classic 11. The existing installation was supplemented with user-cache controller/Python dependencies. Full native system installation scripts and the Pi 5 Docker build were not exercised. The combined report preserves the initial arm failure and points to the corrected independent run.

## Not physically validated

Neither Pi, real GPIO, USB/radio board connectivity, Odroid, microphone/speaker, Arabic recognition accuracy, nor interactive RViz/Gazebo GUIs were tested. Source/build success does not validate these. No simulation screenshot/video was captured; current evidence consists of runtime messages and measurements.

Copy the [record template](run-record.example.json) for each run. Record syllabus reference, Git revision, board/OS/architecture, components, library versions, commands, expected/observed outcomes and failures. Remove private network/device identity details before publishing. Update the [board matrix](compatibility.md) only for actual device runs. Not applicable needs a reason and must not replace untested. See [reproduction instructions](../tests/README.md).

</div>
