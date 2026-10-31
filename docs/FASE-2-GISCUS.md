# Fase 2 · Comentarios y reacciones del Blog YaskCode con Giscus

**Estado:** preparación técnica. **Todavía no está habilitado el widget de comentarios en producción**.

## Objetivo

Ofrecer a los lectores comentarios y reacciones por artículo, moderados desde GitHub Discussions, sin desarrollar Workers, bases de datos o infraestructura propia. Una persona necesita iniciar sesión con GitHub para comentar o reaccionar. La lectura del blog seguirá siendo pública y no exigirá cuenta.

## Decisión de arquitectura

- Sitio: `YaskCode-community/yaskcode-blog`, publicado con **Quarto en GitHub Pages**.
- Repositorio para discusiones: **`YaskCode-community/.github`** (público y con Discussions habilitado; es la fuente de las discusiones de la organización YaskCode Community).
- Categoría propuesta: **`Blog YaskCode`**, tipo **Announcement**, dedicada a conversaciones específicas de artículos. Esta categoría **todavía necesita crearse** y debe tener el nombre y tipo acordados antes de configurar la incrustación.
- Sistema: **Giscus** (`https://giscus.app/es`), aplicación gratuita de GitHub que almacena contenido en Discussions.
- Mapeo recomendado: **pathname**. El mismo artículo siempre utiliza el mismo slug y evita depender de cambios editoriales de título.
- **Reactions** habilitadas, **idioma español**, tema **light**, `input-position: bottom`, `loading: lazy`.
- Comentarios exclusivamente en los cuatro artículos de `posts/`; no en la portada ni en `acerca.qmd`.
- No usar solicitudes de Cloudflare Workers/Workers AI ni operaciones D1 de YASE.

> Nota: la instalación de Giscus y los ajustes de categorías del repositorio requieren una persona con permisos de administración de la organización y no pueden darse por realizados solo por editar el código Quarto. Las reacciones requieren autenticación de GitHub; no son «Me gusta» anónimos.

## Lista de habilitación (administración GitHub)

1. Confirmar que `YaskCode-community/.github` sigue siendo público y tiene **Discussions** habilitado. Esta condición ya estaba confirmada el 31-10-2026.
2. En el GitHub de la organización, crear la categoría **Blog YaskCode** dentro de Discussions, con tipo **Announcement** (los lectores pueden comentar, pero las discusiones nuevas quedan reservadas a los moderadores y a Giscus).
3. Instalar la aplicación oficial **Giscus** en `https://github.com/apps/giscus`, eligiendo **Only select repositories** y autorizando exclusivamente `YaskCode-community/.github`, en vez de todos los repositorios.
4. Abrir `https://giscus.app/es`, indicar el repositorio `YaskCode-community/.github`, elegir la categoría **Blog YaskCode** y asignar mapeo por `pathname`, reacciones habilitadas, idioma español, tema claro, caja de comentarios debajo y carga diferida.
5. Obtener/verificar los identificadores reales de **repo-id** y **category-id** del generador Giscus. No inventarlos. El repo de Discussions tendrá su propio identificador; no usar el ID de `yaskcode-blog`.
6. Antes de publicar: abrir un artículo de prueba y verificar que aparece la caja, que requiere inicio de sesión GitHub para participar, que crea/enlaza una discusión en la categoría acordada y que el moderador puede gestionar comentarios.

## Integración pendiente en Quarto

Una vez que la aplicación esté instalada, la categoría creada y los identificadores confirmados, agregar **al nivel `website:`** de `_quarto.yml`:

```yaml
  comments:
    giscus:
      repo: YaskCode-community/.github
      repo-id: REEMPLAZAR_CON_ID_REAL
      category: Blog YaskCode
      category-id: REEMPLAZAR_CON_ID_REAL
      mapping: pathname
      reactions-enabled: true
      input-position: bottom
      loading: lazy
      language: es
      theme: light
```

**No copiar literalmente los marcadores `REEMPLAZAR_CON_ID_REAL` al sitio.** Son un ejemplo de configuración pendiente. Al habilitar la configuración global, las páginas principales tienen la marca `comments: false`, para que el widget solo se muestre en los artículos.

## Moderación y experiencia de lectura

- Aplicar [Código de conducta de YaskCode Community](https://github.com/YaskCode-community/.github/blob/main/CODE_OF_CONDUCT.md); moderar directamente desde GitHub Discussions.
- Los comentarios son públicos y pueden ser visibles también desde GitHub, no solo dentro del artículo.
- Giscus no ofrece comentarios anónimos: la participación requiere la autorización correspondiente de GitHub.
- Evitar publicar datos personales de estudiantes, calificaciones, información de salud o datos institucionales confidenciales.
- Si Giscus está temporalmente indisponible, los artículos deben seguir siendo legibles. La difusión, el RSS y Web Analytics continúan independientes.
- No publicar contadores de reacciones ni vistas simulados.

## Pruebas de aceptación (antes de marcar Fase 2 completada)

- [ ] Aplicación Giscus instalada solo en repositorio autorizado.
- [ ] Categoría **Blog YaskCode** existente y con tipo adecuado.
- [ ] `_quarto.yml` con IDs reales, sin placeholders.
- [ ] Portada y Acerca de sin comentarios; los cuatro artículos con comentarios y reacciones.
- [ ] Al menos una prueba real de moderación y reacción en la discusión correcta.
- [ ] Tema móvil, teclado, carga diferida y ausencia de solapamientos revisados.
- [ ] CI de Quarto correcto, PR aprobado, merge y despliegue de GitHub Pages exitoso.

Fuentes oficiales:
- https://giscus.app/es
- https://quarto.org/docs/reference/projects/websites.html
- https://docs.github.com/en/discussions/quickstart
- https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-categories-for-discussions
