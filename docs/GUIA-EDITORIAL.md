# Guía editorial del Blog YaskCode

Versión revisada · 31 de octubre de 2026. Guía propia para orientar la publicación y revisión; incorpora la cabecera y plantilla Quarto aprobadas mediante la revisión visual de artículos.

## Propósito y público

Ayudar a estudiantes, docentes y comunidad tecnológica a transformar conocimientos de Ingeniería de Software, IA, Ciencia de Datos y Cloud en prácticas, proyectos y aportes compartidos.

Nuestra promesa editorial es que cada entrada aporte una comprensión, una acción o una reflexión útil, acompañada de fuentes o evidencias acordes con lo que afirma. El idioma principal es el español; las traducciones se identifican y revisan.

## El recorrido Aprende · Practica · Construye · Comparte

La unidad de planificación preferida es una **ruta temática**: una pregunta o problema que puede abordarse con varias publicaciones relacionadas. Cada entrada tiene una etapa principal, un área, un público y un objetivo concreto.

| Etapa | Pregunta editorial | Contenido esperado | Evidencia apropiada |
| --- | --- | --- | --- |
| Aprende | ¿Qué necesita comprender la persona y por qué? | Concepto, ejemplo, límites y pregunta de comprensión. | Fuentes contrastadas y explicación propia. |
| Practica | ¿Qué puede probar y cómo sabrá si lo consiguió? | Actividad breve, requisitos, pasos y comprobación. | Entrada de ejemplo, salida esperada o criterio para valorar una respuesta abierta. |
| Construye | ¿Qué problema puede resolver integrando ese conocimiento? | Reto, decisiones, implementación, pruebas y variantes. | Código o artefacto, instrucciones y resultados con su contexto. |
| Comparte | ¿Qué aprendizaje puede servir a otros y cómo pueden aportar? | Relato crítico, resultados, errores, mejoras y reconocimiento de autores. | Enlaces verificables y una invitación concreta a discutir o contribuir. |

**Para un mismo tema priorizamos dos publicaciones principales:** una entrada **Aprende** con fundamentos, ejemplos, referencias y límites; y una entrada **Practica** con laboratorio guiado, reproducible y resultados verificables. **Construye** se incorpora mediante retos progresivos dentro del laboratorio (Básico, Intermedio y Avanzado cuando tenga sentido), y **Comparte** es una invitación transversal a compartir evidencias y aprendizajes voluntariamente. No es obligatorio publicar cuatro entradas por cada tema.

El recorrido es flexible: se puede entrar por un proyecto y volver a sus fundamentos. Una serie debe señalar los pasos ya disponibles y distinguir los previstos. No creamos enlaces a artículos inexistentes ni publicamos contenido de relleno para completar etapas.

**Ejemplo de planificación, todavía no una serie completa publicada:** RAG — fundamentos; práctica de recuperación sobre documentos de ejemplo; prototipo pequeño con pruebas; relato de resultados y límites. Solo la entrada de fundamentos está migrada en esta entrega.

## Secciones complementarias

| Sección | Función | Condición para publicar |
| --- | --- | --- |
| Radar tecnológico | Ayudar a entender una novedad y decidir si merece explorarse. | Fuente primaria, fecha, contexto y límites; identificar opinión o inferencia. |
| Explora y participa | Conectar con cursos, eventos, recursos y oportunidades. | Enlace oficial, fecha de comprobación y condiciones verificadas; no presentar como gratuita una oferta sin confirmación. |
| Comunidad YaskCode | Visibilizar experiencias y facilitar colaboración. | Autoría reconocida, permiso para materiales ajenos y explicación del aporte. |

El blog desarrolla contenidos con profundidad y conserva sus versiones. La newsletter puede seleccionar una idea central, enlazar una explicación y una actividad disponibles, destacar una oportunidad y cerrar con una pregunta. No tiene que incluir todas las secciones en cada envío. La frecuencia se adapta a la capacidad de revisión.

## Ficha mínima de una propuesta

Antes de redactar, responde:

- ¿A quién se dirige y qué conocimientos previos necesita?
- ¿Qué pregunta resuelve y qué podrá comprender, probar o construir la persona?
- ¿En qué área y etapa del recorrido encaja?
- ¿Qué fuentes y recursos se utilizarán?
- ¿Cómo se comprobará lo que se enseña o afirma?
- ¿Qué parte podrá elegir, adaptar o cuestionar quien aprende?
- ¿Qué siguiente paso o aportación se invitará a realizar?

## Presentación editorial aprobada · 31 de octubre de 2026

La revisión visual de la cabecera quedó aceptada: **APRENDE · ÁREA TEMÁTICA · BÁSICO** aparece como un conjunto uniforme de tres etiquetas; el nivel es un metadato pedagógico separado de las categorías. **AUTORÍA:** va en mayúsculas, con la tipografía de los rótulos de fechas, los enlaces Perfil académico y ORCID en la misma fila cuando haya espacio y un margen de separación respecto de las etiquetas.

El **subtítulo** es la única introducción breve visible (la propiedad `description` se conserva para SEO). No se repite como texto manual la línea «Aprende · Área · Nivel Básico · Fundamentos»: fue retirada de RAG, Hugging Face y POO en el PR #24. El resumen **«En 1 minuto»** tiene función pedagógica y no debe repetir literalmente ese subtítulo.

Los artículos existentes incluyen conocimientos previos, fichas descargables, tiempo estimado, referencias de autoría y SEO. El bloque superior «Comparte este artículo» se integra sin un contenedor visual; **💜 Me gusta** e **Imprimir o guardar como PDF** comparten fila cuando hay espacio. Conservar las fechas reales y presentar vistas y reacciones como métricas de participación, nunca como indicadores de aprendizaje.

Para nuevas entradas se usa la [plantilla editorial y lista de verificación](PLANTILLA-EDITORIAL-2026.md). Las entradas técnicas **Aprende** parten del [archivo Quarto de aprendizaje](../plantillas/articulo-aprende/index.qmd); las historias de origen y experiencias comunitarias usan la [plantilla narrativa de Comunidad](../plantillas/articulo-comunidad/index.qmd), sin nivel técnico ni una estructura de laboratorio forzada. Ambos archivos están fuera de la carpeta de publicaciones y contienen marcadores que deben sustituirse: no se publican automáticamente. La [matriz de revisión de los cuatro artículos](REVISION-EDITORIAL-ARTICULOS-2026-10-31.md) documenta la aplicación por género y sus límites.

**Niveles:** Básico, Intermedio y Avanzado se asignan por prerrequisitos, autonomía, alcance técnico y verificaciones; no por longitud. Los artículos de comunidad pueden no llevar nivel técnico.

La plantilla también registra mejoras que requieren material nuevo y evidencia: resultados de aprendizaje verificables, diagramas complementarios, laboratorios reproducibles y retos por niveles.

## Estructura orientativa de un artículo

1. **Situación y objetivo:** problema, público y resultado de aprendizaje.
2. **Fundamentos o requisitos:** conceptos previos, herramientas, versiones y costes cuando apliquen.
3. **Desarrollo:** explicación o actividad con decisiones razonadas.
4. **Comprobación:** ejemplo, criterio de logro, prueba o resultados observados.
5. **Reflexión:** interpretación, límites, errores y alternativas.
6. **Continuidad:** recurso relacionado y una invitación concreta a practicar o aportar.
7. **Créditos:** autoría, fuentes, fecha y condiciones de reutilización conocidas.

No todas las entradas necesitan siete encabezados. El contenido determina la estructura.

## De los laboratorios y YASE al blog

**Nueva línea editorial pendiente:** [migración de seis wikis de Sistemas Inteligentes a casos académicos del Blog](PLAN-MIGRACION-SEIS-WIKIS-SISTEMAS-INTELIGENTES-2026.md). Será una adaptación autorizada y revisada, **no** una copia pública automática: conservar autoría del estudiantado, rol de edición docente, fecha académica original y fecha real de primera publicación web, sin modificar wikis o repositorios privados. Antes del primer caso habrá que adaptar los componentes de autoría del blog, diseñados actualmente para una sola autora.

Una experiencia se convierte en artículo cuando hay algo útil que explicar y suficiente evidencia para sostenerlo. Registrar problema, entorno, decisiones, pruebas, resultados y límites ayuda a escribir sin reconstruir la historia de memoria.

Antes de compartir trabajos de estudiantes o colaboradores, acordar atribución y autorización; publicar ejemplos anonimizados o datos sintéticos cuando corresponda. Nunca incluir credenciales, contactos, expedientes ni datos privados.

Un prototipo funcional demuestra un comportamiento en un contexto concreto. Para afirmar una mejora educativa necesitamos información del aprendizaje: actividad utilizada, participantes descritos de manera agregada, criterio de evaluación, resultados y límites. Una simulación o una captura no demuestra por sí sola impacto en estudiantes.

## Criterios propios de revisión

Esta lista es una herramienta original de YaskCode. No reproduce ni aplica la escala, los descriptores o las ponderaciones de una rúbrica de concurso. Usamos tres estados: **listo, requiere ajuste, no aplica**, con una nota y una evidencia. No calculamos una supuesta puntuación del jurado.

| Criterio YaskCode | Pregunta para revisar | Evidencia que podemos aportar |
| --- | --- | --- |
| Utilidad | ¿La persona sabe qué podrá aprender o hacer? | Objetivo y actividad alineados con su nivel. |
| Exactitud | ¿Las afirmaciones y resultados tienen sustento? | Fuentes, versiones, comprobaciones y límites. |
| Aplicabilidad | ¿Hay suficiente información para intentar o adaptar la propuesta? | Requisitos, datos de ejemplo, instrucciones y validación. |
| Decisiones y reflexión | ¿Se explica el porqué y se invita a pensar? | Alternativas, preguntas abiertas y análisis de errores. |
| Acceso | ¿Se puede leer y recorrer con distintos dispositivos y recursos? | Revisión móvil y de teclado; alternativas textuales; costes explícitos. |
| Aporte compartido | ¿Queda una forma concreta de continuar o mejorar el trabajo? | Recurso accesible, atribución y canal de contribución. |
| Trazabilidad | ¿Se conoce el origen y estado de la publicación? | Autoría, fechas, referencias y correcciones. |

Para experiencias docentes, añadir un registro de la actividad, el acompañamiento ofrecido, las decisiones del alumnado y la forma de valorar el aprendizaje. Registrar también dificultades y resultados que no confirmen nuestras expectativas.

## Del borrador a la publicación

**Propuesta → borrador → revisión editorial → comprobación técnica y accesible → aceptación → publicación → seguimiento.**

Una misma persona puede cubrir varias revisiones; no se afirma arbitraje ni revisión independiente si no ha ocurrido. Los borradores en GitHub público son visibles aunque no se incluyan en el sitio.

La revisión humana es responsable del texto, las referencias y el código, incluso si se usó IA. Declarar su uso sustancial de forma concreta: por ejemplo, apoyo en redacción, código o imágenes y cómo se revisó. No atribuirle experimentos que no se realizaron.

Las correcciones relevantes deben indicar qué cambió y cuándo. Conservar las fechas originales de textos migrados y distinguirlas de sus actualizaciones.

## Cómo sabremos si estamos aportando

Recoger, cuando exista consentimiento y sea viable, evidencia de prácticas realizadas, proyectos adaptados, correcciones recibidas, dificultades resueltas y colaboraciones. Para datos agregados, indicar periodo, fuente y límites; no fijar metas inventadas ni atribuir causalidad a simples coincidencias.

Las visitas y suscripciones describen alcance. Los trabajos y explicaciones de quienes aprenden ayudan a valorar aprendizaje. Un reconocimiento externo acredita únicamente la distinción que se haya obtenido, con su fecha y categoría.

## Referencias externas y revisión

La consulta del [Premio Internacional Espiral](CONVOCATORIAS.md) ayuda a contrastar nuestras decisiones. Su rúbrica publicada trata aspectos educativos como aprendizaje, evaluación e inclusión, y declara restricciones de uso y reproducción: enlazamos al original y mantenemos nuestra herramienta propia.

Revisaremos esta guía cuando una experiencia publicada revele una mejora necesaria, cambien las herramientas o se preparen candidaturas. No cambiamos la misión del blog para perseguir una categoría.
