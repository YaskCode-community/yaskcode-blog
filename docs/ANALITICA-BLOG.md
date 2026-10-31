# Analítica del Blog YaskCode · vistas sin Workers

**Primera medición:** 31 de octubre de 2026.  
**Estado:** propuesta técnica pendiente de validar, configurar y aprobar antes de publicar el contador automático.

## Objetivo

Conocer qué artículos se consultan más, comprender la evolución de las lecturas y mostrar un contador público **honesto, discreto y sin backend propio**. El blog sigue siendo estático (Quarto + GitHub Pages). Se reserva el cómputo de Cloudflare Workers, Workers AI y D1 para YASE.

## Arquitectura elegida

1. **Recogida:** el script de Cloudflare Web Analytics ya incluido en `assets/footer.html` registra las visualizaciones desde el navegador.
2. **Analítica privada:** el panel de Cloudflare ofrece tendencias, páginas, referentes, dispositivos y otros resúmenes; no se publica información sobre visitantes.
3. **Consulta automática:** el flujo de **GitHub Actions** utiliza una credencial de **solo lectura** para consultar una vez al día la **Analytics SQL API**, conjunto `events.rumPageloadEvents`. Filtra por el sitio del blog, nombre de host, `bot = 0` y ventana temporal de 30 días.
4. **Instantánea pública:** `scripts/update_views.py` genera `_site/assets/views.json` solo con **cinco rutas públicas conocidas y sus totales de pageviews**. No conserva direcciones IP, usuarios, datos por sesión ni referentes individuales.
5. **Presentación:** `assets/article-tools.js` presenta `◉ N vistas registradas · últimos 30 días` en cada artículo y en las tarjetas de la portada. Si la instantánea tiene más de **72 horas** o está dañada, no muestra ningún contador; **no muestra valores inventados**.
6. **Frecuencia:** GitHub Actions está programado cada día a las **12:17 UTC**, además de actualizar al publicar un cambio en la rama `main`. Puede sufrir demoras; no es un contador en tiempo real.
7. **Seguridad y costos:** el visitante solo descarga archivos estáticos de GitHub Pages. La API se consulta desde GitHub Actions, **nunca desde el navegador**. No se crean ni invocan Workers, D1 ni Workers AI. Para este repositorio público, los minutos estándar de GitHub Actions son gratuitos según las condiciones actuales de GitHub.

### Qué mide

- Una **vista registrada** es una carga de página observada por Web Analytics. **No** es una persona única ni una vista histórica desde la publicación original.
- En el contador, la ventana es **30 días móviles**; no es un contador «de toda la vida». Cada actualización puede hacer que el número suba o baje.
- Cloudflare utiliza muestreo adaptativo para consultas de datos agregados; los valores no deben describirse como mediciones infalibles.
- Si un navegador bloquea el script, las visitas pueden no registrarse.
- No se cuentan impresiones en redes sociales ni visitas a copias republicadas en DEV.
- Las consultas hechas para QA del sitio podrían estar incluidas; interpretar con prudencia volúmenes pequeños.

## Primer corte observado · 31 oct 2026

Los registros comienzan al configurar Web Analytics en la mañana del 31/10/2026. Esta tabla corresponde a una consulta de Analytics SQL sobre el sitio, con `bot = 0` y no sustituye datos históricos anteriores a la instalación.

| Página | Vistas registradas |
| --- | ---: |
| Hugging Face | 9 |
| RAG | 8 |
| Portada | 5 |
| POO e IA | 1 |
| Campus YaskCode (artículo) | 0 |

**Total inicial:** 23 vistas de página, no 23 lectores únicos. Por dispositivo se observaron 22 cargas de escritorio y 1 de móvil. Referentes: 15 navegaciones internas del blog, 6 directas/desconocidas y 2 desde `github.com`. Muchos accesos iniciales podrían corresponder a nuestras pruebas de publicación y comentarios.

### Activación del refresco automático (requiere autorización de la administradora)

El flujo se prepara en `.github/workflows/deploy-pages.yml`. Para que la actualización funcione:

1. En Cloudflare, crear **un API Token personalizado** con permiso **Account → Account Analytics → Read**, restringido a la cuenta que ya contiene Web Analytics de YaskCode. **No** seleccionar permisos de Workers, Workers AI, D1, ni `Edit`. No utilizar la Global API Key.
2. En el repositorio público del blog, ir a **Settings → Secrets and variables → Actions → New repository secret** y crear **dos secretos**:
   - `CF_WEB_ANALYTICS_TOKEN`: pegar el token obtenido de Cloudflare (nunca en archivos, capturas, PR ni mensajes de chat).
   - `CF_WEB_ANALYTICS_ACCOUNT_ID`: copiar el **Account ID** desde el panel de Cloudflare. No es una contraseña, pero lo mantenemos fuera del código público por privacidad.
3. Ejecutar manualmente **Actions → Publicar Blog YaskCode en GitHub Pages → Run workflow** para comprobar que el flujo consulta Cloudflare y publica una instantánea reciente.
4. Verificar en un artículo y en su tarjeta de portada la leyenda **«vistas registradas · últimos 30 días»**, y confirmar que cambia con datos reales después de la siguiente ejecución programada.
5. En Cloudflare, revisar periódicamente el uso de API, y revocar el token en caso de sospecha de exposición.

El identificador de sitio incluido en el script no es una credencial. El **Account ID** y el token se guardan como secretos del repositorio; **únicamente el token concede acceso** a Cloudflare. La configuración permanece solamente en el repositorio del blog, no en los recursos de YASE.

**Si no existe el secreto**, el despliegue sigue funcionando con la instantánea inicial; el navegador deja de mostrar la cifra después de 72 horas para evitar datos obsoletos. Si Cloudflare devuelve un error, el trabajo no sobrescribe valores con cifras falsas y detiene ese despliegue, conservando la última versión publicada.

## Alternativas evaluadas

| Alternativa | Ventaja | Límite |
| --- | --- | --- |
| Solo Cloudflare Web Analytics privado | Sin cambios en el sitio ni credenciales de CI | No muestra números públicos |
| **Cloudflare Analytics SQL + GitHub Actions + JSON estático** | Reutiliza la medición real; no usa Workers; un token de lectura y un identificador de cuenta guardados como secretos | Actualización diaria y cuenta 30 días móviles |
| Worker + D1 para contador dinámico | Contador de eventos personalizado y más inmediato | Consume cuota compartida con YASE: descartado ahora |
| Contador público de terceros | Integración sencilla | Datos y condiciones sujetos a proveedor externo; no coinciden necesariamente con Cloudflare |

**Recomendación:** la alternativa estática de 30 días, inicialmente discreta y revisable, y conservar Cloudflare como fuente principal de información.

## Referencias oficiales

- https://developers.cloudflare.com/analytics/sql-api/
- https://developers.cloudflare.com/analytics/sql-api/query-api/
- https://developers.cloudflare.com/web-analytics/faq/
- https://developers.cloudflare.com/workers/platform/pricing/
- https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
