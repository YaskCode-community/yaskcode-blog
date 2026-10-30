# Blog YaskCode

Artículos, tutoriales y recursos sobre **Ingeniería de Software, Inteligencia Artificial, Ciencia de Datos y Cloud**, con aprendizajes de proyectos, laboratorios y experiencias educativas de YaskCode.

**Aprende · Practica · Construye · Comparte.**

Coordinado por **Yaskelly Yedra**, profesora e investigadora en Computación. El español es el idioma principal; se incorporarán traducciones al inglés cuando estén revisadas.

## Estado del proyecto

Estamos migrando el blog desde beehiiv hacia un sitio propio generado con **Quarto**, con sus contenidos e imágenes versionados en GitHub.

La primera entrega está en la rama `feat/quarto-blog-base` y en el [PR #1](https://github.com/YaskCode-community/yaskcode-blog/pull/1). Incluye el artículo publicado **«RAG: fundamentos y arquitectura para comenzar»**, tarjetas, filtros por área y sección, búsqueda y acceso a la suscripción.

**El nuevo sitio sigue en revisión y aún no está desplegado.** La dirección prevista es [yaskcode-community.github.io/yaskcode-blog/](https://yaskcode-community.github.io/yaskcode-blog/).

Consulta el [registro de migración y sus pendientes](docs/MIGRACION.md).

## Cómo se organiza

| Componente | Función |
| --- | --- |
| Este repositorio | Conserva los originales de artículos, imágenes, diseño e historial de cambios. |
| Quarto | Genera las páginas del blog y permite revisarlas localmente. |
| GitHub Pages | Alojamiento previsto, pendiente de habilitar el despliegue. |
| beehiiv | Mantiene la suscripción y el envío de la newsletter. |
| Apps Script → HubSpot | Conserva la integración existente de contactos. |
| Campus YaskCode | Continúa en Astro, en su propio repositorio. |

Guardar cambios en GitHub **no envía una newsletter automáticamente**. En esta primera entrega, GitHub Actions comprueba el sitio y guarda un artefacto de revisión; todavía no lo publica.

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
git switch feat/quarto-blog-base
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

## Escribir un artículo

1. Crea una carpeta en `posts/` con un nombre breve y sin espacios: por ejemplo, `posts/mi-articulo/`.
2. Añade el archivo `index.qmd` y guarda sus imágenes en esa misma carpeta.
3. Completa los metadatos, escribe el contenido y revisa el resultado con `quarto preview`.
4. Presenta el cambio en un pull request para revisión editorial y técnica.

Ejemplo de metadatos para un **borrador**, que debe adaptarse al artículo real:

```yaml
---
title: "Título del artículo"
author: "Nombre de la persona autora"
date: 2026-10-30
description: "Resumen breve de lo que aprenderá la persona lectora."
categories: ["Aprende", "Inteligencia Artificial"]
area: "Inteligencia Artificial"
editorial-section: "Aprende"
image: portada.png
image-alt: "Descripción accesible de la portada."
toc: true
draft: true
---
```

Usa las áreas y secciones existentes, respetando sus nombres. `editorial-section` es el campo utilizado por las tarjetas y los filtros; no lo sustituyas por `section`.

La portada y las búsquedas se regeneran al construir el sitio. Mantén `draft: true` mientras el texto esté pendiente y comprueba su exclusión de la salida destinada a publicación. Un borrador guardado en este repositorio público puede ser leído en GitHub.

Cada artículo debe identificar su autoría, citar sus fuentes y distinguir los ejemplos hipotéticos de los resultados obtenidos. Las publicaciones derivadas de YASE y los laboratorios deben explicar qué se construyó, cómo se probó, qué se observó y cuáles son sus límites.

## Archivos principales

| Ruta | Contenido |
| --- | --- |
| `_quarto.yml` | Configuración, navegación y opciones generales. |
| `index.qmd` | Portada y controles para explorar artículos. |
| `acerca.qmd` | Presentación del blog, pendiente de contraste editorial. |
| `posts/<slug>/index.qmd` | Texto y metadatos de cada artículo. |
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

## Próximos pasos de la migración

- Confirmar visualmente los ajustes de la introducción y del centrado en pantallas amplias.
- Completar la validación visual y funcional en escritorio y móvil.
- Revisar la página Acerca y el recorrido de suscripción.
- Acordar las licencias y el tratamiento de las URLs anteriores.
- Habilitar el despliegue después de la aceptación de esta entrega.
- Actualizar el enlace del Campus cuando el nuevo blog esté disponible y comprobado.
- Incorporar las cinco entradas adicionales con revisión editorial.

## Autoría y licencias

Se conserva la autoría de cada artículo y la procedencia de los recursos. Las licencias de código y contenidos están pendientes de decisión explícita de la autora; la visibilidad pública de este repositorio no concede por sí sola una licencia de reutilización.
