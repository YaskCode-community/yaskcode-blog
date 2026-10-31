(() => {
  'use strict';
  const init = () => {
    const search = document.querySelector('#article-search');
    if (!search) return;
    const cards = [...document.querySelectorAll('.post-card')];
    const groups = [...document.querySelectorAll('.filter-buttons')];
    const status = document.querySelector('#result-status');
    const empty = document.querySelector('#no-results');
    const normalize = value => String(value).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('es');
    const selected = {area: '', section: ''};
    const params = new URLSearchParams(location.search);
    for (const group of groups) {
      const key = group.dataset.group;
      const requested = params.get(key) || '';
      for (const button of group.querySelectorAll('button')) {
        if (button.dataset.value === requested) selected[key] = requested;
        button.addEventListener('click', () => {
          selected[key] = selected[key] === button.dataset.value ? '' : button.dataset.value;
          update(true);
        });
      }
    }
    search.value = params.get('q') || '';
    function update(writeUrl = false) {
      const query = normalize(search.value.trim());
      let count = 0;
      for (const card of cards) {
        const visible = (!selected.area || card.dataset.area === selected.area)
          && (!selected.section || card.dataset.section === selected.section)
          && (!query || normalize(card.textContent).includes(query));
        card.hidden = !visible;
        if (visible) count++;
      }
      for (const group of groups) for (const button of group.querySelectorAll('button')) {
        button.setAttribute('aria-pressed', String(selected[group.dataset.group] === button.dataset.value));
      }
      status.textContent = `${count} ${count === 1 ? 'artículo disponible' : 'artículos disponibles'}`;
      empty.hidden = count > 0;
      if (writeUrl) {
        const url = new URL(location.href);
        for (const [key, value] of Object.entries({...selected, q: search.value.trim()})) {
          if (value) url.searchParams.set(key, value); else url.searchParams.delete(key);
        }
        history.replaceState(null, '', url);
      }
    }
    search.addEventListener('input', () => update(true));
    document.querySelector('#reset-filters').addEventListener('click', () => {
      selected.area = ''; selected.section = ''; search.value = ''; update(true);
    });
    update();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
