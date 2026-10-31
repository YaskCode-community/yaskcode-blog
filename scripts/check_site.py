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
# El artículo principal solo permite 💜 mediante Pagemoji; sin barra Giscus de reacciones.
config = (ROOT.parent / '_quarto.yml').read_text(encoding='utf-8')
assert 'reactions-enabled: false' in config, 'La barra de reacciones principal debe estar desactivada'
ui = (ROOT / 'assets/article-tools.js').read_text(encoding='utf-8')
assert 'pagemoji.magicpages.co/v1/pagemoji.js' in ui, 'Falta carga de botón positivo'
assert 'widget.setAttribute("emojis", "💜")' in ui, 'Debe mostrarse solo corazón positivo'
assert 'top.insertAdjacentElement("beforebegin",like)' in ui, 'Me gusta debe estar antes de Compartir'
# Cabecera compacta: imprimir con Me gusta; perfil y ORCID junto al nombre.
client = (ROOT / 'assets/article-tools.js').read_text(encoding='utf-8')
styles = (ROOT / 'assets/theme.css').read_text(encoding='utf-8') if (ROOT / 'assets/theme.css').exists() else ''
assert 'section.append(widget,print)' in client, 'La impresión debe acompañar al botón Me gusta'
assert 'authorLine.append(authorLinks)' in client, 'Los enlaces deben ir junto al nombre de autoría'
assert 'authorLine.textContent.trim() === "Yaskelly Yedra"' in client, 'El perfil académico y ORCID solo corresponden a su autora'
assert 'Conoce a la autora:' not in client, 'No duplicar la autoría en otra línea'
assert 'grid-column: 1 / -1' in (ROOT.parent / 'assets/theme.scss').read_text(encoding='utf-8'), 'Fechas deben compartir fila'
# Coherencia de cabecera: metadatos, una introducción y nivel educativo.
client = (ROOT / 'assets/article-tools.js').read_text(encoding='utf-8')
css = (ROOT.parent / 'assets/theme.scss').read_text(encoding='utf-8')
assert 'authorHeading.textContent = "AUTORÍA:"' in client, 'Autoría debe estar en mayúsculas y en la misma fila'
assert 'margin-top: .75rem;' in css, 'Falta separación entre etiquetas y autoría'
author_heading_style = css.split('> div:first-child .quarto-title-meta-heading {', 1)[1].split('}', 1)[0]
assert 'text-transform:' not in author_heading_style and 'font-size:' not in author_heading_style and 'font-weight:' not in author_heading_style, 'Autoría debe heredar el estilo nativo de los rótulos de fechas'
assert 'yc-level-badge' in client and '.quarto-category.yc-level-badge' in css, 'Falta etiqueta de nivel'
assert '.quarto-categories .yc-level-badge {' not in css, 'El nivel no debe tener un estilo diferente al de las otras categorías'
assert '#title-block-header .description { display: none; }' in css, 'Descripción SEO repetida visualmente'
assert client.count('level:"Básico"') == 3, 'Los tres artículos técnicos requieren nivel Básico'
assert 'historia-campus-yaskcode",level' not in client, 'El relato del Campus no debe tener nivel técnico'
# Plantilla editorial: recursos físicos, autoría, metadatos sociales y BlogPosting.
source = (ROOT / 'assets/article-tools.js').read_text(encoding='utf-8')
assert 'articleMeta(content)' in source, 'Falta tiempo de lectura y perfil de autora'
assert 'window.print()' in source, 'Falta opción de impresión/PDF'
for post in sorted((ROOT / 'posts').glob('*/index.html')):
    slug = post.parent.name
    page_html = post.read_text(encoding='utf-8')
    assert 'application/ld+json' in page_html and 'BlogPosting' in page_html, f'Sin datos estructurados: {slug}'
    assert 'og:title' in page_html, f'Sin Open Graph: {slug}'
    assert 'twitter:card' in page_html, f'Sin Twitter Card: {slug}'
    assert 'orcid.org/0009-0004-4290-120X' in page_html, f'Sin ORCID estructurado: {slug}'
    assert 'En 1 minuto' in page_html, f'Sin resumen: {slug}'
    assert 'Conocimientos previos' in page_html, f'Sin prerrequisitos: {slug}'
    assert 'Recursos para llevar' in page_html, f'Sin sección descargable: {slug}'
    assert (ROOT / 'recursos' / f'{slug}-ficha.md').exists(), f'Sin ficha descargable: {slug}'
for slug in ('rag-fundamentos-arquitectura','hugging-face-modelos-datasets-ciencia-de-datos',
             'por-que-aprender-poo-en-la-era-de-la-ia'):
    html = (ROOT / 'posts' / slug / 'index.html').read_text(encoding='utf-8')
    assert 'Referencias académicas y técnicas' in html, f'Faltan referencias: {slug}'
# El esqueleto operativo está fuera de posts/ y siempre arranca como borrador.
template = ROOT.parent / 'plantillas/articulo-aprende/index.qmd'
assert template.exists(), 'Falta plantilla Quarto reutilizable de Aprende'
scaffold = template.read_text(encoding='utf-8')
for required in ('draft: true', 'subtitle:', 'description:', 'categories:', 'area:',
                 'editorial-section:', 'level:', 'level-detail:', 'include-in-header:',
                 'En 1 minuto', 'Lo que aprenderás', 'Conocimientos previos',
                 'Recursos para llevar', 'Referencias académicas y técnicas'):
    assert required in scaffold, f'Falta {required} en la plantilla Aprende'
# Los relatos de comunidad usan una plantilla narrativa sin nivel técnico.
community_template = ROOT.parent / 'plantillas/articulo-comunidad/index.qmd'
assert community_template.exists(), 'Falta plantilla narrativa de Comunidad'
community_scaffold = community_template.read_text(encoding='utf-8')
community_metadata = community_scaffold.split('---', 2)[1]
assert 'draft: true' in community_metadata, 'La plantilla de Comunidad debe iniciar en borrador'
assert 'categories: ["Comunidad YaskCode"]' in community_metadata, 'Falta categoría de Comunidad'
assert '\nlevel:' not in community_metadata and '\nlevel-detail:' not in community_metadata, 'Un relato no debe recibir dificultad técnica'
assert 'Qué encontrarás' in community_scaffold and 'Fuentes y recursos del proyecto' in community_scaffold, 'Faltan orientaciones propias de la narrativa'
assert 'plantillas/' not in config, 'No incluir plantillas en la configuración de render'

# Revisión de los tres artículos adicionales; dos técnicos ya son conformes.
for slug in ('hugging-face-modelos-datasets-ciencia-de-datos', 'por-que-aprender-poo-en-la-era-de-la-ia'):
    article = (ROOT.parent / 'posts' / slug / 'index.qmd').read_text(encoding='utf-8')
    metadata = article.split('---', 2)[1]
    for needle in ('editorial-section: "Aprende"', 'level: "Básico"', 'subtitle:',
                   'description:', 'image-alt:', 'include-in-header:'):
        assert needle in metadata, f'Metadato {needle} ausente en {slug}'
    for needle in ('En 1 minuto', 'Lo que aprenderás', 'Antes de comenzar',
                   'Conocimientos previos', 'Público destinatario',
                   'Recursos para llevar', 'Referencias académicas y técnicas',
                   'Continúa aprendiendo', 'Comparte con la comunidad'):
        assert needle in article, f'Componente {needle} ausente en {slug}'

campus_source = (ROOT.parent / 'posts/historia-campus-yaskcode/index.qmd').read_text(encoding='utf-8')
campus_metadata = campus_source.split('---', 2)[1]
assert 'editorial-section: "Comunidad YaskCode"' in campus_metadata
assert '\nlevel:' not in campus_metadata, 'No asignar nivel técnico al relato de Campus'
for needle in ('Qué encontrarás', '### Antes de comenzar', 'Público destinatario',
               'Comparte con la comunidad', 'Fuentes y recursos del proyecto'):
    assert needle in campus_source, f'Falta {needle} en el relato de Campus'
assert '*Comunidad YaskCode · Historia de origen · Experiencia educativa*' not in campus_source, 'Categoría de comunidad repetida en el cuerpo'
# Modelo de caso de estudio: dos etiquetas editoriales, sin nivel automático ni publicación.
case_template = ROOT.parent / 'plantillas/articulo-caso-estudio/index.qmd'
assert case_template.exists(), 'Falta plantilla de casos de estudio'
case_source = case_template.read_text(encoding='utf-8')
case_metadata = case_source.split('---', 2)[1]
assert 'categories: ["Comunidad YaskCode", "Casos de estudio"]' in case_metadata
assert 'editorial-section: "Comunidad YaskCode"' in case_metadata
assert 'draft: true' in case_metadata, 'La plantilla nunca debe publicarse directamente'
assert '\nlevel:' not in case_metadata, 'Un caso de estudio no lleva nivel técnico por defecto'
assert 'author:' in case_metadata and 'adaptación editorial' in case_source.lower(), 'Separar autoría de edición'

# Evitar volver a insertar bajo la cabecera las etiquetas ya mostradas por Quarto.
for source_path in (ROOT.parent / 'posts').glob('*/index.qmd'):
    qmd = source_path.read_text(encoding='utf-8')
    for line in qmd.splitlines():
        heading = line.strip()
        assert not (heading.startswith(('**Aprende ·', '**Practica ·')) and
                    '· Nivel ' in heading), f'Etiquetas duplicadas en {source_path.name}'
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
