# Estándar de prácticas, laboratorios y ejercicios · Blog YaskCode

**Estado:** propuesta técnica y editorial para revisión. No implica que exista ya un laboratorio publicado.

## Decisión: una carpeta por publicación

Seguimos la estructura recomendada para blogs Quarto: cada publicación vive en `posts/<slug>/index.qmd`. Esto aplica tanto a **Aprende**, como a **Práctica**, **Casos de estudio**, otras historias y futuras guías. Un laboratorio es normalmente una publicación *Práctica*; un ejercicio puntual suele ser parte del laboratorio. Solo crear un post independiente para un ejercicio si merece una explicación autónoma, una URL persistente y su propia verificación.

No crear carpetas de primer nivel `laboratorios/` o `ejercicios/` como listados alternativos. En la portada el tipo se identifica por `editorial-section: "Práctica"`. Las etiquetas `Básico / Intermedio / Avanzado` expresan nivel, **no** se incorporan a `categories`.

### Ejemplo de estructura futura, no publicada

```text
posts/
  rag-fundamentos-arquitectura/
    index.qmd                 # Aprende: ya publicado
  rag-recuperacion-documentos-laboratorio/
    index.qmd                 # Práctica: futuro, aún no creado
    portada.webp
    codigo/
      ejemplo.py              # Código verificable y revisado
    datos/
      documentos-ejemplo.csv  # Datos sintéticos o con licencia
    pruebas/
      test_ejemplo.py         # Comprobaciones reproducibles
recursos/
  rag-recuperacion-documentos-laboratorio-ficha.md
plantillas/
  articulo-practica/
    index.qmd                 # Plantilla, NO post del sitio
```

Los nombres de `codigo/`, `datos/` y `pruebas/` son convenciones opcionales; no hay que crear carpetas vacías. Los proyectos extensos, servicios o software que necesita CI propio pueden alojarse en un **repositorio dedicado**, enlazado por versión o commit desde el artículo.

## Dos publicaciones centrales por tema

1. **Aprende:** conceptos, fundamentación, arquitectura y límites.
2. **Práctica:** actividad guiada, entorno, entradas, pasos, resultados verificables y diagnóstico de fallos.

**Construye** aparece al final de la práctica como retos progresivos: Básico (adaptar), Intermedio (extender) y Avanzado (evaluar). El nivel del laboratorio es independiente del nivel de cada reto. **Comparte** es una invitación transversal a compartir resultados, correcciones y recursos de manera voluntaria.

No forzar cuatro publicaciones separadas por tema. Las prácticas también pueden ser ejercicios independientes cuando tengan su propia finalidad pedagógica.

## Ficha mínima de laboratorio reproducible

| Elemento | Criterio de aceptación |
| --- | --- |
| Objetivo | Resultado observable y conocimientos previos explícitos |
| Entorno | Sistema operativo, dependencias y versiones realmente comprobadas |
| Acceso y coste | Cuentas, servicios, cuotas, límites y alternativas gratuitas verificados |
| Materiales | Archivos de código, datos y pruebas existentes y autorizados |
| Seguridad | Nada de tokens, claves API, información personal o trabajos privados |
| Procedimiento | Comandos, rutas, orden de ejecución y explicación de las decisiones |
| Comprobación | Entrada de prueba, salida esperada y resultado real claramente diferenciados |
| Límites | Qué casos se probaron, qué se simuló y qué falta evaluar |
| Retos | Tres grados opcionales con entregables y criterios propios |
| Participación | Canal voluntario para comentar y compartir evidencias, respetando licencias |
| Publicación | Cabecera, portada, `BlogPosting`, accesibilidad y CI validados; aceptación previa |

**Un laboratorio no se considera reproducible por mostrar capturas o listar comandos:** otra persona debe poder ejecutar los pasos con los materiales indicados y obtener resultados comparables. Si no se ejecutó, declararlo como ejercicio propuesto, no como validación.

## Copiar la plantilla en PowerShell

Desde la raíz del repositorio `yaskcode-blog`:

```powershell
New-Item -ItemType Directory -Path posts/mi-laboratorio
Copy-Item plantillas/articulo-practica/index.qmd posts/mi-laboratorio/index.qmd
```

Sustituir `mi-laboratorio` por un slug descriptivo y estable. Reemplazar todos los marcadores, conservar `draft: true`, y no abrir un PR público con material privado o sin permiso de publicación. Los borradores de un repositorio **público** son visibles en el código fuente de GitHub aunque Quarto no los publique en el sitio.

### Descargas y recursos en Quarto

El proyecto limita el render a los documentos Quarto y declara recursos específicos en `_quarto.yml`. **No asumir** que cualquier archivo Python, CSV, notebook o prueba se copiará automáticamente a `_site/`. Antes de publicar:

1. Revisar qué recursos de esa práctica están autorizados para distribución.
2. Incluir en `project.resources` las rutas concretas de archivos necesarios, o alojarlos en un repositorio público dedicado con referencia de versión. No usar un comodín global que exponga datos privados.
3. Ejecutar `quarto render`, comprobar que las descargas existen en `_site/` y que sus enlaces funcionan.
4. Verificar que los ejemplos no requieran API keys de pago sin avisar y que los datos puedan redistribuirse bajo su licencia.

La configuración actual del blog usa `execute.enabled: false`; los bloques de código del post son ilustrativos o copiables, pero **Quarto no ejecuta los laboratorios durante el render**. La ejecución y verificación se hacen por separado y se documentan. No afirmar que un CI del blog prueba el código del ejercicio a menos que efectivamente lo haga.

## Primera práctica prioritaria

**RAG · Recuperación sobre documentos de ejemplo** es el laboratorio previsto después de [RAG: fundamentos y arquitectura para comenzar](../posts/rag-fundamentos-arquitectura/index.qmd). La planificación editorial ya está registrada en el [PR #27](https://github.com/YaskCode-community/yaskcode-blog/pull/27), aún en borrador y no fusionado.

Propuesta de alcance mínimo, **no implementada ni validada**:

- Datos pequeños y sintéticos que cualquiera pueda descargar.
- Preparación y segmentación documentadas, recuperación simple verificable y evaluación de una pregunta con evidencia.
- Comparación de una consulta pertinente con otra fuera de cobertura, sin inventar una respuesta.
- Una base reproducible que no dependa de créditos de servicios externos; integración opcional de embeddings/LLM en extensión o reto.
- Pruebas independientes y salidas observables; construir variantes en retos progresivos.

No anunciar URL ni fecha del laboratorio hasta que exista el artículo aprobado y comprobado.

## Relación con casos académicos

Los **casos de estudio** procedentes de wikis estudiantiles no son automáticamente laboratorios. Su principal finalidad es analizar un problema, decisiones y resultados de proyectos, preservando autoría, asesoría y límites. Un caso puede inspirar después un ejercicio o laboratorio **original**, con datos sintéticos y contenido autorizado. La migración de seis wikis continúa en su [plan independiente](PLAN-MIGRACION-SEIS-WIKIS-SISTEMAS-INTELIGENTES-2026.md).

## Plantilla

Fuente de partida: [`plantillas/articulo-practica/index.qmd`](../plantillas/articulo-practica/index.qmd); debe permanecer fuera de `posts/` hasta copiarla para una publicación real.
