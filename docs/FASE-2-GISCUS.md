# Fase 2 · Comentarios y reacciones del Blog YaskCode con Giscus

**Estado:** integración publicada y primera conversación real verificada el 31 de octubre de 2026. La prueba de moderación y revisión móvil/accesibilidad siguen pendientes.

## Objetivo

Ofrecer a los lectores comentarios y reacciones por artículo, moderados desde GitHub Discussions, sin desarrollar Workers, bases de datos o infraestructura propia. Una persona necesita iniciar sesión con GitHub para comentar o reaccionar. La lectura del blog seguirá siendo pública y no exigirá cuenta.

## Decisión de arquitectura

- Sitio: `YaskCode-community/yaskcode-blog`, publicado con **Quarto en GitHub Pages**.
- Repositorio para discusiones: **`YaskCode-community/.github`** (público y con Discussions habilitado; es la fuente de las discusiones de la organización YaskCode Community).
- Categoría **`Blog YaskCode`**, tipo **Announcement**, creada por la administradora en la sección *3. Aprendizaje y recursos*. Giscus ya la reconoce en el configurador oficial.
- Sistema: **Giscus** (`https://giscus.app/es`), aplicación gratuita de GitHub que almacena contenido en Discussions.
- Mapeo recomendado: **pathname**. El mismo artículo siempre utiliza el mismo slug y evita depender de cambios editoriales de título.
- **Reactions** habilitadas, **idioma español**, tema **light**, `input-position: bottom`, `loading: lazy`.
- Comentarios exclusivamente en los cuatro artículos de `posts/`; no en la portada ni en `acerca.qmd`.
- No usar solicitudes de Cloudflare Workers/Workers AI ni operaciones D1 de YASE.

> Nota: la instalación de Giscus y los ajustes de categorías del repositorio requieren una persona con permisos de administración de la organización y no pueden darse por realizados solo por editar el código Quarto. Las reacciones requieren autenticación de GitHub; no son «Me gusta» anónimos.

## Lista de habilitación (administración GitHub)

1. Confirmar que `YaskCode-community/.github` sigue siendo público y tiene **Discussions** habilitado. Esta condición ya estaba confirmada el 31-10-2026.
2. **Completado:** categoría **Blog YaskCode** creada en Discussions, tipo **Announcement**. Los lectores pueden comentar, pero la creación de discusiones queda restringida a mantenedores y Giscus.
3. **Completado:** aplicación oficial **Giscus** instalada en `https://github.com/apps/giscus`, con acceso **Only select repositories**, exclusivamente a `YaskCode-community/.github`.
4. **Verificado en el configurador:** repositorio `YaskCode-community/.github`, categoría **Blog YaskCode**, mapeo `pathname` y reacciones habilitadas. En Quarto se fija además idioma español, tema claro, caja de comentarios debajo y carga diferida.
5. **Completado:** identificadores reales tomados del bloque generado por Giscus (captura facilitada por la autora): `repo-id: R_kgDOT4uDYg` y `category-id: DIC_kwDOT4uDYs4DKEGP`. Corresponden al repositorio `.github`, no a `yaskcode-blog`.
6. **Prueba de funcionamiento completada:** se abrió el artículo RAG, se inició sesión con GitHub, se publicó el primer comentario y se agregó una reacción 👍. El mensaje apareció dentro de Giscus en el blog y se creó automáticamente la discusión correspondiente en la categoría **Blog YaskCode** de GitHub Discussions. **Moderación aún sin ensayo específico.**

## Integración nativa en Quarto

La versión publicada incorpora la configuración real bajo `website.comments.giscus` en `_quarto.yml`:

```yaml
  comments:
    giscus:
      repo: YaskCode-community/.github
      repo-id: R_kgDOT4uDYg
      category: Blog YaskCode
      category-id: DIC_kwDOT4uDYs4DKEGP
      mapping: pathname
      reactions-enabled: true
      input-position: bottom
      loading: lazy
      language: es
      theme: light
```

La portada `index.qmd` y `acerca.qmd` conservan `comments: false`. Los comentarios solo se renderizan en los cuatro artículos. El script se incorpora mediante la integración nativa de Quarto; no agregar otro script Giscus a `assets/footer.html`, porque duplicaría el widget.

## Evidencia funcional · 31 de octubre de 2026

- **Artículo:** [RAG: fundamentos y arquitectura para comenzar](https://yaskcode-community.github.io/yaskcode-blog/posts/rag-fundamentos-arquitectura/).
- **Comentario:** la autora publicó el texto de inauguración, invitando a conversar sobre las aplicaciones de RAG en educación, investigación y desarrollo de software.
- **Reacción:** la captura del blog muestra 👍 1 en el comentario inaugural.
- **Vinculación:** una captura de GitHub Discussions muestra una discusión generada por `giscus[bot]`, con ruta `yaskcode-blog/posts/rag-fundamentos-arquitectura/`, dentro de la categoría **Blog YaskCode** en la sección *3. Aprendizaje y recursos*, con un comentario.
- **Alcance:** verificación visual de sincronización y participación en el artículo RAG. No se han ensayado todavía todas las opciones de moderación ni las interacciones en vista móvil.
- **Infraestructura:** permanece sin uso de Workers, D1 ni Workers AI de YASE.

## Moderación y experiencia de lectura

- Aplicar [Código de conducta de YaskCode Community](https://github.com/YaskCode-community/.github/blob/main/CODE_OF_CONDUCT.md); moderar directamente desde GitHub Discussions.
- Los comentarios son públicos y pueden ser visibles también desde GitHub, no solo dentro del artículo.
- Giscus no ofrece comentarios anónimos: la participación requiere la autorización correspondiente de GitHub.
- Evitar publicar datos personales de estudiantes, calificaciones, información de salud o datos institucionales confidenciales.
- Si Giscus está temporalmente indisponible, los artículos deben seguir siendo legibles. La difusión, el RSS y Web Analytics continúan independientes.
- No publicar contadores de reacciones ni vistas simulados.

## Pruebas de aceptación (antes de marcar Fase 2 completada)

- [x] Aplicación Giscus instalada solo en repositorio autorizado.
- [x] Categoría **Blog YaskCode** existente y con tipo adecuado.
- [x] `_quarto.yml` con IDs reales, sin placeholders.
- [x] Validación automática: portada y Acerca de sin comentarios; los cuatro artículos incluyen el widget Giscus. Validación visual manual confirmada para RAG.
- [x] Primera publicación de comentario y reacción 👍 desde el artículo RAG; discusión creada y visible en la categoría **Blog YaskCode** de la comunidad.
- [ ] Prueba de moderación real: revisar opciones disponibles para ocultar/denunciar/eliminar un comentario de prueba, sin alterar el comentario inaugural.
- [ ] Tema móvil, teclado, carga diferida y ausencia de solapamientos revisados.
- [x] CI de Quarto correcto, PR #15 integrado y despliegue GitHub Pages #41182231582 exitoso.

Fuentes oficiales:
- https://giscus.app/es
- https://quarto.org/docs/reference/projects/websites.html
- https://docs.github.com/en/discussions/quickstart
- https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions
