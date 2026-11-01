# Ficha YaskCode · De RAG a sistemas multiagentes

**Aprende · Inteligencia Artificial · Intermedio.** Fecha editorial prevista: 17 de junio de 2027.

## Decisión arquitectónica

**Necesidad:** _________________________________________

| Pregunta | Respuesta |
|---|---|
| ¿Basta con recuperar documentos? | |
| ¿Hay que ejecutar acciones autorizadas? | |
| ¿Hay dominios de responsabilidad independientes? | |
| ¿Quién conserva el estado? | |
| ¿Qué componente puede leer datos? | |
| ¿Qué componente puede escribir? | |
| ¿Cuándo debe intervenir una persona? | |

## Compara patrones

| Patrón | ¿Quién tiene el control? | ¿Qué comprobaría? |
|---|---|---|
| Router | | |
| Supervisor | | |
| Handoff | | |
| Secuencial | | |

## Contrato mínimo de delegación

- Identificador de tarea:
- Identificador de traza:
- Destinatario y acción autorizada:
- Datos permitidos:
- Esquema de respuesta:
- Condición de error:
- Límite de pasos:
- Política de aprobación humana:

## Evidencias

- [ ] Documenté la procedencia de las fuentes.
- [ ] Separé pruebas con mocks de pruebas con servicios reales.
- [ ] Agregué pruebas de rutas no autorizadas.
- [ ] Incluí errores y ciclos en el diseño.
- [ ] Justifiqué si realmente necesito más de un agente.

## Retos de profundización

**Básico:** representar el flujo con un router de dos destinos.

**Intermedio:** diseñar un supervisor con contratos de solicitud y respuesta.

**Avanzado:** analizar fallos, autorizaciones y trazabilidad con pruebas por capas.

**Comparte:** publica voluntariamente un diagrama y tu argumentación, sin datos institucionales confidenciales.
