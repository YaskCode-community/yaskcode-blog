# Migración · Primera entrega

## Alcance

GitHub conserva los originales; Quarto genera el blog. La publicación prevista es GitHub Pages. El Campus continúa en Astro. beehiiv conserva suscripciones y newsletter, y Apps Script → HubSpot sigue independiente.

## Fuente comprobada

- Artículo: https://yaskcode.beehiiv.com/p/rag-fundamentos-arquitectura
- Autora: Yaskelly Yedra. Publicación original: 21 de octubre de 2026.
- Fuente de migración: cuerpo HTML y metadatos del post publicado, recuperados con acceso autorizado a beehiiv el 30 de octubre de 2026.
- Conversación facilitada por la autora: el enlace de ChatGPT no fue accesible; no se utilizó como fuente del texto.
- Portada y diagrama descargados desde los originales de la publicación y guardados junto al artículo.
- El cuerpo se convirtió a Markdown sin reescribir sus párrafos. Se eliminaron atributos del editor y estilos en línea; se añadió texto alternativo al diagrama.
- Colores comprobados en el HTML del archivo público: magenta #B00091, lavanda #F5EFFA, blanco y texto oscuro.
- Áreas: Ingeniería de Software, Ciencia de Datos, Inteligencia Artificial y Cloud (etiqueta visible Cloud Computing).
- Secciones observadas en el archivo público: Radar tecnológico, Aprende, Práctica, Construye, Comparte, Explora y participa, Comunidad YaskCode. Se preservó Comparte al estar presente en el sitio actual.

## Decisiones de esta entrega

- Una única entrada real. No se publican artículos de relleno.
- Filtros combinables por área y sección, buscador por título y resumen, enlaces compartibles con parámetros y mensaje para filtros sin artículos.
- La búsqueda global de Quarto consulta el texto completo del sitio.
- Hasta confirmar un formulario incrustable existente, la suscripción enlaza a la landing actual de beehiiv, sin imitar un formulario que no envíe datos.
- El workflow de revisión construye y comprueba, pero no despliega.
- Las licencias concretas de código y materiales quedan pendientes de decisión editorial. No se concede una licencia nueva implícitamente.

## Pendiente antes de publicar

1. Validación visual de la autora en escritorio y móvil.
2. Revisar suscripción y, si procede, incorporar el formulario incrustable oficial.
3. Recuperar la carta editorial aprobada y contrastarla antes de sustituir la página Acerca provisional.
4. Decidir licencia de código y licencia de contenidos.
5. Acordar tratamiento de URLs antiguas y contenido duplicado entre beehiiv y el nuevo blog. No retirar el artículo anterior sin una estrategia.
6. Habilitar GitHub Pages y autorizar el workflow de despliegue después de aceptar la primera entrega.
7. Actualizar el enlace del Campus solo cuando el blog nuevo esté comprobado públicamente.
8. Preparar las cinco entradas adicionales por entregas, con contenido real y validación editorial.

## Comprobaciones realizadas

- Quarto 1.10.20: generación completa correcta.
- Comprobación de enlaces e imágenes locales: correcta.
- Comparación del contenido textual original con el artículo convertido: sin pérdidas de texto.
- JavaScript: sintaxis correcta; comprobación en Node de filtros combinados, búsqueda, estado vacío y restablecimiento.
- `git diff --check`: correcto.
- No se pudo abrir la vista local en el navegador de esta sesión. No se afirma validación visual ni de teclado/móvil. Debe completarse con `quarto preview` antes de aceptar el diseño.
- Se encontró un formulario inline existente en beehiiv. Sus ajustes son diferentes al magenta/lavanda del archivo: no se modificó ni incrustó automáticamente. Se conserva el acceso a la landing actual.
