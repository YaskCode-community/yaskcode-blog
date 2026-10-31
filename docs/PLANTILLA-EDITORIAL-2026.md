# Plantilla editorial YaskCode · Artículos Aprende

**Versión:** 2026-10-31 · **Estado:** cabecera aprobada y normalizada tras los PR #22, #23 y #24; plantilla operativa en revisión mediante PR.

Este modelo se adapta al tema. No exige crear cuatro publicaciones por tema: la ruta editorial utiliza generalmente **dos publicaciones principales**, **Aprende** (fundamentos) y **Practica** (laboratorio verificable). **Construye** se expresa en retos progresivos dentro del laboratorio y **Comparte** invita transversalmente a publicar evidencias, repositorios, aprendizajes y aportes de forma voluntaria.

**Fuentes operativas:** [plantilla Quarto Aprende](../plantillas/articulo-aprende/index.qmd), [plantilla Quarto Práctica](../plantillas/articulo-practica/index.qmd) y [plantilla Quarto de Comunidad](../plantillas/articulo-comunidad/index.qmd), todas fuera de `posts/` para que no entren al sitio como publicaciones. Las prácticas siguen su [estándar de reproducibilidad, ejercicios y recursos](ESTANDAR-PRACTICAS-LABORATORIOS.md). La [matriz de revisión de los cuatro artículos](REVISION-EDITORIAL-ARTICULOS-2026-10-31.md) registra qué se conserva y qué se adapta según el género.

## Claridad en la ficha del artículo

La cabecera debe presentar **«AUTORÍA: Yaskelly Yedra · Perfil académico · ORCID»** en una misma línea cuando haya espacio, sin separar el rótulo del nombre. El rótulo **AUTORÍA:** hereda el mismo estilo tipográfico en mayúsculas de **FECHA DE PUBLICACIÓN** y **FECHA DE ÚLTIMA MODIFICACIÓN**; se agrega una separación vertical moderada entre las etiquetas y la autoría. Los artículos técnicos muestran **BÁSICO / INTERMEDIO / AVANZADO** con exactamente el mismo estilo visual de las otras etiquetas de Quarto, sin añadir el nivel a las categorías temáticas, filtros ni RSS. Los relatos de comunidad no reciben nivel técnico.

No volver a escribir en el cuerpo una línea como **«Aprende · Área temática · Nivel Básico · Fundamentos»**: las dos categorías provienen del frontmatter Quarto y la etiqueta de nivel se añade desde `assets/article-tools.js`. La cabecera ya presenta etapa, área y nivel. El detalle del nivel (`level-detail`, por ejemplo «Fundamentos») puede permanecer como metadato pedagógico sin duplicarse en pantalla. Las narraciones de comunidad pueden conservar su descripción de género si aporta información adicional y no repite íntegramente una etiqueta.

El **subtítulo es la introducción visible** que presenta el propósito del artículo; la propiedad Quarto `description` se conserva como descripción SEO y de metadatos sociales, pero se oculta de la cabecera para evitar una segunda introducción repetida. Esto mantiene SEO y lectura sin redundancias, junto con el resumen detallado **«En 1 minuto»**, que tiene otra función didáctica.

## Cabecera compacta y participación

En pantallas amplias, colocar **💜 Me gusta** al lado de **«Imprimir o guardar como PDF»**, antes del bloque «Comparte este artículo». Pagemoji gestiona el **contador de corazones del artículo** de forma independiente a Giscus y a las visitas de Cloudflare: es un conteo aproximado, no usuarios únicos. No agregar reacciones negativas al artículo principal.

Mostrar **AUTORÍA: Yaskelly Yedra · Perfil académico · ORCID** sin repetir el nombre en otra línea, y reunir en una misma fila las fechas **Publicación** y **Última modificación**. En pantallas estrechas las fechas pueden apilarse para preservar legibilidad. Mantener los valores y la fecha editorial originales, sin ocultar cuándo se modificó el contenido.

## Componentes que ya deben estar en cada publicación

1. **Ficha de publicación:** título descriptivo, subtítulo, autor, fecha editorial, fecha de actualización si procede, área, etapa, nivel (solo artículos técnicos), portada y descripción para buscadores.
2. **«En 1 minuto»:** síntesis original de 2–4 frases. Debe explicar el problema, la idea central y un límite relevante; no sustituye el contenido.
3. **Tiempo de lectura aproximado:** se calcula en el navegador a ~220 palabras por minuto y aparece cerca de la autoría; es una estimación y no una promesa.
4. **Antes de comenzar:** conocimientos previos reales, audiencia y, en un laboratorio futuro, herramientas, versiones, licencias y costes.
5. **Aprende: fundamentos y arquitectura:** cuerpo pedagógico con conceptos precisos, decisiones, comparaciones, ejemplos claramente marcados y límites. No todos los temas necesitan una arquitectura de software; mantener el nombre que mejor describa el contenido.
6. **Fuentes:** referencias académicas y documentación técnica enlazadas y revisadas. Las entradas de comunidad (por ejemplo, el relato del Campus) usan fuentes y evidencias del proyecto, no bibliografía artificial.
7. **Recursos para llevar:** ficha real descargable como archivo Markdown `.md`. El artículo también ofrece «Imprimir o guardar como PDF» mediante el diálogo del navegador, sin afirmar que ya existe un PDF precompilado.
8. **Autoría verificable:** enlace al perfil académico y ORCID de la autora.
9. **Continuidad y conversación:** lecturas relacionadas, compartir y discusión Giscus. La reacción positiva es independiente del comentario.
10. **Calidad web:** Open Graph/Twitter Card, marcado `BlogPosting` de cada artículo, imágenes con `alt`, enlaces accesibles, navegación por teclado, diseño adaptable, y hojas de impresión. Validar CI antes de publicar.

### Verificación académica, SEO y accesibilidad

- La fecha `date` puede representar una **fecha editorial**. En `BlogPosting.datePublished` debe utilizarse la fecha real respaldada de primera publicación (si la original fue en beehiiv, identificarla), sin inventar una antigüedad web.
- `BlogPosting.author.url` enlaza un perfil público identificable. `sameAs` apunta a ORCID. Marcar `dateModified` cuando se publica una revisión real.
- Comprobar que Quarto genere portada social, descripción, un solo `h1`, sitemap y marcado estructurado legible.
- Revisar el orden de encabezados, contraste, foco visible, alternativas de imágenes, enlaces descriptivos, tamaños táctiles y lectura móvil. Las pruebas automáticas no certifican por sí solas WCAG 2.2.
- Las fichas no incluirán datos privados, trabajos estudiantiles sin permiso ni recursos descargables con licencias no verificadas.
- Las capturas o prototipos no deben describirse como un experimento o evaluación educativa, salvo evidencia publicada.

## Plantilla Quarto de una publicación Aprende

La plantilla que debe copiarse al crear una entrada es **[`plantillas/articulo-aprende/index.qmd`](../plantillas/articulo-aprende/index.qmd)**. Este documento explica las reglas; el archivo `.qmd` es la fuente única del esqueleto, para no mantener dos ejemplos que puedan divergir.

| Campo o componente | Regla editorial |
| --- | --- |
| `title` | Título específico, sin repetir área y etapa en una segunda línea. |
| `subtitle` | **Única entrada introductoria visible**: propósito o promesa de aprendizaje. |
| `description` | Descripción breve para SEO y redes; no se vuelve a mostrar visualmente debajo del subtítulo. |
| `categories` | Solo etapa y área temática; p. ej. `["Aprende", "Inteligencia Artificial"]`. |
| `editorial-section` y `area` | Valores coherentes con categorías y filtros de portada. |
| `level` | **Básico, Intermedio o Avanzado** según conocimientos, autonomía, alcance y verificación; **no agregarlo a `categories`**. |
| `level-detail` | Información pedagógica opcional como `Fundamentos`, sin repetirla como subtítulo del cuerpo. |
| `date` / `date-modified` | Fechas reales y justificables; `date-modified` solo para una revisión publicada. |
| `image` / `image-alt` | Archivo real y texto alternativo útil; evitar recursos inexistentes. |
| `draft` | Siempre `true` hasta aceptación y comprobación de publicación. |
| `format.html.include-in-header` | Referencia a metadatos por artículo comprobados; el archivo SEO debe existir. |

### Orden visual aprobado

1. Título y controles `💜 Me gusta` + `Imprimir o guardar como PDF`; bloque **Comparte este artículo** sin recuadro superior.
2. Subtítulo único y tres etiquetas visualmente iguales: **APRENDE · ÁREA TEMÁTICA · BÁSICO** (nivel equivalente según proceda).
3. **AUTORÍA: Yaskelly Yedra · Perfil académico · ORCID** en una fila cuando exista espacio, con la tipografía del rótulo de fechas y aire respecto de las etiquetas.
4. Fecha de publicación, última modificación cuando corresponda, tiempo estimado de lectura y vistas agregadas verificadas.
5. Inicio del contenido: **«En 1 minuto»** (salvo recursos gráficos propios necesarios antes de ese bloque), seguido de «Lo que aprenderás», «Antes de comenzar» y el desarrollo. No agregar una línea manual repitiendo las etiquetas.
6. Ficha descargable, bibliografía real, continuidad y participación según el tema.

La cabecera y los controles se generan desde Quarto y `assets/article-tools.js`; **no se duplican a mano en el `.qmd`**. Registrar cada artículo nuevo en la configuración actual del JavaScript, junto con su nivel y enlaces relacionados. También deben existir la portada, la ficha `recursos/<slug>-ficha.md` y los metadatos estructurados correspondientes. Las vistas y pruebas automáticas actuales contienen rutas de artículos conocidas: actualizarlas expresamente al añadir nuevas entradas. No asumir que copiar el archivo publica o registra automáticamente el artículo.

### Niveles de complejidad

| Nivel | Conocimientos previos y autonomía | Alcance y validación esperada |
| --- | --- | --- |
| **Básico** | Puede comenzar con nociones introductorias y guía explícita | Comprende conceptos, interpreta un ejemplo y realiza comprobaciones sencillas. |
| **Intermedio** | Integra conceptos y toma algunas decisiones técnicas | Compara alternativas, adapta un ejemplo y justifica pruebas. |
| **Avanzado** | Maneja fundamentos y resuelve decisiones con más autonomía | Integra componentes, explicita compromisos técnicos y aporta evaluación más exigente. |

El nivel **no depende del número de páginas**, ni debe convertirse en una promesa de dificultad sin revisar el contenido. Los relatos de comunidad no exigen un nivel técnico.

### Lista mínima antes de publicar

- [ ] Sustituir todos los marcadores `REEMPLAZAR` y fechas de ejemplo; conservar `draft: true` hasta el cierre editorial.
- [ ] Confirmar que no se repitan título, subtítulo, categorías ni nivel en el cuerpo.
- [ ] Revisar objetivos, conocimientos previos, fuentes, límites y coherencia con el nivel.
- [ ] Verificar imágenes, ficha de lectura, SEO `BlogPosting`, atribución y licencias.
- [ ] Registrar slug, nivel, relacionados, datos de portada y seguimiento técnico necesarios sin inventar métricas.
- [ ] Ejecutar `quarto render`, `python3 scripts/check_site.py` y controles de GitHub Actions; revisar escritorio, móvil y teclado.
- [ ] Obtener aceptación editorial antes de quitar `draft: true`, fusionar o publicar.

## Material didáctico reservado para una segunda intervención

**Estado: pendientes de desarrollo, revisión y evidencia suficiente. No fingir que están completados.**

| Línea | Qué deberá estar disponible antes de publicar | Prueba de aceptación |
| --- | --- | --- |
| **Resultados de aprendizaje verificables** | Competencias u objetivos operacionales, instrumento y criterio observable; actividades reales y datos anonimizados cuando existan | Se puede demostrar qué se evaluó y qué no; distinguir objetivos de resultados logrados |
| **Diagramas y ejemplos originales** | Modelo/diagrama creado o adaptado con autoría, explicación, propósito y condiciones de uso | Figura legible, texto alternativo y correspondencia con el concepto; evitar figuras sin procedencia |
| **Código y laboratorio reproducible (Practica)** | Repositorio, versiones, requisitos, datos autorizados o sintéticos, pasos ejecutables y prueba/salida esperada | Otra persona puede reproducir la práctica y comparar resultados |
| **Retos progresivos y evaluación (Construye)** | Retos Básico/Intermedio/Avanzado, entregables, rúbrica/criterios y evidencias | Se puede comprobar el cumplimiento por nivel sin confundir tareas con aprendizaje medido |

**Estado de partida:** RAG y POO ya contienen *algunos diagramas y ejemplos conceptuales*, y los artículos Aprende incluyen objetivos y preguntas de comprensión. Se conservarán; la mejora pendiente es validarlos, documentarlos y enlazarlos a prácticas/evidencias cuando estén listas. El relato del Campus no requiere pruebas de programación ni niveles técnicos.

## Enlaces normativos y documentación

- Quarto · metadatos sociales: https://quarto.org/docs/websites/website-tools.html
- Google Search Central · Article/BlogPosting: https://developers.google.com/search/docs/appearance/structured-data/article
- WCAG 2.2: https://www.w3.org/TR/WCAG22/

*No se atribuyen reconocimientos ni resultados a una publicación solamente por aplicar este esquema.*
