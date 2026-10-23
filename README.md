<div dir="rtl" lang="ar">

# أنظمة تشغيل الروبوتات

**رمز المقرر: 204 روبوت** · <span dir="ltr">Robot Operating Systems</span> · [English](README.en.md)

مستودع المقرر التعليمي. تنتظم مادته في ست وحدات، وتحت كل وحدة مجلدات مستقلة للبنود والتمارين المذكورة في الخطة. لكل تمرين شرح عربي وإنجليزي ومتطلبات وقطع وإعدادات ونتائج تحقق. التوسعات الإضافية لها فهرس مستقل.

## المحتوى التعليمي

تتوفر [عروض المقرر الأسبوعية](PPT/README.md) بصيغة <span dir="ltr">PDF</span>، موزعة على ١٦ أسبوعًا. استخدمها للشرح والمراجعة إلى جانب أدلة التمارين العملية.

## ابدأ هنا

1. راجع [خريطة المقرر](course/syllabus-map.md) و[الفهرس التفصيلي للبنود والتمارين](course/exercises-index.md).
2. اختر الوحدة من [فهرس الوحدات](labs/README.md)، ثم التمرين حسب مرجع الخطة.
3. حدد جهازك ونظامه من [دليل البيئات](environments/README.md)، وراجع [القطع والتوصيل](hardware/README.md).
4. نفذ التمرين ثم سجل النتيجة في [التحقق](validation/README.md).

هناك أربعة تمارين ربط للأنظمة المدمجة: أردوينو، ومتحكمات <span dir="ltr">STM32</span>، والرازبيري، و<span dir="ltr">Odroid</span>. عدد التقييمات الأسبوعية لا يساوي عدد التمارين التفصيلية.

## بنية المستودع

<div dir="ltr">

```text
course/
  syllabus-map.md
  exercises-index.md
PPT/
  README.md
  WK01.pdf ... WK16.pdf
labs/
  01-ros-fundamentals/
  02-installation-and-setup/
  03-mobile-robot-simulation/
  04-robot-arm-simulation/
  05-conversation-and-speech/
  06-embedded-systems/
    01-arduino/
    02-stm32/
    03-raspberry-pi/
    04-odroid/
extensions/
  ai-models/
  whatsapp/
  voice-home-automation/
environments/
hardware/
validation/
docs/
references/
```

</div>

## المتوفر الآن

[التجربة النصية للمبة الافتراضية](labs/06-embedded-systems/03-raspberry-pi/01-text-lamp/README.md) متوفرة كمرحلة تمهيدية ضمن تمرين الرازبيري. لا تنفذ ربطًا فعليًا مع الأجهزة أو نظام <span dir="ltr">ROS</span>. بقية الأدلة تحدد النطاق والمتطلبات، وليست تجارب منفذة.

من جذر المستودع على لينكس، باستخدام <span dir="ltr">Python 3.8</span> أو أحدث:

<div dir="ltr">

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m arabic_home --command "شغل اللمبة"
python -m arabic_home --command "طفي اللمبة"
```

</div>

## مسار الجهازين

| الجهاز | مسار النظام | حالة تحقق المشروع |
| --- | --- | --- |
| <span dir="ltr">Pi 4</span> | <span dir="ltr">Ubuntu 20.04 arm64</span> لمواءمة المنهج | لم يختبر على الجهاز |
| <span dir="ltr">Pi 5</span> | <span dir="ltr">Ubuntu 24.04 arm64</span> كمسار مقترح | لم يختبر على الجهاز |

يستهدف الرازبيري الجهازين. عند استخدام أي منهما مضيفًا لتمرين لوحة أخرى، توثق إعدادات المضيف واللوحة المتصلة بشكل مستقل. دعم النظام لا يثبت توافق الصوت أو <span dir="ltr">GPIO</span> أو <span dir="ltr">ROS</span>. [التفاصيل والمصادر](docs/environments.md).

## العمل والمساهمة

راجع [تصميم المستودع](docs/architecture.md) و[خطة التنفيذ](docs/roadmap.md) و[دليل المساهمة](CONTRIBUTING.md). استخدم [قالب التمرين](docs/lesson-template.md) و[دليل اتجاه النص](docs/writing-style.md). المستودع عام ومتاح للجميع للاطلاع على المحتوى التعليمي. يحدد صاحب المقرر ترخيص إعادة الاستخدام. ملف المنهج الأصلي محفوظ محليًا خارج المستودع لبيانات التواصل التي يحتويها.

</div>
