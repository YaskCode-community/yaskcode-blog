"""Preparación determinista de consultas, sin LLM ni búsqueda vectorial.

Adaptación didáctica original de YaskCode con registros ficticios.
La antigüedad viene expresada en días y no depende del reloj actual.
"""
from __future__ import annotations
from collections.abc import Iterable

VENTANA_DIAS = 7
LIMITE_NOTAS = 180
MAX_NOTAS = 3


def seleccionar_notas(sesiones: Iterable[dict], ventana: int = VENTANA_DIAS,
                     limite: int = LIMITE_NOTAS, max_notas: int = MAX_NOTAS) -> list[str]:
    """Selecciona hasta max_notas recientes, distintas y sin texto vacío."""
    if not isinstance(ventana, int) or isinstance(ventana, bool) or ventana < 0:
        raise ValueError("ventana debe ser entero no negativo")
    if not isinstance(limite, int) or isinstance(limite, bool) or limite < 0:
        raise ValueError("limite debe ser entero no negativo")
    if not isinstance(max_notas, int) or isinstance(max_notas, bool) or max_notas < 0:
        raise ValueError("max_notas debe ser entero no negativo")
    candidatas = []
    for i, sesion in enumerate(sesiones):
        if not isinstance(sesion, dict):
            continue
        dias, nota = sesion.get("dias_atras"), sesion.get("nota")
        if not isinstance(dias, int) or isinstance(dias, bool) or not 0 <= dias <= ventana:
            continue
        if not isinstance(nota, str):
            continue
        normalizada = " ".join(nota.split()).strip()
        if normalizada:
            candidatas.append((dias, i, normalizada))
    candidatas.sort(key=lambda item: (item[0], item[1]))
    vistas, salida, total = set(), [], 0
    for _, _, nota in candidatas:
        clave = nota.casefold()
        if clave in vistas or len(salida) >= max_notas:
            continue
        if len(nota) > limite-total:
            nota = nota[:max(0, limite-total)].rstrip()
        if not nota:
            break
        vistas.add(clave)
        salida.append(nota)
        total += len(nota)
        if total == limite:
            break
    return salida


def construir_consulta(pregunta: str, sesiones: Iterable[dict],
                       ventana: int = VENTANA_DIAS) -> str:
    """Prepara texto para una recuperación futura, sin generar respuestas."""
    if not isinstance(pregunta, str) or not pregunta.strip():
        raise ValueError("la pregunta debe ser texto no vacío")
    base = " ".join(pregunta.split())
    notas = seleccionar_notas(sesiones, ventana=ventana)
    if not notas:
        return base
    return base + "\nContexto de registros recientes: " + " | ".join(notas)
