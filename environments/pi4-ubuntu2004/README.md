# إعداد Raspberry Pi 4

المسار المستهدف: Ubuntu 20.04 arm64 لمواءمة المقرر. لم يتم تشغيل تجارب المشروع على الجهاز.

1. تحقق من موديل اللوحة والنظام ومعمارية 64 بت قبل تثبيت المتطلبات.
2. للتجربة النصية اتبع البيئة الافتراضية في الدليل الرئيسي؛ لا تحتاج ROS أو صوتًا أو GPIO.
3. للتجربة الفعلية سجل [القطع](../../hardware/README.md)، ثم حدد المكتبات والتوصيل داخل التمرين.
4. أكمل [مثال الإعداد](environment.example.json) محليًا. الملف وصف للبيئة وليس إعدادًا يقرأه البرنامج الحالي.
5. سجل التشغيل في [التحقق](../../validation/README.md). مسار ROS 1 يحتاج توثيق تثبيت مستقل والتحقق من توفر الحزم.

## English

Target: arm64 Ubuntu 20.04 for course alignment. Hardware validation is pending. Confirm board, OS, and architecture. The text demo needs only the root README's virtual environment setup. Physical labs must identify actual parts, libraries, and wiring. Complete the linked JSON example locally; the current code does not load it. Record runs using the validation guide. The legacy ROS 1 path needs verified installation instructions and package availability.
