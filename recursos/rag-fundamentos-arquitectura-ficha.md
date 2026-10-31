# Ficha de lectura · RAG: fundamentos y arquitectura para comenzar

**Blog YaskCode · Aprende · Inteligencia Artificial · Básico**  
**Autora:** Yaskelly Yedra  
**Artículo:** https://yaskcode-community.github.io/yaskcode-blog/posts/rag-fundamentos-arquitectura/

## La idea esencial

RAG (generación aumentada por recuperación) busca fragmentos de información externa pertinentes antes de pedir a un modelo de lenguaje que responda. La evidencia recuperada puede ayudar a fundamentar y comprobar una respuesta, pero no garantiza su veracidad.

## Dos procesos

1. **Preparación e indexación:** identificar fuentes autorizadas, extraer contenido, dividirlo en fragmentos, representar y almacenar información con sus metadatos.
2. **Consulta:** recibir la pregunta, recuperar evidencia pertinente, generar la respuesta y verificar que las afirmaciones están sustentadas.

## Piezas de la arquitectura

Fuentes → ingestión → fragmentación → embeddings/índice → recuperación → contexto → generación y comprobación.

## Qué conviene recordar

- La recuperación relevante no siempre recupera evidencia suficiente.
- RAG permite consultar información documental; el *fine-tuning* adapta el modelo. Son complementarios.
- La confidencialidad, el origen de las fuentes y las citas verificables importan tanto como la fluidez.
- Ante evidencia ausente o contradictoria, el sistema debería reconocer el límite.

## Tres preguntas para revisar tu comprensión

1. ¿Qué cambia en la arquitectura cuando la guía docente incorpora una nueva versión?
2. ¿Por qué un fragmento semánticamente similar podría ser insuficiente para responder?
3. ¿Cómo distinguirías una respuesta bien redactada de una sustentada en documentos?

## Referencias para profundizar

- Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*: https://papers.nips.cc/paper_files/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html
- Hugging Face, documentación RAG: https://huggingface.co/docs/transformers/model_doc/rag

**Alcance:** ficha de síntesis del artículo conceptual; no representa resultados de un experimento ni un laboratorio ya publicado. Consulta la bibliografía completa en el artículo.
