# Ficha de evaluación RAG · Precision@K, Recall@K y MRR

**Serie YaskCode 2027 · Aprende · Inteligencia Artificial · Básico.**

## Contrato de evaluación

- Fecha y versión del corpus:
- Consultas de evaluación:
- Versión de los juicios de relevancia:
- K utilizado:
- Criterio para documentos parcialmente relevantes:
- Protocolo para consultas sin documentos relevantes:

## Tabla de trabajo

| Consulta | Relevantes conocidos | Recuperados, en orden | Precision@K | Recall@K | RR@K |
|---|---|---|---|---|---|
| Q1 | A, B | A, C, B | | | |
| Q2 | D, E | X, D, Y | | | |
| Q3 | F | G, H, F | | | |

Para K=3, resultados de referencia:

- Precision@3 media macro = 4/9 = 0,444.
- Recall@3 media macro = 5/6 = 0,833.
- MRR@3 = 11/18 = 0,611.

## Comprueba

- [ ] Distingo documentos relacionados de documentos relevantes para responder.
- [ ] Compruebo el numerador y denominador de cada cálculo.
- [ ] Mantengo el mismo valor K entre consultas.
- [ ] Identifico la primera posición relevante para RR.
- [ ] Informo resultados por consulta además de promedios.
- [ ] Distingo recuperación de generación y de validez de respuestas.

## Construye

**Básico:** sustituye el resultado Y de Q2 por E y recalcula métricas.

**Intermedio:** introduce una consulta sin resultados relevantes encontrados y documenta tu política de cálculo.

**Avanzado:** diseña dos conjuntos disjuntos (ajuste y evaluación) y compara los resultados de dos configuraciones de recuperación.

**Comparte:** publica voluntariamente tus tablas y decisiones metodológicas sin revelar datos reservados.
