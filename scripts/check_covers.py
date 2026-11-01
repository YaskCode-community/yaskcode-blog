"""Validate article covers in rendered cards, social metadata and JSON-LD."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
BASE = 'https://yaskcode-community.github.io/yaskcode-blog/'

class Metadata(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.meta = {}
        self.images = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'meta':
            self.meta.setdefault(a.get('property', a.get('name')), []).append(a.get('content'))
        if tag == 'img':
            self.images.append(a)

index = Metadata((SITE / 'index.html').read_text())
count = 0
for source in sorted((ROOT / 'posts').glob('*/index.qmd')):
    front = source.read_text().split('---', 2)[1]
    def field(name):
        match = re.search(r'^' + re.escape(name) + r':\s*(.+)$', front, re.M)
        assert match, f'{source}: falta {name}'
        return match[1].strip().strip('"\'')
    name, alt = field('image'), field('image-alt')
    assert name.endswith('.webp') and alt, source
    relative = f'posts/{source.parent.name}/{name}'
    assert (ROOT / relative).is_file() and (SITE / relative).is_file(), relative
    data = (ROOT / relative).read_bytes()
    assert data[:4] == b'RIFF' and data[8:12] == b'WEBP', relative
    text = (SITE / source.parent.relative_to(ROOT) / 'index.html').read_text()
    page = Metadata(text)
    expected = BASE + relative
    for key in ('og:image', 'twitter:image'):
        assert page.meta.get(key) == [expected], (relative, key, page.meta.get(key))
    for key in ('og:image:alt', 'twitter:image:alt'):
        assert page.meta.get(key) == [alt], (relative, key, page.meta.get(key))
    assert page.meta.get('twitter:card') == ['summary_large_image'], relative
    records = [json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S)]
    postings = [x for x in records if x.get('@type') == 'BlogPosting']
    assert len(postings) == 1 and postings[0].get('image') == expected, relative
    matching = [i for i in index.images if unquote(urlsplit(i.get('src', '')).path).removeprefix('./').lstrip('/').removeprefix('yaskcode-blog/') == relative]
    assert len(matching) == 1, (relative, matching)
    count += 1
print(f'OK: {count} portadas WebP; tarjetas, Open Graph, Twitter y JSON-LD coherentes, sin duplicados.')
