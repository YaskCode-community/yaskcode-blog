"""Demostración local con datos sintéticos de recorridos."""
import json
from pathlib import Path
from .consultas import construir_consulta, seleccionar_notas

def ejecutar():
    path = Path(__file__).resolve().parents[1] / "datos" / "sesiones.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        "notas_incluidas": seleccionar_notas(data["sesiones"]),
        "consulta": construir_consulta(data["pregunta"], data["sesiones"])
    }

if __name__ == "__main__":
    print(json.dumps(ejecutar(), ensure_ascii=False, indent=2))
