<div dir="rtl" lang="ar">

# اتجاه النص والمصطلحات

الفقرات العربية تقرأ من اليمين إلى اليسار. تعزل أسماء الأنظمة والأجهزة والمصطلحات اللاتينية وأرقام إصداراتها باتجاه من اليسار إلى اليمين، خصوصًا عندما تبدأ بها الجملة.

- استخدم حاوية <span dir="ltr">HTML</span> باتجاه <code dir="ltr">rtl</code> ولغة <code dir="ltr">ar</code> للقسم العربي، واتجاه <code dir="ltr">ltr</code> ولغة <code dir="ltr">en</code> للقسم الإنجليزي.
- أحط المصطلح اللاتيني وإصداره معًا بعنصر <code dir="ltr">span</code> باتجاه <code dir="ltr">ltr</code>، مثل <span dir="ltr">Ubuntu 20.04</span> أو <span dir="ltr">Pi 5</span>.
- اعرض الأوامر والمسارات وأسماء الملفات البرمجية باتجاه <code dir="ltr">ltr</code> دون تغيير النص المنسوخ.
- أبقِ أوامر الطرفية داخل كتلة كود مستقلة باتجاه <code dir="ltr">ltr</code>. لا تضف علامات اتجاه مخفية إلى الكود أو الروابط.
- اترك سطرًا فارغًا حول حاويات <span dir="ltr">HTML</span> حتى تبقى العناوين والقوائم والجداول قابلة للعرض على <span dir="ltr">GitHub</span>.
- راجع العرض النهائي على <span dir="ltr">GitHub</span>، وليس النص الخام فقط.

</div>

<div dir="ltr" lang="en">

## English

Arabic sections use explicit right to left containers with Arabic language metadata. English sections use left to right containers. Isolate Latin terms together with their version numbers in left to right spans, including when they begin an Arabic sentence. Keep commands, paths, and code blocks left to right without changing copied text. Do not inject invisible direction controls into commands or URLs. Leave blank lines around HTML containers so GitHub renders Markdown headings, lists, and tables. Verify the rendered GitHub page.

</div>
