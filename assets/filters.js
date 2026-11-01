(() => {
  'use strict';
  const PAGE_SIZE = 9;

  const init = () => {
    const search = document.querySelector('#article-search');
    const grid = document.querySelector('#article-grid');
    if (!search || !grid) return;

    const cards = [...grid.querySelectorAll('.post-card')];
    const groups = [...document.querySelectorAll('.filter-buttons')];
    const status = document.querySelector('#result-status');
    const empty = document.querySelector('#no-results');
    const pagination = document.querySelector('#article-pagination');
    const pagesContainer = document.querySelector('#yc-page-numbers');
    const previous = document.querySelector('#yc-page-prev');
    const next = document.querySelector('#yc-page-next');
    const summary = document.querySelector('#yc-page-summary');
    const normalize = value => String(value).normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('es');
    const params = new URLSearchParams(location.search);
    const requestedPage = Number(params.get('page') || '1');
    let page = Number.isSafeInteger(requestedPage) && requestedPage >= 1 ? requestedPage : 1;
    const selected = {area: '', section: ''};

    const writeState = () => {
      const url = new URL(location.href);
      for (const [key, value] of Object.entries({...selected, q: search.value.trim()})) {
        if (value) url.searchParams.set(key, value); else url.searchParams.delete(key);
      }
      if (page > 1) url.searchParams.set('page', String(page));
      else url.searchParams.delete('page');
      history.replaceState(null, '', url);
    };

    const makeButton = (label, target, current = false) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = String(label);
      button.setAttribute('aria-label', 'Ir a la página ' + target);
      if (current) {
        button.setAttribute('aria-current', 'page');
        button.disabled = true;
      } else {
        button.addEventListener('click', () => changePage(target));
      }
      return button;
    };

    const changePage = value => {
      page = value;
      update(true);
      const heading = document.querySelector('.article-controls');
      if (heading) heading.scrollIntoView({behavior: 'auto', block: 'start'});
    };

    function update(writeUrl = false) {
      const query = normalize(search.value.trim());
      const matches = cards.filter(card =>
        (!selected.area || card.dataset.area === selected.area)
        && (!selected.section || card.dataset.section === selected.section)
        && (!query || normalize(card.textContent).includes(query))
      );
      const total = matches.length;
      const pageCount = Math.ceil(total / PAGE_SIZE);
      page = Math.min(Math.max(1, page), Math.max(pageCount, 1));
      const start = (page - 1) * PAGE_SIZE;
      const visible = new Set(matches.slice(start, start + PAGE_SIZE));

      for (const card of cards) card.hidden = !visible.has(card);
      for (const group of groups) {
        for (const button of group.querySelectorAll('button')) {
          button.setAttribute('aria-pressed', String(selected[group.dataset.group] === button.dataset.value));
        }
      }

      if (status) {
        const range = total ? ' · Mostrando ' + (start + 1) + '–' + Math.min(start + PAGE_SIZE, total) : '';
        status.textContent = total + (total === 1 ? ' artículo disponible' : ' artículos disponibles') + range;
      }
      if (empty) empty.hidden = total > 0;

      // La búsqueda y los filtros siempre incluyen TODAS las tarjetas; el paginado
      // se aplica después de obtener los resultados filtrados.
      if (pagination && pagesContainer && previous && next && summary) {
        pagination.hidden = pageCount <= 1;
        summary.textContent = pageCount > 1 ? 'Página ' + page + ' de ' + pageCount : '';
        previous.disabled = page === 1;
        next.disabled = page >= pageCount;
        pagesContainer.replaceChildren();
        if (pageCount > 1) {
          for (let number = 1; number <= pageCount; number++) {
            pagesContainer.append(makeButton(number, number, number === page));
          }
        }
      }

      if (writeUrl) writeState();
    }

    for (const group of groups) {
      const key = group.dataset.group;
      const requested = params.get(key) || '';
      for (const button of group.querySelectorAll('button')) {
        if (button.dataset.value === requested) selected[key] = requested;
        button.addEventListener('click', () => {
          selected[key] = selected[key] === button.dataset.value ? '' : button.dataset.value;
          page = 1;
          update(true);
        });
      }
    }

    search.value = params.get('q') || '';
    search.addEventListener('input', () => {
      page = 1;
      update(true);
    });
    const reset = document.querySelector('#reset-filters');
    if (reset) reset.addEventListener('click', () => {
      selected.area = '';
      selected.section = '';
      search.value = '';
      page = 1;
      update(true);
    });
    if (previous) previous.addEventListener('click', () => {
      if (page > 1) changePage(page - 1);
    });
    if (next) next.addEventListener('click', () => {
      changePage(page + 1);
    });

    update();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
