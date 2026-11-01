// Pruebas DOM simuladas, sin red ni paquetes. Node.js >= 20.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const js = fs.readFileSync('assets/filters.js', 'utf8');

function element({dataset = {}, textContent = ''} = {}) {
  return {
    dataset, textContent, hidden: false, disabled: false, value: '',
    attrs: {}, children: [], listeners: {},
    setAttribute(key, value) { this.attrs[key] = value; },
    addEventListener(name, fn) { this.listeners[name] = fn; },
    append(child) { this.children.push(child); },
    replaceChildren() { this.children = []; },
    querySelectorAll() { return []; },
    scrollIntoView() {},
    click() { if (this.listeners.click) this.listeners.click(); }
  };
}

function setup(url = 'https://example.org/yaskcode-blog/') {
  const cards = Array.from({length: 12}, (_, i) => element({
    dataset: {area: i % 2 ? 'Ciencia de Datos' : 'Inteligencia Artificial', section: i < 8 ? 'Aprende' : 'Práctica'},
    textContent: 'Artículo ' + (i + 1)
  }));
  const grid = element();
  grid.querySelectorAll = () => cards;
  const search = element();
  const status = element();
  const noResults = element();
  const nav = element();
  nav.hidden = true;
  const numbers = element();
  const previous = element();
  const next = element();
  const summary = element();
  const reset = element();
  const heading = element();
  const areaButtons = ['Inteligencia Artificial', 'Ciencia de Datos'].map(value => {
    const b = element({dataset: {value}});
    b.dataset.value = value;
    return b;
  });
  const areaGroup = element({dataset:{group:'area'}});
  areaGroup.querySelectorAll = () => areaButtons;
  const sectionGroup = element({dataset:{group:'section'}});
  const sectionButtons = ['Aprende','Práctica'].map(value => element({dataset: {value}}));
  sectionGroup.querySelectorAll = () => sectionButtons;
  const nodes = {
    '#article-search': search, '#article-grid': grid, '#result-status': status,
    '#no-results': noResults, '#article-pagination':nav, '#yc-page-numbers':numbers,
    '#yc-page-prev':previous, '#yc-page-next':next, '#yc-page-summary':summary,
    '#reset-filters':reset, '.article-controls':heading
  };
  const document = {
    readyState: 'complete', querySelector: selector => nodes[selector],
    querySelectorAll: selector => selector === '.filter-buttons' ? [areaGroup, sectionGroup] : [],
    createElement: () => element(),
    addEventListener() {}
  };
  const location = new URL(url);
  const history = {replaceState(_a, _b, dest) { location.href = String(dest); }};
  vm.runInNewContext(js, {document, location, history, URL, URLSearchParams, Set}, {filename:'assets/filters.js'});
  return {cards, search, status, noResults, nav, numbers, previous, next, summary, reset, areaButtons, sectionButtons, location};
}

let page = setup();
assert.equal(page.cards.filter(c => !c.hidden).length, 9, 'Portada debe mostrar 9');
assert.equal(page.status.textContent, '12 artículos disponibles · Mostrando 1–9');
assert.equal(page.numbers.children.length, 2, '12 artículos requieren dos páginas');
assert.equal(page.next.disabled, false);
page.next.click();
assert.equal(page.cards.filter(c => !c.hidden).length, 3, 'Segunda página debe mostrar 3');
assert.equal(page.status.textContent, '12 artículos disponibles · Mostrando 10–12');
assert.equal(page.location.searchParams.get('page'), '2');
page.search.value = 'Artículo 11';
page.search.listeners.input();
assert.equal(page.cards.filter(c => !c.hidden).length, 1, 'Buscar incluye página 2');
assert.equal(page.location.searchParams.has('page'), false, 'Buscar reinicia página');
assert.equal(page.nav.hidden, true, 'Una página no muestra controles');
page.search.value = '';
page.search.listeners.input();
page.areaButtons[0].click();
assert.equal(page.cards.filter(c => !c.hidden).length, 6, 'Filtro se aplica a todas las tarjetas');
page.reset.click();
assert.equal(page.cards.filter(c => !c.hidden).length, 9, 'Restaurar devuelve la página 1');
page.search.value = 'No existe';
page.search.listeners.input();
assert.equal(page.cards.filter(c => !c.hidden).length, 0);
assert.equal(page.noResults.hidden, false, 'Estado vacío visible');
// Un caso puede pertenecer a Casos de estudio y Comunidad YaskCode a la vez.
page = setup();
page.cards[0].dataset.section = 'Casos de estudio';
page.cards[0].dataset.community = 'true';
const community = page.sectionButtons.find(b => b.dataset.value === 'Comunidad YaskCode');
assert(community, 'Debe existir filtro Comunidad YaskCode');
community.click();
assert.equal(page.cards[0].hidden, false, 'Los casos con categoría Comunidad deben aparecer en ese filtro');
page = setup();
page.cards[0].dataset.section = 'Casos de estudio';
page.cards[0].dataset.community = 'true';
const cases = page.sectionButtons.find(b => b.dataset.value === 'Casos de estudio');
assert(cases, 'Debe existir filtro Casos de estudio');
cases.click();
assert.equal(page.cards.filter(c => !c.hidden).length, 1, 'Casos de estudio muestra el caso');
page = setup('https://example.org/yaskcode-blog/?page=2');
assert.equal(page.cards.filter(c => !c.hidden).length, 3, 'El enlace a página 2 se restaura');
page = setup('https://example.org/yaskcode-blog/?page=999');
assert.equal(page.cards.filter(c => !c.hidden).length, 3, 'Página fuera de rango se ajusta');
console.log('OK: paginación 9/3, búsqueda global, filtros, URL y estado vacío');
