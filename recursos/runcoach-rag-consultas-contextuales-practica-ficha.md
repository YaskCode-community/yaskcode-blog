# Ficha práctica · Consultas contextuales RAG

**Serie YaskCode 2027 · Práctica del 20 de mayo (fecha prevista).**

## Objetivo

Preparar consultas útiles para recuperación futura a partir de registros sintéticos y verificar el comportamiento de la selección temporal.

## Lista de comprobación

- [ ] Ejecuté `py -m codigo.demo` desde la carpeta raíz del laboratorio.
- [ ] Ejecuté `py -m unittest discover -s pruebas -v`.
- [ ] Identifiqué las tres notas esperadas en el orden correcto.
- [ ] Comprobé una nota antigua y otra de edad inválida.
- [ ] Añadí un nuevo caso límite y registré el resultado.

## Registro de evidencias

| Prueba | Entrada | Resultado esperado | Resultado observado |
|---|---|---|---|
| Nota antigua | `dias_atras=15` | Excluida | |
| Duplicado | Texto con espacios adicionales | Una aparición | |
| Ventana límite | `dias_atras=7` | Incluida | |
| Edad inválida | `dias_atras="desconocido"` | Excluida | |

## Retos

**Básico:** caso con nota vacía.

**Intermedio:** límite de caracteres por nota.

**Avanzado:** comparación entre dos políticas de selección y un conjunto de validación independiente.

**Interpretación:** estos resultados validan solo el laboratorio, no un recuperador completo ni un modelo generativo.
