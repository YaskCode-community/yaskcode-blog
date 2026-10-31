# Plan de migración editorial · Seis wikis de Sistemas Inteligentes al Blog YaskCode

**Registro inicial:** 31 de octubre de 2026  
**Estado:** propuesta de trabajo **pendiente**; no se han clonado las wikis ni creado/publicado sus artículos.  
**Origen:** seis equipos de proyectos académicos de **Sistemas Inteligentes**, Maestría en Tecnologías de Información y Comunicación, Universidad del Zulia. Repositorios de `YaskCode-laboratory`.  
**Destino:** [Blog YaskCode (Quarto)](https://yaskcode-community.github.io/yaskcode-blog/), en `YaskCode-community/yaskcode-blog`.  
**Referencia editorial:** [guía editorial](GUIA-EDITORIAL.md) · [estándar Quarto](PLANTILLA-EDITORIAL-2026.md) · [revisión de cuatro artículos publicados](REVISION-EDITORIAL-ARTICULOS-2026-10-31.md).

## 1. Propósito y decisión

Convertir **copias autorizadas** de las seis wikis académicas en hasta **seis artículos de casos de estudio**, conservando su procedencia, autoría y fechas verificables. El contenido se adaptará para una audiencia abierta, con rigor académico, enlaces, imágenes y accesibilidad; **no se copiará automáticamente a producción**.

El original académico permanece en cada repositorio/wiki de GitHub, con su visibilidad, archivos e historial intactos. El Blog publica únicamente una **adaptación editorial revisada y aprobada**, no la documentación interna completa ni una réplica de código privado.

**Tipo editorial propuesto:** «Caso de estudio académico» dentro de **Comunidad YaskCode**, con relación temática a Inteligencia Artificial / Ingeniería de Software según el proyecto. No crear una categoría nueva ni añadir `BÁSICO` o `INTERMEDIO` a los seis artículos por defecto. Solo asignar nivel pedagógico a un eventual artículo didáctico específico, después de examinar el contenido.

## 2. Inventario y control de acceso

Los seis repositorios existen y se verificó su visibilidad en GitHub el 31-10-2026. La existencia de un repositorio **no garantiza** que su wiki pueda clonarse, esté completa ni que exista permiso para republicarla.

| Equipo | Repositorio de origen | Visibilidad verificada | Contenido wiki y autorizaciones |
| --- | --- | --- | --- |
| 1 | `wellness-platform-team1` | Público | Pendientes de revisar y autorizar |
| 2 | `wellness-platform-team2` | Privado | Pendientes de revisar y autorizar |
| 3 | `wellness-platform-team3` | Privado | Pendientes de revisar y autorizar |
| 4 | `wellness-platform-team4` | Privado | Pendientes de revisar y autorizar |
| 5 | `wellness-platform-team5` | Privado | **Piloto propuesto**; revisar wiki completa y autoría |
| 6 | `wellness-platform-team6` | Público | Pendientes de revisar y autorizar |

**Privacidad:** no incluir el contenido de las wikis privadas, nombres de participantes, enlaces a archivos privados, capturas internas, datos identificables ni documentos de autorización en este repositorio público. El inventario detallado con consentimiento y permisos debe gestionarse en un espacio privado y con acceso restringido.

## 3. Autoría, edición y fechas: regla obligatoria

Antes de redactar **cada** artículo, contrastar la portada y el historial de la wiki con README, commits y con la confirmación del equipo. Los commits prueban cambios de Git, pero **no bastan por sí solos para asignar autoría intelectual**.

| Dato | Cómo documentarlo en el artículo y en el registro de trabajo |
| --- | --- |
| **Autoría original** | Nombres y orden de quienes efectivamente contribuyeron al trabajo, confirmados por el equipo y con autorización para su identificación pública. Si alguien no desea aparecer, acordar una atribución autorizada alternativa. |
| **Coordinación/edición** | «Revisión académica y adaptación editorial: YaskCode / Yaskelly Yedra» **separada** de la autoría del estudiantado. Atribuir coautoría solo cuando corresponda al aporte real y exista acuerdo explícito. |
| **Fecha del proyecto o de la wiki** | Indicar como fecha de elaboración académica o periodo del curso, según evidencia de wiki/commits/entrega. No inventar el día de creación si solo se sabe el semestre. |
| **Versión de origen** | Registrar identificador de revisión/commit o copia autorizada y fecha de extracción en el expediente **privado** de procedencia. |
| **Fecha de publicación del Blog** | Usar la fecha **real de la primera publicación web** del artículo adaptado para `datePublished` y la cabecera; no retrotraerla a la fecha del semestre o de la wiki. |
| **Fecha de actualización** | `dateModified` solo cuando se publique efectivamente una revisión, manteniendo historial. |
| **Enlaces y permisos** | Enlazar el origen solo cuando sea público y la exposición esté autorizada; para privados, ofrecer créditos acordados **sin revelar URL o contenido reservado**. |

**Texto orientativo de créditos, para adaptar a cada caso (no publicar marcadores):**

> **Autores del trabajo académico:** [nombres confirmados por el equipo].  
> **Proyecto original:** Sistemas Inteligentes, Maestría TIC, Universidad del Zulia; [periodo/fecha verificable].  
> **Adaptación al Blog YaskCode:** [personas responsables de la edición].  
> **Primera publicación de esta adaptación:** [fecha real].  
> **Fuente y alcance:** adaptación autorizada de una wiki académica; se preserva el original y solo se muestran materiales aprobados.

**Regla de licencias:** ni la visibilidad pública de GitHub ni la existencia de una licencia del código autorizan automáticamente la republicación de texto, diagramas, fotografías, datos o contribuciones de terceros. Acordar permisos y condiciones de reutilización antes de publicar. La coordinación docente no sustituye el consentimiento de las personas autoras.

## 4. Piloto y conversión técnica (sin alterar el repositorio de origen)

Comenzar por **Equipo 5**, únicamente si hay acceso y permiso de lectura. La captura del proyecto sirve para definir el piloto, pero **no sustituye** la revisión de la wiki completa. En particular, revisar con cuidado cualquier afirmación sobre salud, seguridad, desempeño, validación clínica o resultados cuantitativos: distinguir metas, resultados internos, prototipos y validaciones externas verificadas.

1. **Acceso y copia:** con una cuenta autorizada y Git, intentar clonar la wiki como un repositorio independiente (`<repositorio>.wiki.git`). Ejemplo de comando para el equipo piloto:

   ```bash
   git clone https://github.com/YaskCode-laboratory/wellness-platform-team5.wiki.git
   ```

   Es una operación de lectura/copia local; no modifica la wiki ni hace público el repositorio. Si no hay contenido o falta acceso, registrar el bloqueo; **no** cambiar la privacidad del repositorio para solucionarlo. No incorporar credenciales/tokens en el comando ni en documentos públicos.
2. **Inventariar el material:** Markdown, páginas, adjuntos, imágenes, diagramas, referencias, enlaces internos/externos, autores y versión/fecha disponibles. Comprobar qué recursos realmente son parte de la wiki; no asumir que todo está en el clon.
3. **Curaduría:** seleccionar el problema, objetivos, fundamentos, arquitectura/decisiones, implementación relevante, pruebas y límites. El artículo puede sintetizar varias páginas, pero nunca presentar una afirmación sin sustento o afirmar que el prototipo es un sistema validado en producción.
4. **Adaptación Quarto:** crear **borrador** en `posts/<slug-aprobado>/index.qmd` con imágenes autorizadas y accesibles, portada y SEO propios. Los enlaces relativos y diagramas deben funcionar en el blog. Registrar la procedencia sin publicar materiales privados.
5. **Atribución y revisión del equipo:** presentar copia previa para verificar nombres, orden, rol, fechas, citas, exclusiones, imagen/diagramas y cualquier derecho de terceros. Guardar permisos en expediente privado.
6. **Aceptar y publicar por equipo:** CI Quarto, revisión de enlaces/SEO/accesibilidad, validación editorial, PR de cada caso, autorización expresa para merge y comprobación pública posterior. La wiki original continúa intacta.

**Ruta de trabajo propuesta:** `posts/caso-estudio-equipo-5/index.qmd` como marcador de planificación, **no ruta definitiva ni archivo creado**. El nombre y slug finales se fijan tras revisar el tema real y la autorización editorial.

## 5. Estructura orientativa de cada caso de estudio

1. Título específico, subtítulo único, tipo **Caso de estudio** y área temática coherente con la portada del Blog.
2. **«En 1 minuto»**: problema, enfoque y límite; sin duplicar el subtítulo.
3. **El proyecto y su contexto**: propósito, curso, alcance, equipo y créditos verificados.
4. **Investigación y fundamentos**: conceptos realmente investigados, fuentes y preguntas.
5. **Diseño y construcción**: arquitectura, decisiones, tecnologías y diagramas autorizados.
6. **Validación**: qué se probó, cómo, evidencias disponibles, resultados observados y lo que aún no se comprobó.
7. **Lecciones aprendidas y límites**, incluyendo consideraciones técnicas y éticas.
8. **Autoría, procedencia y fechas** diferenciadas (trabajo original, adaptación y publicación web).
9. **Continúa explorando / Comparte**: recursos públicos aprobados y conversación de Giscus; participación voluntaria de autores y lectores.

No es obligatorio usar idéntico número de secciones en los seis artículos. La **autoría, privacidad, accesibilidad y fiabilidad** sí son requisitos comunes.

## 6. Adecuación necesaria del Blog antes del primer caso

El código actual está optimizado para los cuatro artículos de una misma autora; **no sería correcto reutilizarlo sin cambios** para publicaciones con equipos de estudiantes:

- `assets/article-tools.js`: la función de cabecera agrega el **perfil académico y ORCID de Yaskelly** a la primera línea de autoría de cada artículo. Debe admitir **múltiples autores y créditos por artículo**, mostrar el perfil/ORCID de una persona **solo cuando corresponda**, y distinguir «Edición académica» de «Autoría».
- `assets/cards.ejs.md`: revisar la presentación de listas de autores en las tarjetas del Blog, evitando nombres concatenados incorrectamente o atribuciones genéricas.
- SEO `BlogPosting`: crear el campo `author` con las personas efectivamente autoras (lista si son varias), `datePublished` real y `dateModified` justificado; registrar `editor` o `contributor` sin atribuir falsamente el artículo a Yaskelly.
- `scripts/check_site.py`: hoy presupone **cuatro artículos**, perfiles ORCID y rutas conocidas; generalizar verificaciones sin exigir el ORCID de una sola autora a todos.
- `assets/article-tools.js`, tarjetas/filtros y estadísticas: registrar los nuevos slugs y relacionados, sin generar valores falsos de visitas o reacciones ni exponer datos no autorizados.
- **Giscus** ya está configurado para `YaskCode-community/.github` mediante la URL/ruta del artículo. Probar comentarios al publicar cada caso; la wiki original no se convierte en el destino de los comentarios.

Estos cambios se planifican en una entrega técnica separada y deben validarse **antes** de publicar el primer caso.

## 7. Presupuesto de planificación planteado: seis horas

**Hipótesis de la propuesta de la autora: 6 h de trabajo sobre materiales ya accesibles y con permisos resueltos. No es un compromiso de ejecución ni una garantía de publicación integral.**

| Bloque de planificación | Presupuesto orientativo |
| --- | ---: |
| Inventario, comprobación de copias disponibles y metadatos | 45 min |
| Piloto editorial y conversión de la wiki del Equipo 5 | 75 min |
| Primera adaptación de las otras cinco wikis, 40 min por equipo | 200 min |
| Revisión de consistencia, enlaces, créditos y control inicial | 40 min |
| **Total de referencia** | **360 min (6 horas)** |

**Supuestos:** wikis descargables, equipo/autoría confirmados, autorizaciones obtenidas previamente, contenidos e imágenes preparados, estructura documental razonablemente homogénea y sin fallas de CI. **Quedan fuera del presupuesto** los tiempos de respuesta del estudiantado, permisos faltantes, correcciones sustanciales, pruebas clínicas/educativas o validaciones técnicas no existentes y cualquier problema de licencias/privacidad. Si aparecen, suspender publicación del caso hasta resolverlos y revisar el alcance.

El objetivo razonable de esas seis horas es la **primera migración editorial de seis borradores**, no comprometer seis publicaciones aprobadas sin comprobación individual.

## 8. Registro de avance y puntos de aceptación

| Equipo | Material wiki accesible | Créditos y fechas | Adaptación Quarto | Revisión/autorización | Publicado |
| --- | --- | --- | --- | --- | --- |
| 1 | Pendiente | Pendiente | Pendiente | Pendiente | No |
| 2 | Pendiente | Pendiente | Pendiente | Pendiente | No |
| 3 | Pendiente | Pendiente | Pendiente | Pendiente | No |
| 4 | Pendiente | Pendiente | Pendiente | Pendiente | No |
| 5 (**piloto**) | Pendiente | Pendiente | Pendiente | Pendiente | No |
| 6 | Pendiente | Pendiente | Pendiente | Pendiente | No |

**Puerta de publicación por caso:** wiki íntegra recuperada o fuente alternativa verificada + derechos/autorizaciones + créditos/fechas corroborados + revisión de privacidad/contenido + validación Quarto/SEO/Giscus + aceptación editorial explícita. No modificar la privacidad de las fuentes ni publicar materiales del repositorio privado para acelerar el proceso.

## 9. Relación con el próximo laboratorio «Practica · RAG»

La migración de las seis wikis es una **línea de casos académicos de Comunidad YaskCode**, distinta del laboratorio **«Practica · RAG»**, ya registrado como siguiente desarrollo didáctico en el PR #27 (pendiente de integración cuando corresponda). Los casos podrán ilustrar **Comparte** y ofrecer futuras ideas de prácticas, pero **no sustituyen** un laboratorio reproducible y no se enlazarán como publicados hasta que existan.

**Próxima acción cuando se autorice la ejecución:** preparar el expediente privado de permisos y metadatos por equipo, comprobar la clonación de la wiki del piloto y definir la adaptación de autores múltiples en el Blog. El orden de las otras cinco publicaciones se decidirá según sus materiales y autorizaciones reales.
