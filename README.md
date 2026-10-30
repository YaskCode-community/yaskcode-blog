# Blog YaskCode

Artículos, tutoriales y recursos abiertos sobre Ingeniería de Software, Inteligencia Artificial, Ciencia de Datos y Cloud.

**Aprende · Practica · Construye · Comparte.** Español principal, acceso en inglés cuando exista una traducción revisada.

## Primera entrega de migración

Quarto genera el blog desde los originales guardados en GitHub. Esta rama contiene el artículo publicado de RAG, sus imágenes originales, tarjetas, búsqueda y navegación por área y contenido.

El sitio aún está en revisión. La URL prevista es https://yaskcode-community.github.io/yaskcode-blog/; no se presenta como un despliegue existente.

## Trabajar en local

Instala Quarto 1.10.20. No se requiere base de datos, Node ni un modelo de IA para generar este sitio.

```sh
quarto preview
```

Para generar y comprobar:

```sh
quarto render
python3 scripts/check_site.py
git diff --check
```

En Windows, si Python está instalado mediante el lanzador, utiliza `py scripts/check_site.py`.

## Añadir artículos

Crea `posts/<slug>/index.qmd` y guarda sus imágenes en la misma carpeta. Indica `title`, `author`, `date`, `description`, `categories`, `area`, `editorial-section`, `image` e `image-alt`. La portada y los filtros se actualizan al renderizar.

Mantén `draft: true` en textos pendientes de revisión y comprueba que no se incluyan en la versión pública. No publiques artículos de relleno.

## Suscripción y publicación

La suscripción enlaza a la landing actual de beehiiv. La newsletter y Apps Script → HubSpot siguen operando de forma independiente.

El workflow de esta entrega solo construye, comprueba y guarda un artefacto de revisión; no publica. Consulta [el plan y las decisiones de migración](docs/MIGRACION.md).

## Autoría y licencias

Se conserva la autoría de cada artículo. Las licencias de código y materiales están pendientes de decisión explícita; este repositorio no concede una licencia de reutilización por el solo hecho de ser público.
