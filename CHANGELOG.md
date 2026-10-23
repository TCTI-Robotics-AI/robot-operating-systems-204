<div dir="rtl" lang="ar">

# سجل التغييرات

## إعادة تنظيم المقرر بتاريخ 2026-10-23

اعتماد ست وحدات، ومجلد مستقل لكل بند تفصيلي، وأربعة تمارين للأنظمة المدمجة. فصل التوسعات عن المنهج، ونقل كود اللمبة إلى تمرين الرازبيري، وإضافة فهرس يفرق بين التمرين والتقييم الأسبوعي. نجح فحص الروابط واللغتين وملفات الإعداد والتثبيت في بيئة نظيفة، وتشغيل التجربة من خارج مجلد المستودع. اختبارات أجهزة الرازبيري ما زالت غير منفذة. أقسام الإصدارات السابقة أدناه سجل تاريخي وقد استبدلت بنيتها بالتنظيم الحالي.

<span dir="ltr">Version 0.3.0</span>: ست وحدات مع الحفاظ على الشرح باللغتين واتجاه النص، وتحديث مسارات الحزمة والروابط وسجلات المضيف واللوحة.

<div dir="ltr" lang="en">

Version 0.3.0 organizes six course units with separate syllabus item directories and four embedded integration labs. It moves optional applications to extensions and the lamp code to the Pi lab, adds a detailed reference index, and distinguishes weekly assessments from exercises. Package paths, links, host and target records are updated. Local checks passed for links, language containers, configuration files, clean installation and demo execution outside the repository. Pi hardware runs remain pending. Earlier version entries below are historical and their layouts are superseded.

</div>


## 0.2.0 بتاريخ 2026-10-23

- اعتماد هوية أنظمة تشغيل الروبوتات 204 روبوت واسم المستودع <span dir="ltr">robot-operating-systems-204</span>.
- تقسيم المحتوى إلى 11 مجلد تمرين مستقل تحت <span dir="ltr">labs</span>، مع بقاء التحكم المنزلي بالصوت تطبيقًا تجميعيًا.
- نقل كود اللمبة الافتراضية إلى تمرين <span dir="ltr">GPIO</span> وتحديث مسار بناء حزمة <span dir="ltr">Python</span>.
- إضافة مسارات إعداد <span dir="ltr">Pi 4</span> و<span dir="ltr">Pi 5</span> للمدرب والمتدربين، وقوالب القطع والإعدادات وسجلات التحقق ومصفوفة التوافق.
- تحديث التوثيق العربي والإنجليزي وربط التمارين بخطة المقرر. اختبارات <span dir="ltr">Raspberry Pi</span> الفعلية ما زالت معلقة.
- نجاح تثبيت الحزمة المعاد تنظيمها في بيئة <span dir="ltr">Python</span> نظيفة وتشغيل أوامر التشغيل والإطفاء ورفض أمر مجهول من خارج مجلد المشروع، وفحص روابط الشرح وملفات <span dir="ltr">JSON</span> واعتماد صياغة <span dir="ltr">Python 3.8</span>.

</div>

<div dir="ltr" lang="en">

### English

Version 0.2.0 adopts the Robot Operating Systems course identity and repository name, organizes 11 independent labs, moves the simulated lamp source into its GPIO lab, and updates Python package discovery. Both boards are learner and instructor targets. Board environment examples, hardware inventory, validation records, and a compatibility matrix document actual settings and results. Arabic and English guides map labs to the course. A fresh package install and commands run outside the repository passed locally, including on, off, and unknown input checks. Documentation links, JSON examples, and Python 3.8 syntax were checked. Raspberry Pi hardware validation remains pending.

</div>

<div dir="rtl" lang="ar">

## 0.1.0 بتاريخ 2026-10-23

سجل تاريخي للنسخة الأولى؛ توزيع الأجهزة وهيكل الملفات استبدلا في 0.2.0. <span dir="ltr">Historical entry</span>: <span dir="ltr">the board roles and file layout below were superseded by 0.2.0</span>.

- إنشاء بنية المشروع والتوثيق العربي وربط الوحدات بخطة المقرر.
- إضافة تجربة أوامر نصية عربية لعرض حالة لمبة افتراضية دون مكتبات تشغيل خارجية.
- تخصيص مساحات لدروس <span dir="ltr">ROS</span> والمحاكاة والصوت والأجهزة والتكاملات.
- اعتماد <span dir="ltr">Pi 4</span> و<span dir="ltr">Ubuntu 20.04</span> كبيئة متدرب مستهدفة و<span dir="ltr">Pi 5</span> كجهاز تطوير يحتاج تحديد النظام.
- التحقق محليًا على <span dir="ltr">Windows</span> من تشغيل أوامر التشغيل والإطفاء ورفض أمر غير معروف، ومن روابط التوثيق وصلاحية صياغة الكود لـ<span dir="ltr">Python 3.8</span>. لم يختبر التثبيت على <span dir="ltr">Python 3.8</span> أو التشغيل على أجهزة <span dir="ltr">Raspberry Pi</span> بعد.
- إضافة دليل إنجليزي وأقسام إنجليزية للشروحات وقوالب المساهمة.
- نجاح التثبيت في بيئة <span dir="ltr">Python</span> محلية جديدة على <span dir="ltr">Windows</span>.

</div>

<div dir="ltr" lang="en">

## English

Version 0.1.0, dated 2026-10-23, adds the repository structure, course mapping, Arabic and English documentation, contribution templates, and a text command demo with a simulated lamp. Directories are reserved for future ROS, simulation, speech, hardware, and optional integrations.

The learner target is Pi 4 with Ubuntu 20.04. The development board is Pi 5, with its OS still to be confirmed. Local Windows checks verified installation in a fresh Python environment, on and off commands, rejection of an unknown command, documentation links, and Python 3.8 syntax compatibility. Installation on Python 3.8 and execution on Raspberry Pi hardware have not been validated.

</div>
