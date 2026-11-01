"""Validación del contrato; no es una evaluación clínica ni un RAG completo."""
import json
import unittest
from pathlib import Path
from codigo.evidencias import tokens, recuperar, decidir, evaluar_serie

ROOT = Path(__file__).resolve().parents[1]
DOCS = json.loads((ROOT / "datos" / "corpus.json").read_text(encoding="utf-8"))["documentos"]
QS = json.loads((ROOT / "datos" / "consultas.json").read_text(encoding="utf-8"))["consultas"]


class EvidenciasTest(unittest.TestCase):
    def test_normaliza_tildes(self):
        self.assertEqual(tokens("notificación"), tokens("notificacion"))

    def test_vacio_no_recupera(self):
        self.assertEqual(recuperar("", DOCS), [])

    def test_fuera_de_tema(self):
        self.assertEqual(decidir("tamaño de Júpiter", "diametro", DOCS)["estado"], "SIN_COINCIDENCIAS")

    def test_hay_candidatos(self):
        self.assertTrue(recuperar("convocatoria universitaria", DOCS))

    def test_cierre(self):
        self.assertEqual(decidir(QS[0]["pregunta"], QS[0]["campo"], DOCS)["fuente"], "DOC-02")

    def test_requisitos(self):
        self.assertEqual(decidir(QS[1]["pregunta"], QS[1]["campo"], DOCS)["fuente"], "DOC-03")

    def test_notificacion(self):
        self.assertEqual(decidir(QS[2]["pregunta"], QS[2]["campo"], DOCS)["fuente"], "DOC-04")

    def test_costo_sin_evidencia(self):
        self.assertEqual(decidir(QS[3]["pregunta"], QS[3]["campo"], DOCS)["estado"], "SIN_EVIDENCIA")

    def test_costo_no_inventado(self):
        self.assertIsNone(decidir(QS[3]["pregunta"], QS[3]["campo"], DOCS)["respuesta"])

    def test_error_campo_vacio(self):
        with self.assertRaises(ValueError):
            decidir("propuestas", "", DOCS)

    def test_serie_cinco(self):
        self.assertEqual(len(evaluar_serie(QS, DOCS)), 5)

    def test_estado_serie(self):
        self.assertEqual([r["estado"] for r in evaluar_serie(QS, DOCS)],
                         ["RESPALDADA"] * 3 + ["SIN_EVIDENCIA", "SIN_COINCIDENCIAS"])

    def test_no_mutacion(self):
        before = json.dumps(DOCS, sort_keys=True)
        evaluar_serie(QS, DOCS)
        self.assertEqual(json.dumps(DOCS, sort_keys=True), before)

    def test_sin_hecho_en_documento(self):
        docs = [dict(DOCS[1], hechos={})]
        self.assertEqual(decidir(QS[0]["pregunta"], "cierre", docs)["estado"], "SIN_EVIDENCIA")

    def test_cantidad_invalida(self):
        with self.assertRaises(ValueError):
            recuperar("fecha", DOCS, 0)

if __name__ == "__main__":
    unittest.main()
