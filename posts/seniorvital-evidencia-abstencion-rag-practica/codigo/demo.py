"""Demostración reproducible sin conexión ni servicios externos."""
from pathlib import Path
import json
from .evidencias import evaluar_serie

ROOT = Path(__file__).resolve().parents[1]


def ejecutar():
    docs = json.loads((ROOT / "datos" / "corpus.json").read_text(encoding="utf-8"))
    qs = json.loads((ROOT / "datos" / "consultas.json").read_text(encoding="utf-8"))
    return evaluar_serie(qs["consultas"], docs["documentos"])


if __name__ == "__main__":
    print(json.dumps(ejecutar(), ensure_ascii=False, indent=2))
