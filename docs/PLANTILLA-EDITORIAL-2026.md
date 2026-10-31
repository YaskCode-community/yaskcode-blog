# Plantilla editorial YaskCode · Artículos Aprende

**Versión:** 2026-10-31 · **Estado:** estándar editorial aprobado para futuras publicaciones.

Este modelo se adapta al tema. No exige crear cuatro publicaciones por tema: la ruta editorial utiliza generalmente un artículo **Aprende** (fundamentos) y un artículo **Practica** (laboratorio). **Construye** son retos progresivos del laboratorio y **Comparte** invita a publicar evidencias en la comunidad.

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

## Esqueleto de una nueva publicación

```qmd
---
title: "Un título que describa el problema"
subtitle: "Una promesa de aprendizaje concreta"
author: "Yaskelly Yedra"
date: YYYY-MM-DD
description: "Descripción original para buscadores"
categories: ["Aprende", "Área temática"]
area: "Área temática"
editorial-section: "Aprende"
level: "Básico"
image: "portada-por-crear.webp"
image-alt: "Descripción textual de la portada"
toc: true
---

**Aprende · Área temática · Nivel Básico**

::: {.callout-note title="En 1 minuto"}
Síntesis comprobada, idea central y límites.
:::

::: {.callout-tip title="Lo que aprenderás"}
Objetivos conceptuales adecuados al artículo (sin adjudicar resultados medidos).
:::

### Antes de comenzar

**Conocimientos previos:** requisitos reales.

::: {.callout-tip title="Recursos para llevar"}
[Descargar ficha de lectura](ruta-real.md)
:::

## 1. Situación o problema

## 2. Conceptos esenciales

## 3. Aprende: fundamentos y arquitectura

Explicación, ejemplos, decisiones y límites, según el tema.

## 4. Conclusiones

### Referencias académicas y técnicas

Fuentes reales con título y enlace oficial.

### Continúa aprendiendo

Enlace al laboratorio Practica **solo si ya está publicado**.
```

Los marcadores de ejemplo **no deben incorporarse a producción**. Para cada nuevo artículo hay que crear su ficha descargable real y su archivo de metadatos `BlogPosting`, o automatizar esa generación con pruebas.

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
