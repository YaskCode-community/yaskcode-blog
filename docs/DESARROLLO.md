# Desarrollo y colaboración técnica

Esta guía describe la operación actual del blog Quarto. Para el propósito y recorrido editorial, consulta el [README](../README.md), la [guía editorial](GUIA-EDITORIAL.md) y la [plantilla editorial](PLANTILLA-EDITORIAL-2026.md).

## Estado del proyecto

**Blog YaskCode está publicado en [GitHub Pages](https://yaskcode-community.github.io/yaskcode-blog/)**. Su fuente vive en la rama `main`; las correcciones editoriales de la cabecera aprobadas el 31 de octubre de 2026 se integraron mediante los PR #22, #23 y #24. La migración y ampliación de contenidos siguen evolucionando y requieren revisión.

| Componente | Función |
| --- | --- |
| Repositorio y Quarto | Fuentes `.qmd`, diseño, datos y generación estática del sitio. |
| GitHub Pages | Blog público; después de cada cambio revisar también la URL publicada. |
| GitHub Actions | Comprueba render, enlaces y scripts; un CI exitoso no prueba por sí solo el aspecto visual del sitio desplegado. |
| beehiiv | Suscripción y newsletter; publicar un artículo no envía un correo automáticamente. |
| Apps Script → HubSpot | Sincronización de contactos independiente del blog. |
| Campus YaskCode | Sitio Astro separado, no afectado por cambios de este repositorio. |

Consulta el [registro de migración](MIGRACION.md) para las tareas históricas y pendientes que aún deban verificarse.

## Explorar el contenido

**Áreas:** Ingeniería de Software, Ciencia de Datos, Inteligencia Artificial y Cloud Computing.

**Secciones:** Radar tecnológico, Aprende, Práctica, Construye, Comparte, Explora y participa y Comunidad YaskCode.

La portada permite combinar filtros de área y sección y buscar por título, tema o descripción. La búsqueda de la barra superior permite consultar el contenido completo del sitio.

## Preparar el entorno local

Se necesitan Git y **Quarto 1.10.20**, la misma versión utilizada por el workflow de revisión. Python 3 se utiliza para comprobar recursos locales. El sitio actual no requiere Node ni una base de datos.

Para una primera descarga:

```powershell
git clone https://github.com/YaskCode-community/yaskcode-blog.git
cd yaskcode-blog
git switch main
code -n .
```

Si ya tienes la carpeta abierta, no hace falta volver a clonar. Ejecuta los siguientes comandos desde la raíz de `yaskcode-blog`.

### Ver el blog

```powershell
quarto preview
```

Abre la dirección que indique la terminal; el puerto puede variar. Para detener la vista previa, pulsa **Ctrl + C** en esa terminal.

### Generar y comprobar

En Windows:

```powershell
quarto render
py scripts/check_site.py
git diff --check
```

En Linux o macOS, sustituye `py` por `python3`.

El sitio generado queda en `_site/`. Se editan los archivos fuente, no las páginas de esa carpeta. La comprobación de recursos valida enlaces e imágenes locales; la revisión visual, de teclado y de enlaces externos se realiza por separado.

## Escribir un artículo nuevo con la plantilla aprobada

El esqueleto reutilizable está en **[`plantillas/articulo-aprende/index.qmd`](../plantillas/articulo-aprende/index.qmd)**; está fuera de `posts/` y de los archivos de render, de modo que no se publica por sí solo. Desde la raíz del repositorio, en PowerShell:

```powershell
New-Item -ItemType Directory -Path posts/mi-articulo
Copy-Item plantillas/articulo-aprende/index.qmd posts/mi-articulo/index.qmd
```

1. Cambiar `mi-articulo` por el slug final, reemplazar todos los marcadores `REEMPLAZAR` y la fecha de ejemplo, y mantener `draft: true` durante la revisión.
2. Ajustar `categories` (etapa y área), `area`, `editorial-section`, `level` (**Básico / Intermedio / Avanzado**) y, si procede, `level-detail`. El nivel **no es una categoría**. Para un artículo de comunidad, no aplicar automáticamente la plantilla técnica ni añadir nivel.
3. Preparar la portada y su texto alternativo, la ficha real `recursos/<slug>-ficha.md` y el archivo `assets/seo-<slug>.html` con datos estructurados `BlogPosting` y fechas veraces. La plantilla referencia ese archivo, pero **no lo genera**.
4. Registrar el nuevo slug y nivel en `assets/article-tools.js`, que actualmente enumera artículos explícitamente; comprobar los relacionados, el índice/tarjetas, métricas, pruebas de conteo y rutas del artículo. Los contadores **no se inventan**.
5. No escribir en el cuerpo `**Aprende · Área · Nivel Básico · Fundamentos**`, ni otra línea que repita categorías y nivel: esas etiquetas ya aparecen arriba. `subtitle` es la única introducción breve visible; `description` queda para SEO y se mantiene «En 1 minuto» como síntesis didáctica.
6. Comprobar con `quarto preview` y `quarto render`; ejecutar las pruebas, revisar enlaces, teclado, escritorio y móvil. Antes de quitar `draft: true`, solicitar aprobación editorial y confirmar el funcionamiento del artículo público después de desplegar.

La **autoría** usa el rótulo `AUTORÍA:` y enlaza el perfil académico y ORCID; las fechas comparten fila cuando cabe. El bloque superior de compartir no debe recuperar un recuadro, y la etiqueta del nivel debe compartir estilo con las de etapa y área.

**Importante:** el registro de artículos, los metadatos SEO por publicación y las comprobaciones automatizadas actuales no se crean automáticamente al copiar la plantilla. No se afirma que exista un laboratorio, ficha, imagen o evidencia hasta publicar el recurso real.

## Archivos principales

| Ruta | Contenido |
| --- | --- |
| `_quarto.yml` | Configuración, navegación y opciones generales. |
| `index.qmd` | Portada y controles para explorar artículos. |
| `acerca.qmd` | Presentación pública del propósito y recorrido editorial. |
| `posts/<slug>/index.qmd` | Texto y metadatos de cada artículo. |
| `plantillas/articulo-aprende/index.qmd` | Plantilla reutilizable de borrador, excluida del render público. |
| `docs/PLANTILLA-EDITORIAL-2026.md` | Estándar aprobado de cabecera y lista de verificación. |
| `assets/theme.scss` | Colores, tipografía y estilos. |
| `assets/cards.ejs.md` | Plantilla de tarjetas. |
| `assets/filters.js` | Filtros y búsqueda de la portada. |
| `scripts/check_site.py` | Comprobación de recursos locales. |
| `.github/workflows/check.yml` | Construcción y comprobación en GitHub Actions. |
| `docs/MIGRACION.md` | Decisiones y pendientes de migración. |
| `AGENTS.md` | Instrucciones para asistentes que trabajen en el repositorio. |

## Suscripción y comunidad

La suscripción continúa en [beehiiv](https://yaskcode.beehiiv.com/). La integración con HubSpot funciona de manera independiente del blog; aquí no se guardan contactos, credenciales ni exportaciones de suscriptores.

Puedes participar en [YaskCode Community](https://github.com/YaskCode-community), proponer ideas en [Discussions](https://github.com/orgs/YaskCode-community/discussions) o comunicar correcciones mediante un [issue del blog](https://github.com/YaskCode-community/yaskcode-blog/issues).

## Trabajo editorial y operativo pendiente

- Revisar cualquier nueva entrada con la plantilla y sus criterios de nivel; no repetir etiquetas ni introducir un segundo párrafo de presentación.
- Validar visualmente cada incorporación en escritorio, móvil y teclado, además del CI.
- Continuar migrando entradas tras su comprobación editorial, bibliográfica, SEO y de permisos.
- Revisar el registro de migración para confirmar qué enlaces antiguos o integraciones siguen pendientes.
- Decidir y documentar licencias antes de permitir reutilización no autorizada.

## Autoría y licencias

Se conserva la autoría de cada artículo y la procedencia de los recursos. Las licencias de código y contenidos están pendientes de decisión explícita de la autora; la visibilidad pública de este repositorio no concede por sí sola una licencia de reutilización.
