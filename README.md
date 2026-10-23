<div dir="rtl" lang="ar">

# أنظمة تشغيل الروبوتات

**رمز المقرر: 204 روبوت** · <span dir="ltr">Robot Operating Systems</span> · [<span dir="ltr">English</span>](README.en.md)

مستودع المقرر التعليمي، يجمع تمارين <span dir="ltr">Linux</span> و<span dir="ltr">ROS</span> والمحاكاة والصوت والمحادثة والتحكم بالأنظمة المدمجة. لكل تمرين شرح ومتطلبات وإعدادات ونتائج تحقق مستقلة بالعربية والإنجليزية. التحكم المنزلي بالصوت و<span dir="ltr">WhatsApp</span> تطبيقات ضمن المقرر وتوسعاته.

## البداية

1. راجع [خريطة المقرر](docs/course-map.md) و[فهرس التمارين](labs/README.md).
2. حدد جهازك من [دليل البيئات](environments/README.md).
3. راجع [قائمة القطع والتوصيل](hardware/README.md).
4. نفذ التمرين وسجل النتيجة حسب [دليل التحقق](validation/README.md).

المتوفر الآن هو [التحكم النصي بلمبة افتراضية](labs/07-gpio-control/01-text-lamp/README.md). بقية مجلدات التمارين تحدد النطاق المطلوب، وليست تطبيقات مكتملة.

## الأجهزة والتوافق

<span dir="ltr">Pi 4</span> و<span dir="ltr">Pi 5</span> جهازان مستهدفان للمدرب والمتدربين. تختلف خطوات النظام والصوت و<span dir="ltr">GPIO</span> عند الحاجة، بينما يبقى الهدف التعليمي واحدًا.

| الجهاز | مسار النظام | اختبارات المشروع |
| --- | --- | --- |
| <span dir="ltr">Raspberry Pi 4</span> | <span dir="ltr">Ubuntu 20.04</span> بنظام 64 بت لمواءمة المنهج | لم يختبر على الجهاز |
| <span dir="ltr">Raspberry Pi 5</span> | <span dir="ltr">Ubuntu 24.04</span> بنظام 64 بت كمسار مقترح مدعوم للجهاز | لم يختبر على الجهاز |

<span dir="ltr">Ubuntu 20.04</span> ليس مسار تثبيت مباشر مدعومًا على <span dir="ltr">Pi 5</span>. توفر نظام مدعوم للجهاز لا يثبت توافق <span dir="ltr">ROS</span> أو المايك أو <span dir="ltr">GPIO</span>؛ توثق النتائج لكل تمرين على حدة. [التفاصيل والمصادر](docs/environments.md).

## تنظيم المستودع

<div dir="ltr">

```text
labs/
  01-linux-and-setup/
  02-ros-fundamentals/
  03-mobile-robot-simulation/
  04-robot-arm-simulation/
  05-arabic-speech/
  06-conversation/
  07-gpio-control/
  08-embedded-interfaces/
  09-ai-models/
  10-whatsapp/
  11-voice-home-automation/
environments/
hardware/
validation/
docs/
references/
.github/
```

</div>

الكود الحالي داخل تمرين <span dir="ltr">GPIO</span>. ملفات وحزم <span dir="ltr">ROS</span> وإعدادات المحاكاة لأي تمرين جديد توضع داخل مجلده. تستخرج المكونات المشتركة عند وجود حاجة فعلية.

## تجربة أولى دون أجهزة

من جذر المستودع على <span dir="ltr">Linux</span>، باستخدام <span dir="ltr">Python 3.8</span> أو أحدث:

<div dir="ltr">

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m arabic_home --command "شغل اللمبة"
python -m arabic_home --command "طفي اللمبة"
```

</div>

يعرض المثال حالة لمبة افتراضية دون استخدام الصوت أو <span dir="ltr">GPIO</span> أو <span dir="ltr">ROS</span>. كل تشغيل مستقل ولا يحفظ الحالة.

## التطوير والمساهمة

راجع [خطة التنفيذ](docs/roadmap.md) و[دليل المساهمة](CONTRIBUTING.md). لا يوصف تمرين بأنه متوافق مع الجهازين قبل تسجيل اختبار فعلي لكل منهما. التوثيق العربي والإنجليزي وبيانات القطع والإعدادات والإصدارات جزء من كل تمرين.

لم يحدد ترخيص إعادة الاستخدام بعد. ملف توصيف المقرر الأصلي محفوظ محليًا خارج <span dir="ltr">Git</span> لاحتوائه على بيانات تواصل.

</div>
