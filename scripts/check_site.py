"""Check real rendered pages and their local links; no network or dependencies."""
from html.parser import HTMLParser
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
