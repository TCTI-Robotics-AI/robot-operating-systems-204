<div dir="rtl" lang="ar">

# التحكم النصي بلمبة افتراضية

## الهدف

فهم تحويل العبارة العربية إلى طلب محدد قبل إضافة الصوت أو الأجهزة. تجربة تمهيدية لتطبيق <span dir="ltr">Raspberry Pi</span> في الأسبوع 15 ولمسار المحادثة في الأسابيع 11 إلى 13.

## المتطلبات

<span dir="ltr">Python 3.8</span> أو أحدث. لا تحتاج <span dir="ltr">Raspberry Pi</span> أو مايك أو <span dir="ltr">ROS</span> لهذه التجربة.

## القطع وإعداد الجهازين

هذه تجربة برمجية فقط؛ لا تحتاج توصيلًا أو <span dir="ltr">GPIO</span> أو مايكًا أو خدمة خارجية. على <span dir="ltr">Pi 4</span> اتبع [مسار <span dir="ltr">Ubuntu 20.04</span>](../../../environments/pi4-ubuntu2004/README.md)، وعلى <span dir="ltr">Pi 5</span> اتبع [مسار <span dir="ltr">Ubuntu 24.04</span> المقترح](../../../environments/pi5-ubuntu2404/README.md). أوامر <span dir="ltr">Python</span> نفسها بعد تجهيز البيئة، ولا توجد إعدادات صوت أو أطراف لهذه المرحلة.

ابدأ التثبيت والتشغيل من جذر المستودع وفق [الدليل الرئيسي](../../../README.md). كود التجربة في <code dir="ltr">labs/07-gpio-control/src/arabic_home/</code>. حالة الجهازين مستهدفة وغير مختبرة؛ التحقق المحلي على <span dir="ltr">Windows</span> فقط. سجل أي اختبار فعلي في [مصفوفة التوافق](../../../validation/compatibility.md).

## التشغيل

بعد إعداد المشروع حسب الدليل الرئيسي:

<div dir="ltr">

```bash
python -m arabic_home --command "شغّل اللمبة"
python -m arabic_home --command "طفّي اللمبة"
python -m arabic_home --command "افتح الباب"
```

</div>

## النتيجة المتوقعة

الأمر الأول يعرض «اللمبة الافتراضية: تعمل»، والثاني «اللمبة الافتراضية: مطفأة». الثالث يعرض رسالة بأن الأمر غير معروف ويعيد رمز خروج 2. لا يتحكم المثال بأي جهاز، ولا يحفظ الحالة بين التشغيلات.

البرنامج يزيل التشكيل ويطابق عبارات محددة؛ ليس نموذج فهم لغة عامًّا. العبارات الموجودة في قاموس الأوامر فقط هي المدعومة.

## المشاكل الشائعة

- رسالة <span dir="ltr">No module named arabic_home</span> تعني الحاجة لتفعيل البيئة وتثبيت المشروع باستخدام <code dir="ltr">python -m pip install -e .</code> من مجلده الرئيسي.
- عند عدم قبول عبارة، راجع العبارات المعرفة في <code dir="ltr">labs/07-gpio-control/src/arabic_home/__main__.py</code>.

## تمرين

أضف عبارة «أشعل اللمبة» إلى قاموس الأوامر، ثم تأكد من أن أمرًا غير معروف لا يتحول إلى طلب تشغيل.

</div>

<div dir="ltr" lang="en">

## English

### Objective and prerequisites

Learn how an Arabic phrase becomes an explicit request before adding speech or physical devices. This introductory exercise prepares for weeks 11 to 13 on conversation and week 15 on Raspberry Pi. It requires Python 3.8 or newer; no Pi, microphone, or ROS is needed.

### Run

This is a software only exercise: no wiring, GPIO, microphone, or external service. Use the linked Pi 4 Ubuntu 20.04 or proposed Pi 5 Ubuntu 24.04 profile, then run the same Python commands from the repository root. No board specific audio or pin settings apply. Both hardware runs are pending; only Windows checks exist. Record real board results in the linked matrix. The source is under `labs/07-gpio-control/src/arabic_home/`.

Install the project using the main README, then run:

```bash
python -m arabic_home --command "شغّل اللمبة"
python -m arabic_home --command "طفّي اللمبة"
python -m arabic_home --command "افتح الباب"
```

The phrases mean “turn on the lamp,” “turn off the lamp,” and “open the door.” The first prints “اللمبة الافتراضية: تعمل” (simulated lamp: on). The second prints “اللمبة الافتراضية: مطفأة” (simulated lamp: off). The third reports an unknown command and exits with code 2. Each invocation is independent; no state is persisted and no hardware is accessed.

The program removes Arabic diacritics and matches an explicit phrase dictionary. It is not a general language understanding model.

### Troubleshooting and exercise

For `No module named arabic_home`, activate the virtual environment and run `python -m pip install -e .` from the repository root. For an unsupported phrase, inspect the command dictionary in `labs/07-gpio-control/src/arabic_home/__main__.py`.

Add “أشعل اللمبة” (light the lamp) to the dictionary. Verify that an unrelated phrase still does not produce a switching request.

</div>
