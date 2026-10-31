"""Pruebas unitarias de la evaluación sintética, solo biblioteca estándar."""
import unittest
from fractions import Fraction
from codigo.metricas import CONSULTAS, medir, resumen

class MetricasTest(unittest.TestCase):
    def test_q1(self):
        self.assertEqual(medir({"A","B"},["A","C","B"]),{"precision":Fraction(2,3),"recall":Fraction(1),"rr":Fraction(1)})
    def test_q2(self):
        self.assertEqual(medir({"D","E"},["X","D","Y"])["rr"], Fraction(1,2))
    def test_q3(self):
        self.assertEqual(medir({"F"},["G","H","F"])["rr"], Fraction(1,3))
    def test_precision_media(self):
        self.assertEqual(resumen()[1]["precision"], Fraction(4,9))
    def test_recall_media(self):
        self.assertEqual(resumen()[1]["recall"], Fraction(5,6))
    def test_mrr(self):
        self.assertEqual(resumen()[1]["rr"], Fraction(11,18))
    def test_sin_relevante_entre_top(self):
        self.assertEqual(medir({"A"},["B","C","D"])["rr"], 0)
    def test_no_relevantes_conocidos(self):
        with self.assertRaises(ValueError): medir(set(),["B","C","D"])
    def test_rechaza_top_corto(self):
        with self.assertRaises(ValueError): medir({"A"},["A"])
    def test_k_invalido(self):
        with self.assertRaises(ValueError): medir({"A"},["A","B","C"],0)
    def test_no_duplicados(self):
        with self.assertRaises(ValueError): medir({"A"},["A","A","C"])
    def test_sin_consultas(self):
        with self.assertRaises(ValueError): resumen([])
    def test_conjunto_constante(self):
        self.assertEqual(len(CONSULTAS),3)

if __name__=="__main__":
    unittest.main()
