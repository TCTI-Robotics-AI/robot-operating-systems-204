# سجل التغييرات

## 0.2.0 بتاريخ 2026-10-23

- اعتماد هوية أنظمة تشغيل الروبوتات 204 روبوت واسم المستودع robot-operating-systems-204.
- تقسيم المحتوى إلى 11 مجلد تمرين مستقل تحت labs، مع بقاء التحكم المنزلي بالصوت تطبيقًا تجميعيًا.
- نقل كود اللمبة الافتراضية إلى تمرين GPIO وتحديث مسار بناء حزمة Python.
- إضافة مسارات إعداد Pi 4 وPi 5 للمدرب والمتدربين، وقوالب القطع والإعدادات وسجلات التحقق ومصفوفة التوافق.
- تحديث التوثيق العربي والإنجليزي وربط التمارين بخطة المقرر. اختبارات Raspberry Pi الفعلية ما زالت معلقة.
- نجاح تثبيت الحزمة المعاد تنظيمها في بيئة Python نظيفة وتشغيل أوامر التشغيل والإطفاء ورفض أمر مجهول من خارج مجلد المشروع، وفحص روابط الشرح وملفات JSON واعتماد صياغة Python 3.8.

### English

Version 0.2.0 adopts the Robot Operating Systems course identity and repository name, organizes 11 independent labs, moves the simulated lamp source into its GPIO lab, and updates Python package discovery. Both boards are learner and instructor targets. Board environment examples, hardware inventory, validation records, and a compatibility matrix document actual settings and results. Arabic and English guides map labs to the course. A fresh package install and commands run outside the repository passed locally, including on, off, and unknown input checks. Documentation links, JSON examples, and Python 3.8 syntax were checked. Raspberry Pi hardware validation remains pending.

## 0.1.0 بتاريخ 2026-10-23

سجل تاريخي للنسخة الأولى؛ توزيع الأجهزة وهيكل الملفات استبدلا في 0.2.0. Historical entry: the board roles and file layout below were superseded by 0.2.0.

- إنشاء بنية المشروع والتوثيق العربي وربط الوحدات بخطة المقرر.
- إضافة تجربة أوامر نصية عربية لعرض حالة لمبة افتراضية دون مكتبات تشغيل خارجية.
- تخصيص مساحات لدروس ROS والمحاكاة والصوت والأجهزة والتكاملات.
- اعتماد Pi 4 وUbuntu 20.04 كبيئة متدرب مستهدفة وPi 5 كجهاز تطوير يحتاج تحديد النظام.
- التحقق محليًا على Windows من تشغيل أوامر التشغيل والإطفاء ورفض أمر غير معروف، ومن روابط التوثيق وصلاحية صياغة الكود لـPython 3.8. لم يختبر التثبيت على Python 3.8 أو التشغيل على أجهزة Raspberry Pi بعد.
- إضافة دليل إنجليزي وأقسام إنجليزية للشروحات وقوالب المساهمة.
- نجاح التثبيت في بيئة Python محلية جديدة على Windows.

## English

Version 0.1.0, dated 2026-10-23, adds the repository structure, course mapping, Arabic and English documentation, contribution templates, and a text command demo with a simulated lamp. Directories are reserved for future ROS, simulation, speech, hardware, and optional integrations.

The learner target is Pi 4 with Ubuntu 20.04. The development board is Pi 5, with its OS still to be confirmed. Local Windows checks verified installation in a fresh Python environment, on and off commands, rejection of an unknown command, documentation links, and Python 3.8 syntax compatibility. Installation on Python 3.8 and execution on Raspberry Pi hardware have not been validated.
