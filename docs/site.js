(() => {
  const search = document.querySelector('#week-search');
  const weeks = [...document.querySelectorAll('[data-week]')];
  const count = document.querySelector('#week-count');
  const empty = document.querySelector('#no-weeks');
  const arabic = new Intl.NumberFormat('ar-SA');
  const normalize = value => value.trim().replace(/[٠-٩]/g, c => String('٠١٢٣٤٥٦٧٨٩'.indexOf(c))).replace(/[۰-۹]/g, c => String('۰۱۲۳۴۵۶۷۸۹'.indexOf(c))).replace(/[أإآ]/g, 'ا').replace(/[\u064B-\u065F]/g, '').replace(/\s+/g, ' ').toLowerCase();
  search.addEventListener('input', () => {
    const query = normalize(search.value);
    const numeric = /^\d+$/.test(query);
    let shown = 0;
    for (const week of weeks) {
      const match = numeric ? Number(week.dataset.week.split(' ')[0]) === Number(query) : normalize(`${week.dataset.week} ${week.textContent}`).includes(query);
      week.hidden = !match;
      shown += Number(match);
    }
    count.textContent = query ? `عدد النتائج: ${arabic.format(shown)}` : '١٦ عرضًا متاحًا بصيغة PDF';
    empty.hidden = shown !== 0;
  });
  document.querySelector('#copy-link').addEventListener('click', async () => {
    const url = 'https://tcti-robotics-ai.github.io/robot-operating-systems-204/';
    const status = document.querySelector('#copy-status');
    try {
      await navigator.clipboard.writeText(url);
      status.textContent = 'تم نسخ الرابط. شاركه مع من يستفيد منه.';
    } catch {
      status.textContent = `يمكنك نسخ الرابط: ${url}`;
    }
  });
})();
