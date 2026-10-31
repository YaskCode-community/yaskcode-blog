# Blog YaskCode

- Proyecto Quarto, español principal. Mantener áreas, secciones, tarjetas y colores existentes.
- Los artículos canónicos se guardan en `posts/<slug>/index.qmd` y las imágenes junto al artículo.
- No inventar resultados educativos, referencias, métricas ni artículos publicados. Distinguir ejemplos hipotéticos.
- No incluir datos de suscriptores, claves o exportaciones de HubSpot en el repositorio público.
- No modificar beehiiv, Apps Script, HubSpot ni Campus como parte de una edición del blog sin alcance explícito.
- Trabajo editorial: preparar cambios en rama y PR. Sin merge ni despliegue hasta validación explícita de la autora, salvo autorización previa para una publicación concreta.
- Revisar `docs/MIGRACION.md` antes de continuar la migración.
- Para contenido editorial, seguir `docs/GUIA-EDITORIAL.md` y `docs/PLANTILLA-EDITORIAL-2026.md`; crear borradores desde `plantillas/articulo-aprende/index.qmd` sin publicar marcadores. El README presenta el propósito y recorrido; las instrucciones técnicas están en `docs/DESARROLLO.md`.
- Cabecera aprobada: etiquetas de etapa, área y nivel con mismo estilo; `level` separado de `categories`; `AUTORÍA:` y enlaces en línea cuando haya espacio; un solo subtítulo visible. No repetir en el cuerpo `Aprende · Área · Nivel Básico · Fundamentos`.
- Para cada artículo nuevo, registrar el slug/nivel en `assets/article-tools.js` y crear recursos y metadatos SEO reales. La plantilla no automatiza registro, métricas, fichas ni publicación.
- Consultar `docs/CONVOCATORIAS.md` al hablar de premios; verificar de nuevo cada edición. No presentar criterios internos como una rúbrica oficial ni afirmar avales o premios inexistentes.
- Comprobaciones: `quarto render`, `python3 scripts/check_site.py`, `git diff --check`.
- No asignar licencias a contenido existente sin decisión de la autora.
