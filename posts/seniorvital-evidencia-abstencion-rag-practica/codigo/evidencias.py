"""Laboratorio independiente de evidencia documental con datos sintéticos."""
import re
import unicodedata

STOPWORDS = {
    "la", "el", "de", "del", "en", "un", "una", "las", "los", "es",
    "que", "por", "para", "cual", "cuanto", "cuales", "cuando", "son",
    "y", "con", "al", "se", "será", "sera"
}


def tokens(texto):
    """Palabras informativas, sin tildes y sin palabras funcionales."""
    if not isinstance(texto, str):
        raise TypeError("Se esperaba texto")
    limpio = "".join(
        c for c in unicodedata.normalize("NFD", texto.lower())
        if unicodedata.category(c) != "Mn"
    )
    return {x for x in re.findall(r"[a-z0-9]+", limpio)
            if len(x) > 2 and x not in STOPWORDS}


def recuperar(pregunta, documentos, max_resultados=5):
    """Recupera candidatos ordenados por coincidencias léxicas."""
    if not isinstance(max_resultados, int) or isinstance(max_resultados, bool) or max_resultados < 1:
        raise ValueError("max_resultados debe ser entero positivo")
    q = tokens(pregunta)
    if not q:
        return []
    candidatos = []
    for pos, doc in enumerate(documentos):
        coincidencias = len(q & tokens(doc["texto"]))
        if coincidencias:
            candidatos.append((-coincidencias, pos, doc))
    candidatos.sort(key=lambda x: (x[0], x[1]))
    return [doc for _, _, doc in candidatos[:max_resultados]]


def decidir(pregunta, campo, documentos):
    """Responde solo si un documento candidato tiene el hecho curado."""
    if not isinstance(campo, str) or not campo.strip():
        raise ValueError("El campo debe estar anotado")
    candidatos = recuperar(pregunta, documentos)
    if not candidatos:
        return {"estado": "SIN_COINCIDENCIAS", "fuente": None, "respuesta": None}
    for doc in candidatos:
        valor = doc.get("hechos", {}).get(campo)
        if isinstance(valor, str) and valor.strip():
            return {"estado": "RESPALDADA", "fuente": doc["id"], "respuesta": valor}
    return {"estado": "SIN_EVIDENCIA", "fuente": None, "respuesta": None}


def evaluar_serie(consultas, documentos):
    return [dict(id=q["id"], **decidir(q["pregunta"], q["campo"], documentos))
            for q in consultas]
