"""Check real rendered pages and their local links; no network or dependencies."""
from html.parser import HTMLParser
import json
from xml.etree import ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / '_site'
PREFIX = '/yaskcode-blog/'
errors = []

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if attrs.get(key):
                self.refs.append(attrs[key])
        if tag == 'img' and 'alt' not in attrs:
            errors.append('Imagen sin atributo alt')

pages = {}
for path in ROOT.rglob('*.html'):
    page = Page()
    page.feed(path.read_text())
    pages[path.resolve()] = page
assert ROOT.joinpath('index.html').exists(), 'Falta index.html'
assert ROOT.joinpath('posts/rag-fundamentos-arquitectura/index.html').exists(), 'Falta RAG'
# El blog publica cuatro entradas y un feed RSS sindicado independiente de la newsletter.
feed_path = ROOT / 'index.xml'
assert feed_path.exists(), 'Falta index.xml (RSS)'
feed = ET.parse(feed_path).getroot()
assert feed.tag == 'rss', 'El feed no es RSS válido'
rss_items = feed.findall('./channel/item')
assert len(rss_items) >= 4, f'RSS incompleto: {len(rss_items)} publicaciones'
assert all((item.findtext('link') or '').startswith('https://') for item in rss_items), 'RSS con enlaces no absolutos'
# Estadísticas públicas: archivo estático, fuente real, sin contadores simulados.
snapshot_file = ROOT / 'assets/views.json'
assert snapshot_file.exists(), 'Falta assets/views.json'
snapshot = json.loads(snapshot_file.read_text(encoding='utf-8'))
assert snapshot.get('schema_version') == 2 and snapshot.get('window_days') == 30, 'Ventana de vistas inválida'
assert snapshot.get('metric') == 'recorded_pageviews_non_bot', 'Métrica pública no verificada'
assert snapshot.get('generated_at'), 'La instantánea debe indicar su fecha'
paths = snapshot.get('paths')
assert isinstance(paths, dict), 'Faltan rutas de vistas'
assert PREFIX in paths, 'Falta la portada en vistas'
assert all(isinstance(value, dict) and
           isinstance(value.get('total'), int) and value['total'] >= 0 and
           isinstance(value.get('last_30_days'), int) and
           0 <= value['last_30_days'] <= value['total']
           for value in paths.values()), 'Histórico o métricas de 30 días inválidos'
# Giscus debe mostrarse únicamente en las cuatro publicaciones, no en portada ni Acerca de.
article_pages = sorted((ROOT / 'posts').glob('*/index.html'))
assert len(article_pages) == 4, f'Se esperaban 4 artículos, hay {len(article_pages)}'
for article_path in article_pages:
    assert PREFIX + 'posts/' + article_path.parent.name + '/' in paths, f'Falta contador para {article_path.parent.name}'
    assert 'giscus.app/client.js' in article_path.read_text(), (
        f'Falta Giscus en {article_path.relative_to(ROOT)}'
    )
for rel in ('index.html', 'acerca.html'):
    assert 'giscus.app/client.js' not in (ROOT / rel).read_text(), (
        f'Giscus no debe mostrarse en {rel}'
    )
for path, page in pages.items():
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc or not url.path:
            continue
        route = unquote(url.path)
        if route.startswith(PREFIX):
            target = ROOT / route[len(PREFIX):]
        elif route.startswith('/'):
            target = ROOT / route.lstrip('/')
        else:
            target = path.parent / route
        if target.is_dir():
            target = target / 'index.html'
        if not target.exists():
            errors.append(f'{path.relative_to(ROOT)} → {ref}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(pages)} páginas; enlaces y recursos locales disponibles.')
