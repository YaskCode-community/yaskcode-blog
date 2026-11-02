# Aplicación del estándar editorial a los cuatro artículos · 31 de octubre de 2026

**Estado:** revisión editorial de archivos fuente completada; la comprobación automática y la revisión visual posterior al despliegue se registran por separado.

**Norma:** [guía editorial](GUIA-EDITORIAL.md) · [estándar de publicación](PLANTILLA-EDITORIAL-2026.md). La cabecera compacta, autoría, fechas, controles sociales y estilo de nivel son **comunes**: se generan desde Quarto, `assets/article-tools.js` y `assets/theme.scss`, no se duplican en cada artículo.

## Matriz de revisión

| Publicación | Tipo y nivel | Componentes de la plantilla | Decisión editorial |
| --- | --- | --- | --- |
| [RAG: fundamentos y arquitectura](../posts/rag-fundamentos-arquitectura/index.qmd) | Aprende · IA · Básico | Subtítulo único, etiquetas en cabecera, resumen, objetivos, prerrequisitos, ficha, fuentes y continuidad | Referencia visual aprobada; no modificar en esta intervención. |
| [Hugging Face: modelos y datasets](../posts/hugging-face-modelos-datasets-ciencia-de-datos/index.qmd) | Aprende · Ciencia de Datos · Básico | Resumen «En 1 minuto», «Lo que aprenderás», «Antes de comenzar», ficha, verificación de aprendizaje, bibliografía, futura práctica y participación | **Ya cumple** el estándar. Conservar portada, objetivos, ejemplos, fuentes y fecha; no reescribir solo por uniformidad. |
| [POO en la era de la IA](../posts/por-que-aprender-poo-en-la-era-de-la-ia/index.qmd) | Aprende · Ingeniería de Software · Básico | Los mismos componentes; ejercicio de inventario, comprobaciones, fuentes y laboratorio proyectado | **Ya cumple** el estándar. Conservar las fechas editoriales y de primera publicación, sin inventar resultados educativos. |
| [Historia de Campus YaskCode](../posts/historia-campus-yaskcode/index.qmd) | Comunidad YaskCode · historia de origen · **sin nivel técnico** | «En 1 minuto», «Qué encontrarás», «Antes de comenzar», ficha, relato, fuentes propias del proyecto e invitación a participar | Retirar rótulo manual repetido, organizar prerrequisitos y añadir orientación narrativa. No convertir un testimonio en laboratorio ni añadir una bibliografía artificial. |

## Regla editorial de aplicación

- **Aprende**: mantener la etiqueta de etapa y área, más el nivel (Básico/Intermedio/Avanzado) según prerrequisitos, autonomía y verificación, no por longitud. No añadir el nivel a `categories`.
- **Comunidad YaskCode**: mantener solo la categoría comunitaria, identificar el tipo de relato mediante `article-type` y el propio contenido, sin nivel técnico y sin repetir una etiqueta manual.
- **Presentación**: el subtítulo debe cumplir el papel de introducción visible; `description` se reserva para SEO. El resumen «En 1 minuto» no debe ser una copia del subtítulo. Las imágenes pueden aparecer al comienzo cuando aportan contenido independiente.
- **Autoría y transparencia**: mantener nombre, perfil académico, ORCID, fechas existentes, fuentes y aclaración de experiencias hipotéticas, prototipos o resultados medidos.
- **Participación**: no inventar laboratorios publicados. En artículos técnicos, ofrecer la transición futura a *Practica* sin enlaces ficticios; en relatos, invitar a explorar o conversar sin obligar a compartir información privada.
- **Reutilización**: usar `plantillas/articulo-aprende/index.qmd` o `plantillas/articulo-comunidad/index.qmd`, según el tipo. Ambas son borradores con marcadores; copiar y publicar exige completar sus recursos y metadatos específicos.

## Comprobaciones y límites

- [x] Inspección de los cuatro archivos `.qmd` y sus metadatos en GitHub.
- [x] Verificado que Hugging Face y POO ya cumplen la estructura editorial aprobada; sus contenidos se conservan sin cambios.
- [x] Historia del Campus adaptada al género narrativo, sin nivel ni etiqueta manual duplicada.
- [x] Plantilla narrativa separada de la plantilla didáctica.
- [ ] GitHub Actions: `quarto render` + pruebas del repositorio.
- [ ] Revisión visual de las páginas en escritorio y móvil tras aceptar y publicar los cambios.
- [ ] Verificación manual de enlaces externos, lectura con teclado y comportamiento de widgets; el CI no equivale a certificación WCAG.

## Próximo pendiente · Primer laboratorio Practica · RAG

- [ ] **Diseñar, implementar, verificar y publicar «Practica · RAG»**, como continuación del artículo [«RAG: fundamentos y arquitectura para comenzar»](../posts/rag-fundamentos-arquitectura/index.qmd).
- **Propósito:** realizar la **primera prueba completa del recorrido editorial Aprende → Practica → Construye → Comparte**, sin confundir el laboratorio con una evaluación formal de impacto educativo.
- **Practica:** laboratorio guiado y reproducible con objetivo, conocimientos previos, herramientas y versiones, datos públicos o sintéticos autorizados, pasos, código ejecutable, resultados esperados y verificaciones.
- **Construye:** retos de aplicación progresivos (Básico, Intermedio y Avanzado, cuando correspondan), con criterios de aceptación y evidencias.
- **Comparte:** invitación voluntaria a publicar repositorios, observaciones, errores y aprendizajes con respeto a licencias, privacidad y autoría.
- **Criterios de cierre:** otra persona puede reproducir el laboratorio y contrastar resultados; se documentan limitaciones, pruebas, versiones y fuentes; el artículo Aprende enlaza al laboratorio **solo después** de su publicación verificada.
- **Estado:** pendiente de planificación y elaboración; **no** existe todavía un laboratorio publicado ni resultados experimentales validados que podamos atribuirle.

**Alcance:** esta revisión no altera comentarios de Giscus, corazones Pagemoji, métricas históricas, ni los repositorios Campus/YASE. No supone una evaluación formal del aprendizaje ni publicación de laboratorios todavía pendientes.
