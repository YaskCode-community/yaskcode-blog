# Estrategia de difusión · Blog YaskCode

**Versión:** 31 de octubre de 2026  
**Estado:** propuesta para revisión editorial.

## Principio

El **Blog YaskCode en Quarto / GitHub Pages** es la fuente principal de los artículos. La distribución en redes y comunidades acompaña a las etapas **Aprende · Practica · Construye · Comparte**. Se prioriza la audiencia académica y de desarrollo de software, los lectores hispanohablantes, la calidad de la conversación y la preservación de las URLs originales. Esta prioridad es editorial, no una clasificación basada en estadísticas reales de tráfico.

## Prioridad de canales

| Prioridad | Canal | Objetivo | Experiencia del botón |
| --- | --- | --- | --- |
| 1 | LinkedIn | Divulgación profesional y académica | Compartir el enlace del artículo |
| 2 | DEV Community (dev.to) | Conversación técnica; republicación editorial separada mediante RSS | **DEV · debatir** abre el editor para redactar una reflexión propia, no para copiar el artículo |
| 3 | WhatsApp | Difusión directa a estudiantes, colegas y grupos | Compartir título y enlace |
| 4 | Bluesky | Conversación en tecnología y ciencia | Preparar publicación con título y enlace |
| 5 | Reddit | Diálogo en comunidades técnicas pertinentes | Abrir formulario de envío y respetar reglas comunitarias |
| 6 | Mastodon | Participación en comunidades abiertas | Abrir herramienta de distribución con texto y enlace |
| 7 | X | Alcance y novedades rápidas | Preparar publicación con título y enlace |
| 8 | Telegram | Canales y grupos de aprendizaje | Compartir título y enlace |
| 9 | Threads | Conversación y divulgación general | Preparar publicación con título y enlace |
| 10 | Facebook | Grupos, páginas y comunidades educativas | Compartir enlace |
| Complementario | Correo electrónico | Difusión personalizada | Crear mensaje en cliente de correo |

**Utilidades independientes de redes:** «Copiar enlace» y «Compartir» (menú nativo del dispositivo). El menú nativo depende del sistema y de las aplicaciones instaladas; no muestra necesariamente todas las plataformas. Instagram no aparece por ser redundante con «Copiar enlace» y no contar con un flujo universal de compartir una página web.

**Diseño:** barra principal con Copiar enlace, Compartir (si el navegador lo permite), LinkedIn, DEV · debatir y WhatsApp. «Más redes» contiene, en ese orden, *Comunidades y redes técnicas* (Bluesky, Reddit, Mastodon y X) y *Difusión y mensajería* (Telegram, Threads, Facebook y Correo).

## DEV Community: procedimiento recomendado

DEV es **plataforma editorial**, no un servicio que publique automáticamente una URL con un botón. El botón público **DEV · debatir** abre `https://dev.to/new`: permite a un lector escribir una **reflexión propia y sustancial** y citar el artículo original; no concede permiso para reproducirlo íntegramente. No equivale a una acción de compartir directamente una URL. La **republicación oficial de contenidos YaskCode** es un flujo distinto y exclusivo de la autora o su equipo autorizado. Para conservar la fuente original:

1. Mantener primero la publicación canónica en el Blog YaskCode.
2. Elegir el contenido técnico que aporte valor a la comunidad DEV, evitando publicaciones únicamente promocionales.
3. Crear o revisar el borrador en DEV y **asignar la URL del artículo YaskCode como enlace canónico**.
4. Verificar imágenes, código, enlaces y referencias antes de publicar.
5. Publicar manualmente la versión revisada y participar en la conversación posterior.

### Alternativa: importar mediante RSS (configuración manual, todavía pendiente)

- Feed original de YaskCode: `https://yaskcode-community.github.io/yaskcode-blog/index.xml`.
- En DEV: `https://dev.to/settings/extensions`, sección **Publishing to DEV Community from RSS**.
- Activar **Mark the RSS source as canonical URL by default**. Revisar los enlaces importados y conservar la versión original como fuente.
- DEV permite revisar los artículos importados como **borradores** antes de su publicación. No activar un proceso que publique sin revisión editorial.
- No publicar entradas que sean solo un enlace ni reproducir contenido ajeno sin permiso: DEV exige contenido original y sustancial.
- La configuración del RSS en DEV requiere sesión/autorización de la propia autora y **no se ha realizado desde el repositorio**.

Fuentes oficiales:
- https://dev.to/help/writing-editing-scheduling
- https://dev.to/help/organizations/importing-your-organizations-content

## Seguimiento y límites

Revisar resultados cada cierto número de publicaciones: lecturas por artículo (Web Analytics), clics en recursos y conversaciones. Las cifras por red solo deben informarse cuando haya medición fiable y explícita. El botón DEV y las demás opciones de difusión son enlaces desde el navegador: **no utilizan Workers, D1 ni Workers AI de YASE**. No se ha creado ni publicado contenido en DEV desde esta intervención.
