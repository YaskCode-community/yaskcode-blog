# Ficha de lectura crítica · Casos de inteligencia artificial

**Blog YaskCode · Aprende · Ingeniería de Software · Básico**  
**Artículo asociado:** «Cómo leer críticamente un caso de IA: evidencia, arquitectura y límites»  
**Autora de la guía:** Yaskelly Yedra  
**Uso:** actividad formativa reutilizable; no constituye una certificación ni una calificación automática del proyecto.

## Antes de empezar

- **Caso analizado:** ______________________________________________
- **Fuente y versión:** _____________________________________________
- **Fecha de lectura:** _____________________________________________
- **Tipo de material:** [ ] Caso académico  [ ] Estudio empírico  [ ] Tutorial  [ ] Otro

## Las seis preguntas

| Pregunta | Respuesta / fuente comprobable | ¿Es hecho, inferencia o pendiente? |
|---|---|---|
| 1. ¿Qué problema resuelve y para quién? | | |
| 2. ¿Qué se diseñó y qué está implementado? | | |
| 3. ¿Qué evidencia respalda una afirmación central? | | |
| 4. ¿Qué se evaluó, con cuántos casos y en qué entorno? | | |
| 5. ¿Qué fallos, riesgos o límites se declararon? | | |
| 6. ¿Qué decisión podrías transferir y bajo qué condición? | | |

**Clave de lectura:** no rellenes silencios de la documentación con conjeturas. Es válido escribir «no consta en la evidencia consultada».

## Mini ejercicio: ¿qué demuestra cada prueba?

*Escenario ficticio.* Un asistente de convocatorias responde a preguntas sobre el plazo de inscripción. El equipo informa que cinco pruebas unitarias de selección de documentos terminaron correctamente.

1. **Afirmación A:** «La selección de documentos funcionó en los cinco casos probados». ¿Está respaldada? ¿Qué falta para reproducirla?
2. **Afirmación B:** «El asistente nunca inventará una fecha». ¿Está respaldada? ¿Por qué?
3. **Afirmación C:** «La arquitectura tiene un supervisor». ¿Qué evidencia necesitas además de un dibujo?
4. **Afirmación D:** «El sistema está listo para producción». ¿Qué comprobaciones adicionales pedirías?

### Orientaciones para el análisis

- **A:** es compatible con el resultado reportado, pero conviene identificar las entradas, expectativas, versión y entorno.
- **B:** no se deriva de probar un componente de selección; hace falta evaluar la generación, la fidelidad y casos negativos.
- **C:** el diagrama demuestra intención de diseño; para confirmar implementación hay que examinar código, interfaces y ejecuciones.
- **D:** requiere requisitos de seguridad, control de acceso, disponibilidad, evaluación de riesgos, pruebas de integración y contexto de uso.

## Registro de una decisión transferible

Completa con tu propio caso:

> Adoptaría la decisión ____________________ cuando ____________________.
> Antes comprobaría ____________________. No la utilizaría si ____________________.

## Retos Construye (opcionales)

**Básico — Identifica:** selecciona una afirmación y subraya la oración exacta que la respalda. Si no existe, registra la ausencia.

**Intermedio — Contrasta:** compara un diagrama y un módulo de código. Escribe qué componentes coinciden, cuáles son solo propuestas y qué evidencia hace falta.

**Avanzado — Diseña verificación:** toma un resultado «100 %» y propone un conjunto independiente de al menos seis casos que pongan a prueba nuevas entradas, errores y límites. Define las métricas, los criterios y qué conclusión sería legítima.

## Lista breve de comprobación

- [ ] Diferencié arquitectura propuesta e implementación observada.
- [ ] Identifiqué un resultado con su denominador y contexto.
- [ ] Busqué al menos un caso negativo o un límite conocido.
- [ ] No confundí simulación local con validación en uso real.
- [ ] Formulé una pregunta pendiente sin inventar datos.
- [ ] Documenté la fuente y la versión consultada.

**Para continuar:** al publicarse el primer caso de la serie, RunCoach AI, utiliza esta misma ficha y compara su arquitectura, sus pruebas y sus límites con los del ejemplo ficticio.

**Referencias de apoyo:** [SWEBOK](https://www.computer.org/education/bodies-of-knowledge/software-engineering/resources/) · [Runeson y Höst, 2009](https://doi.org/10.1007/s10664-008-9102-8) · [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).