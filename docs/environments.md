# بيئات المشروع والتوافق

## القرارات المعتمدة

- بيئة المتدرب المستهدفة Raspberry Pi 4 مع Ubuntu 20.04 بنظام 64 بت.
- جهاز التطوير المتوفر Raspberry Pi 5. لم يُسجل نظامه الحالي بعد.
- دعم الجهازين يعني المحافظة على وظائف الدروس مع توثيق اختلاف الإعداد والمكتبات والتوصيل.
- لا تُعمم نتيجة الاختبار على جهاز إلى الجهاز الآخر.

## نظام التشغيل

تذكر [ملاحظات Ubuntu 20.04](https://documentation.ubuntu.com/release-notes/20.04/) دعم Pi 4. وتذكر [Canonical](https://canonical.com/blog/canonical-releases-ubuntu-23-10-mantic-minotaur) بدء دعم Pi 5 مع Ubuntu 23.10. لذلك لا نعتمد تثبيت Ubuntu 20.04 مباشرة على Pi 5.

اختيار نظام Pi 5 وطريقة تشغيل دروس ROS عليه قرار قادم. تشغيل بيئة قديمة داخل حاوية احتمال يحتاج تجربة، خصوصًا مع الصوت وGPIO، وليس مسارًا معتمدًا حاليًا.

## ROS

المقرر يتضمن Catkin. نجهز مسار ROS 1 متوافقًا مع المقرر، لكن تثبيت التوزيعة ونسخ الحزم وخطوات التشغيل يحتاج تحققًا قبل اعتماده. لا توجد حزم ROS منفذة في البنية الحالية.

## سجل التحقق

| الجزء | تحقق محلي | Pi 4 وUbuntu 20.04 | Pi 5 |
| --- | --- | --- | --- |
| أوامر نصية ولمبة افتراضية | يسجل في سجل التغييرات | لم يختبر | لم يختبر |
| الصوت العربي | لم ينفذ | لم يختبر | لم يختبر |
| GPIO | لم ينفذ | لم يختبر | لم يختبر |
| ROS والمحاكاة | لم ينفذ | لم يختبر | لم يختبر |

عند الاختبار نسجل الجهاز والنظام ومعمارية المعالج وإصدار Python وROS والمكتبات والأمر المستخدم والنتيجة.

## English

The learner target is Raspberry Pi 4 with 64 bit Ubuntu 20.04. The available development board is Pi 5; its installed OS still needs to be confirmed. Equivalent lesson behavior is the goal, with separate setup and GPIO instructions when necessary. Results on one board do not establish compatibility with the other.

[Ubuntu 20.04 release notes](https://documentation.ubuntu.com/release-notes/20.04/) describe Pi 4 support. [Canonical's Ubuntu 23.10 announcement](https://canonical.com/blog/canonical-releases-ubuntu-23-10-mantic-minotaur) describes the introduction of Pi 5 support. A native Ubuntu 20.04 installation is therefore not the Pi 5 path.

The Pi 5 OS and ROS setup remain open implementation decisions. A container for the older environment is a possibility requiring validation, especially for audio and GPIO; it is not an approved setup yet.

The course uses Catkin, so a ROS 1 learning path is planned. Distribution selection, dependency versions, and installation instructions require verification before adoption. No ROS package is implemented yet.

| Component | Local validation | Pi 4 with Ubuntu 20.04 | Pi 5 |
| --- | --- | --- | --- |
| Text commands and simulated lamp | See changelog | Pending | Pending |
| Arabic speech | Not implemented | Pending | Pending |
| GPIO | Not implemented | Pending | Pending |
| ROS and simulation | Not implemented | Pending | Pending |

Record the date, board, OS, CPU architecture, Python and ROS versions, dependency versions, command, and result for each validation.
