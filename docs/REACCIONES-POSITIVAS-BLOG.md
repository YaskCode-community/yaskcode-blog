# Blog YaskCode · Reacciones positivas del artículo

**Decisión editorial:** ofrecer un único botón **💜 Me gusta** al comienzo del artículo, antes del bloque «Comparte este artículo», y eliminar la barra «0 reacciones» que Giscus mostraba antes de los comentarios.

## Implementación

- En `_quarto.yml`, `website.comments.giscus.reactions-enabled: false` desactiva **las reacciones de la discusión principal**; los comentarios de GitHub Discussions y sus respuestas siguen activos.
- `assets/article-tools.js` crea, únicamente en las cuatro publicaciones, el componente `<pagemoji-reactions>` con `emojis="💜"`, `label="Me gusta"`, `variant="outline"` y un identificador estable derivado del slug. El widget queda **antes de Compartir**.
- El JavaScript externo se carga solamente en páginas de artículos: `https://pagemoji.magicpages.co/v1/pagemoji.js`. En portada y «Acerca de» no hay botón ni solicitudes a ese servicio.
- Estilos magenta de YaskCode en `assets/theme.scss`.
- **Sin Cloudflare Workers, Workers AI ni D1 de YASE**. El contador positivo se aloja por separado en Pagemoji, no en GitHub ni en Cloudflare Analytics.

## Privacidad, limitaciones y moderación

- Pagemoji es de código abierto y ofrece un servidor público gratuito sin registro de lectores y sin cookies, según la documentación de su mantenedor.
- El servicio externo procesa la dirección de cada artículo y la reacción; declara protección temporal contra votos repetidos mediante un identificador derivado de IP que rota periódicamente. No es una votación autenticada ni un conteo exacto de personas únicas.
- **Solo se muestra 💜 en el artículo.** No se ofrece 👎 ni calificación negativa en este widget.
- Las reacciones **a comentarios individuales** dentro de GitHub/Giscus continúan siguiendo las opciones normales de GitHub (pueden incluir otros emojis). No es posible limitar esos emojis mediante la configuración nativa de Giscus.
- Los corazones de Pagemoji son **independientes** de la reacción 👍 ya existente en el comentario inaugural del artículo RAG. Ningún historial de Giscus se migra ni borra.
- Si el servicio gratuito cambia, se interrumpe o limita el acceso, el blog conserva sus artículos, enlaces, comentarios y vistas; la interacción 💜 puede quedar indisponible.
- No debe confundirse el conteo positivo con la métrica académica de calidad del contenido.

## Aceptación

- [ ] CI Quarto y prueba estática de configuración completados.
- [ ] Comprobar en un artículo que no aparece «0 reacciones» sobre Giscus.
- [ ] Comprobar que el widget 💜 aparece **antes de Compartir** y responde al clic.
- [ ] Comprobar que los comentarios históricos y sus reacciones permanecen.
- [ ] Comprobar vista móvil y teclado, y que no aparece el widget en portada.
- [ ] Documentar dependencias externas para evaluación periódica.

Fuentes:
- https://quarto.org/docs/reference/projects/websites.html
- https://giscus.app/es
- https://github.com/magicpages/pagemoji
- https://www.magicpages.co/pagemoji/
