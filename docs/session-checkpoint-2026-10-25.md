<div dir="rtl" lang="ar">

# متابعة 25 أكتوبر 2026

**الحالة النهائية: مكتمل باعتماد المستخدم. الاستماع متوقف واللمبة مطفأة.** راجع [محضر التسليم](../extensions/voice-home-automation/completion.md). طلب المستخدم في ختام الجلسة «انتهينا» ثم «وثق ويعتبر مكتمل»؛ أوقف المساعد وتحقق غياب التسجيل الجاري، ونجح أمر إطفاء ROS وأكد الوكيل الحقيقي الحالة. الفقرات التالية تسجل مراحل الجلسة تاريخيا، ولا تعني أن الاستماع ما زال نشطا.

استؤنف العمل بطلب المستخدم، مع عرض الأوامر في المتصفح على شاشة الحاسب هذه المرة. اتصال الرازبيري وسماعة أبل يعملان. حدد المستخدم **جدة** لبيانات الطقس.

أضيف [دليل التاريخ والطقس](../extensions/voice-home-automation/date-weather.md)، وملف إعداد المدينة، ووحدة مطابقة الأسئلة والتحقق من البيانات، وتوليد الرد العربي المتغير محليا. التاريخ ميلادي بتوقيت السعودية من ساعة الجهاز المتزامنة؛ الحرارة الحالية للمدينة من Open-Meteo. لا يرسل الصوت للخدمة. أخطاء الشبكة أو القراءة القديمة لا تنتج رقما تخمينيا.

اجتازت الاختبارات المحلية السبع والثلاثون، واختبارات المعلومات السبعة على الرازبيري. شغل رد التاريخ ثم رد حرارة جدة عبر سماعة أبل وأكد المستخدم سماعهما. نجح بعد ذلك النداء المباشر «يا مساعد» ثم «كم التاريخ اليوم؟» والرد الصوتي؛ أكد المستخدم سماع التاريخ. حالة تجربة الطقس الصوتية الأحدث محفوظة في [سجل التحقق](../validation/runs/2026-10-25-pi5-date-weather.json).

نجح أيضا سؤال «كم درجة الحرارة اليوم» بعد توسيع سياق مفردات التعرف إلى السؤال الكامل؛ أكد المستخدم سماع الرد. حفظت المحاولة الأولى التي خرجت «الحرار» ورفضت دون إضافة مرادف خاطئ. أنهت تجربتا السؤال دورة واحدة لكل اختبار؛ الاستماع متوقف واللمبة مطفأة عند إنهاء العمل. تبقى الطرفية المباشرة ظاهرة للمراجعة. لإعادة الاستماع استخدم أمر الدليل بعد إبلاغ المستخدم؛ يلزم إعادة فتح العرض المحلي إن توقفت خدمته.

المصدر موجود في المشروع المحلي وعلى الرازبيري. لم ينشر تحديث GitHub في هذه الجلسة. لا تلمس تغييرات الموقع المتزامنة في docs/index.html وdocs/sitemap.txt. اتبع أوامر الدليل الجديد عند إعادة التشغيل، وأبلغ المستخدم قبل الميكروفون أو تشغيل رد اختباري. تسجيل السؤال خمس ثوان. لا توجد خدمة تشغيل تلقائي مضافة.

</div>

<div dir="ltr" lang="en">

## English handoff

**Final state: COMPLETE and accepted by the user; listening stopped and LED OFF.** The [completion record](../extensions/voice-home-automation/completion.md) is the delivery reference. Final checks found no assistant/capture process; ROS and the physical device agent both acknowledged OFF. The subsequent resume notes below are session history, not the current listening state.

The user resumed date/weather work and requested commands on the laptop screen. A localhost browser view mirrors the Pi's `course204:voice` tmux pane. Jeddah was explicitly selected. New exact information intents are separate from physical ROS actions; date is Gregorian at UTC+03:00, current city temperature uses Open-Meteo with timeout, units and freshness checks, and dynamic replies use local Piper in an isolated short-lived worker. Existing wake/readiness/five-second capture and lamp acknowledgement ordering remain intact.

37 local tests and seven new tests on Pi passed. The user heard both generated demonstration answers. A fresh live wake-to-date question was recognized and answered audibly, confirmed by the user. See the [validation record](../validation/runs/2026-10-25-pi5-date-weather.json) for the latest weather voice trial and runtime state. Code is saved locally and deployed to Pi; no GitHub update was made. Preserve concurrent website edits. No boot-start service was installed.

The weather question also passed on retry after expanding vocabulary context to full information questions; user confirmed hearing it. The original rejected transcript is preserved. Both supervised tests used one turn and exited; listening is stopped and the LED is OFF. The read-only browser terminal remains available for review. Restart the live assistant from the guide only after notifying the user.

</div>

<div dir="rtl" lang="ar">

## استئناف لاحق في اليوم نفسه — سجل تاريخي قبل الإنهاء

طلب المستخدم «اكمل». شغل المساعد بجميع الوظائف في وضع الاستماع المستمر، دون حد لعدد الطلبات، بعد إبلاغه. عرضت جلسة <code dir="ltr">course204:voice</code> الأوامر في المتصفح، واستخدم نطاق <code dir="ltr">course204-live-assistant.scope</code> بحد ذاكرة 1400 ميغابايت. تحقق ظهور <code dir="ltr">LISTENING_FOR_WAKE</code> فعليا في الطرفية والمتصفح. استمر انتظار النداء والتقاط الطلب خمس ثوان بعد «تفضل» إلى أن طلب المستخدم إنهاء الجلسة؛ أوقف الاستماع وأطفئت اللمبة كما في الحالة النهائية أعلى الملف. افحص العملية القائمة قبل أي تشغيل لاحق. لا يوجد تشغيل تلقائي عند الإقلاع.

</div>

<div dir="ltr" lang="en">

Historical same-day resume, before final shutdown: after the user asked to continue and was notified, the assistant was started without a turn limit in `course204:voice`, within the 1400 MB `course204-live-assistant.scope`. `LISTENING_FOR_WAKE` was verified on the live browser terminal. This run was subsequently stopped at the user's request. Check existing processes before any future restart. No boot-start service was installed.

</div>
