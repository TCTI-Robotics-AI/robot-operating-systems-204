# التحكم النصي بلمبة افتراضية

## الهدف

فهم تحويل العبارة العربية إلى طلب محدد قبل إضافة الصوت أو الأجهزة. تجربة تمهيدية لتطبيق Raspberry Pi في الأسبوع 15 ولمسار المحادثة في الأسابيع 11 إلى 13.

## المتطلبات

Python 3.8 أو أحدث. لا تحتاج Raspberry Pi أو مايك أو ROS لهذه التجربة.

## التشغيل

بعد إعداد المشروع حسب الدليل الرئيسي:

```bash
python -m arabic_home --command "شغّل اللمبة"
python -m arabic_home --command "طفّي اللمبة"
python -m arabic_home --command "افتح الباب"
```

## النتيجة المتوقعة

الأمر الأول يعرض «اللمبة الافتراضية: تعمل»، والثاني «اللمبة الافتراضية: مطفأة». الثالث يعرض رسالة بأن الأمر غير معروف ويعيد رمز خروج 2. لا يتحكم المثال بأي جهاز، ولا يحفظ الحالة بين التشغيلات.

البرنامج يزيل التشكيل ويطابق عبارات محددة؛ ليس نموذج فهم لغة عامًّا. العبارات الموجودة في قاموس الأوامر فقط هي المدعومة.

## المشاكل الشائعة

- رسالة No module named arabic_home تعني الحاجة لتفعيل البيئة وتثبيت المشروع باستخدام `python -m pip install -e .` من مجلده الرئيسي.
- عند عدم قبول عبارة، راجع العبارات المعرفة في `src/arabic_home/__main__.py`.

## تمرين

أضف عبارة «أشعل اللمبة» إلى قاموس الأوامر، ثم تأكد من أن أمرًا غير معروف لا يتحول إلى طلب تشغيل.

## English

### Objective and prerequisites

Learn how an Arabic phrase becomes an explicit request before adding speech or physical devices. This introductory exercise prepares for weeks 11 to 13 on conversation and week 15 on Raspberry Pi. It requires Python 3.8 or newer; no Pi, microphone, or ROS is needed.

### Run

Install the project using the main README, then run:

```bash
python -m arabic_home --command "شغّل اللمبة"
python -m arabic_home --command "طفّي اللمبة"
python -m arabic_home --command "افتح الباب"
```

The phrases mean “turn on the lamp,” “turn off the lamp,” and “open the door.” The first prints “اللمبة الافتراضية: تعمل” (simulated lamp: on). The second prints “اللمبة الافتراضية: مطفأة” (simulated lamp: off). The third reports an unknown command and exits with code 2. Each invocation is independent; no state is persisted and no hardware is accessed.

The program removes Arabic diacritics and matches an explicit phrase dictionary. It is not a general language understanding model.

### Troubleshooting and exercise

For `No module named arabic_home`, activate the virtual environment and run `python -m pip install -e .` from the repository root. For an unsupported phrase, inspect the command dictionary in `src/arabic_home/__main__.py`.

Add “أشعل اللمبة” (light the lamp) to the dictionary. Verify that an unrelated phrase still does not produce a switching request.
