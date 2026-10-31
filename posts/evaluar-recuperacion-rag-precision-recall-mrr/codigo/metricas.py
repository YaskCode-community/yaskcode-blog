"""Ejemplo original de YaskCode: evaluación de recuperación @3.

Sin LLM, acceso a red, bibliotecas externas ni datos de usuarios.
"""
from fractions import Fraction

CONSULTAS = (
    {"id": "Q1", "relevantes": {"A", "B"}, "recuperados": ["A", "C", "B"]},
    {"id": "Q2", "relevantes": {"D", "E"}, "recuperados": ["X", "D", "Y"]},
    {"id": "Q3", "relevantes": {"F"}, "recuperados": ["G", "H", "F"]},
)


def medir(relevantes: set[str], recuperados: list[str], k: int = 3) -> dict:
    if not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("K debe ser un entero positivo")
    if len(recuperados) < k:
        raise ValueError("La demostración requiere al menos K documentos")
    if len(set(recuperados[:k])) != k:
        raise ValueError("No se permiten IDs duplicados en el top K")
    if not relevantes:
        raise ValueError("Recall indefinido: no hay relevantes conocidos")
    top = recuperados[:k]
    encontrados = sum(doc in relevantes for doc in top)
    primero = next((i for i, doc in enumerate(top, 1) if doc in relevantes), None)
    return {
        "precision": Fraction(encontrados, k),
        "recall": Fraction(encontrados, len(relevantes)),
        "rr": Fraction(1, primero) if primero is not None else Fraction(0),
    }


def resumen(consultas=CONSULTAS, k=3):
    resultados = [(consulta["id"], medir(consulta["relevantes"], consulta["recuperados"], k)) for consulta in consultas]
    if not resultados:
        raise ValueError("Debe existir al menos una consulta")
    total = len(resultados)
    promedios = {nombre: sum((r[nombre] for _, r in resultados), Fraction(0))/total for nombre in ("precision", "recall", "rr")}
    return resultados, promedios


if __name__ == "__main__":
    resultados, media = resumen()
    for identificador, valores in resultados:
        print(identificador, " ".join(f"{clave}={float(valor):.3f}" for clave, valor in valores.items()))
    print("PROMEDIO", " ".join(f"{clave}={float(valor):.3f}" for clave, valor in media.items()))
