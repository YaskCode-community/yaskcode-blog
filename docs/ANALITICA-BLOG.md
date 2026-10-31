# Analítica y vistas históricas del Blog YaskCode

**Primera medición:** 31 de octubre de 2026.  
**Estado:** PR #17 en borrador; implementación pendiente de aprobación y prueba en despliegue.

## Objetivo

Conservar las visualizaciones del blog desde el comienzo de la medición, además de informar el interés reciente (últimos 30 días), **sin utilizar Cloudflare Workers, Workers AI ni D1 de YASE**. El sitio permanece como Quarto + GitHub Pages y los comentarios siguen funcionando mediante Giscus.

## Arquitectura

1. **Medición:** Cloudflare Web Analytics, ya integrado en el sitio, registra cargas de página desde el navegador.
2. **Consulta:** GitHub Actions consulta cada día la API de Cloudflare **Analytics SQL** (`events.rumPageloadEvents`) con permiso de **solo lectura**. Se limita al `siteTag` del blog, a su host y a `bot = 0`.
3. **Agrupación diaria:** la consulta devuelve `toDate(timestamp)`, ruta y vistas. El script `scripts/update_views.py` agrega por día UTC y ruta canónica. Las ejecuciones repetidas **reemplazan los días consultados**, no suman su resultado sobre el existente.
4. **Histórico persistente:** GitHub Actions conserva `views-history.json` en una rama independiente **`analytics-history`** del mismo repositorio público. Este archivo solo contiene **totales diarios por las cinco páginas públicas** y ninguna información de visitantes. No se guarda en una base de datos de Cloudflare.
5. **Corrección y continuidad:** cada ejecución vuelve a consultar los últimos **7 días** para captar ajustes de analítica; si se omitieron ejecuciones, recupera los días faltantes junto con esa ventana. Si la ausencia supera el límite de recuperación definido (160 días), **falla sin reiniciar ni falsear el contador histórico**. El historial de días más antiguos se conserva indefinidamente en GitHub, sujeto a conservar esa rama y sus copias de seguridad.
6. **Publicación:** un único archivo `_site/assets/views.json` contiene dos medidas por página: `total` desde la primera medición y `last_30_days` para los últimos 30 días. No contiene un token, IDs de visitantes ni estadísticas privadas.
7. **Presentación:** `assets/article-tools.js` muestra en los títulos de los artículos y tarjetas: **«N vistas acumuladas · M últimos 30 días»**. El inicio real del registro es el **31-10-2026**, no la fecha editorial de publicación del artículo.
8. **Cadencia:** actualización programada mediante GitHub Actions a las **12:17 UTC cada día**, además de cada despliegue. No es tiempo real. Si los datos publicados tienen más de **72 horas** sin actualizar, se **oculta la cifra**, pero **no se elimina ni restablece el histórico**.

### Seguridad

- Se requieren dos secretos del repositorio, guardados en **Settings → Secrets and variables → Actions**:
  - `CF_WEB_ANALYTICS_TOKEN`: token Cloudflare con **Account Analytics → Read**, alcance de la cuenta que contiene la analítica del blog.
  - `CF_WEB_ANALYTICS_ACCOUNT_ID`: identificador de la cuenta obtenido del panel Cloudflare. No es contraseña, pero se mantiene fuera de los archivos públicos.
- No conceder permisos sobre Workers, Workers AI, D1 o modificación de la cuenta. No utilizar Global API Key.
- La autorización de GitHub Actions para escribir se utiliza exclusivamente para registrar el histórico en una **rama diferente de `main`**; si no logra persistirlo, **aborta el despliegue**. El flujo de comprobación del PR mantiene permisos de lectura.
- No compartir el valor del token en el chat, archivos del repositorio, capturas o PR.
- Los datos de los usuarios nunca son exportados a GitHub; solo los totales agregados y por fecha.

### Primer corte verificado (31 de octubre de 2026)

| Página | Vistas registradas inicialmente |
| --- | ---: |
| Hugging Face | 9 |
| RAG | 8 |
| Portada | 5 |
| POO e IA | 1 |
| Campus YaskCode | 0 |
| **Total** | **23** |

Son las cifras de **una primera consulta**, no los totales actuales. En nuevas consultas aparecen más visitas, incluidas las generadas durante QA. No se han recuperado visitas anteriores a la instalación del beacon de Cloudflare Web Analytics.

### Limitaciones importantes

- **Vistas ≠ personas únicas.** Un mismo lector puede generar múltiples cargas.
- Un navegador puede bloquear las mediciones. Los informes de Cloudflare también pueden emplear muestreo o correcciones retrospectivas; por eso el contador representa **vistas registradas**, no una cifra absoluta indiscutible.
- La agrupación utiliza fechas **UTC**. En la ventana de «últimos 30 días» se incluyen el día UTC actual y los 29 anteriores.
- No mostramos el detalle por visitantes, dispositivos o referentes en el contador público. Estos datos se consultan de manera privada desde Cloudflare.
- La rama `analytics-history` **debe conservarse y respaldarse**: no borrar ni forzar su historial. Sin ella, una interrupción extensa podría impedir recuperar datos antiguos una vez que expiren en Cloudflare.
- Los permisos y límites de la Analytics SQL API pueden cambiar; si una consulta falla, el flujo **no debe publicar contadores falsos**.

## Comprobación final antes de aprobar el PR

- [x] Lógica de agregación diaria y de acumulación implementada.
- [x] Integración visual de **acumuladas + últimos 30 días** preparada.
- [x] Pruebas offline de rutas, idempotencia, ventana 30 días y conservación de datos viejos añadidas.
- [ ] Crear en GitHub los dos secretos de Cloudflare.
- [ ] Confirmar que el PR #17 pasa el CI con la última revisión.
- [ ] Aprobar PR, integrar a `main` y ejecutar el flujo de despliegue.
- [ ] Verificar que GitHub Actions creó la rama `analytics-history`, el JSON público es actual y los contadores se muestran correctamente.
- [ ] Confirmar actualización al día siguiente y revisar la estrategia de respaldo periódico de la rama histórica.

## Referencias técnicas

- [Cloudflare Analytics SQL API](https://developers.cloudflare.com/analytics/sql-api/)
- [Query API y parámetros](https://developers.cloudflare.com/analytics/sql-api/query-api/)
- [Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)
- [GitHub Actions – secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)
