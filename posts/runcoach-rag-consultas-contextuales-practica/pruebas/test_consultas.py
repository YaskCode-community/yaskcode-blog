import json
import unittest
from pathlib import Path
from codigo.consultas import seleccionar_notas, construir_consulta

class ConsultasTest(unittest.TestCase):
    def test_sin_sesiones(self): self.assertEqual(seleccionar_notas([]), [])
    def test_sin_notas(self): self.assertEqual(seleccionar_notas([{"dias_atras":1}]), [])
    def test_blancos(self): self.assertEqual(seleccionar_notas([{"dias_atras":1,"nota":"  "}]), [])
    def test_fuera_ventana(self): self.assertEqual(seleccionar_notas([{"dias_atras":8,"nota":"fuera"}]), [])
    def test_limite_incluido(self): self.assertEqual(seleccionar_notas([{"dias_atras":7,"nota":"limite"}]), ["limite"])
    def test_futuro_no_entra(self): self.assertEqual(seleccionar_notas([{"dias_atras":-1,"nota":"futuro"}]), [])
    def test_dias_no_parseables(self): self.assertEqual(seleccionar_notas([{"dias_atras":"desconocido","nota":"x"}]), [])
    def test_bool_no_es_dia(self): self.assertEqual(seleccionar_notas([{"dias_atras":True,"nota":"x"}]), [])
    def test_notas_no_texto(self): self.assertEqual(seleccionar_notas([{"dias_atras":1,"nota":45}]), [])
    def test_recientes_primero(self):
        value=seleccionar_notas([{"dias_atras":5,"nota":"a"},{"dias_atras":1,"nota":"b"}])
        self.assertEqual(value,["b","a"])
    def test_se_eliminan_duplicados_normalizados(self):
        value=seleccionar_notas([{"dias_atras":1,"nota":"Lluvia fuerte"},{"dias_atras":2,"nota":"  lluvia   fuerte "}])
        self.assertEqual(len(value),1)
    def test_limite_numero(self):
        value=seleccionar_notas([{"dias_atras":x,"nota":str(x)} for x in range(7)], max_notas=2)
        self.assertEqual(len(value),2)
    def test_limite_caracteres(self):
        value=seleccionar_notas([{"dias_atras":1,"nota":"x"*500}], limite=28)
        self.assertEqual(len("".join(value)),28)
    def test_limite_cero(self):
        self.assertEqual(seleccionar_notas([{"dias_atras":0,"nota":"x"}], limite=0),[])
    def test_no_agregar_bloque_si_sin_notas(self):
        self.assertEqual(construir_consulta("¿Qué revisar?",[]),"¿Qué revisar?")
    def test_consulta_contiene_nota(self):
        self.assertIn("lluvia",construir_consulta("Ruta",[{"dias_atras":1,"nota":"lluvia"}]))
    def test_sin_respuesta_generada(self):
        self.assertNotIn("Recomendación:", construir_consulta("Ruta",[]))
    def test_pregunta_vacia_rechazada(self):
        with self.assertRaises(ValueError): construir_consulta(" ",[])
    def test_ventana_invalida(self):
        with self.assertRaises(ValueError): seleccionar_notas([],ventana=-1)
    def test_dato_original_no_modificado(self):
        data=[{"dias_atras":1,"nota":"  nota  "}]
        seleccionar_notas(data)
        self.assertEqual(data[0]["nota"],"  nota  ")
    def test_dataset_archivo(self):
        path=Path(__file__).resolve().parents[1]/"datos"/"sesiones.json"
        data=json.loads(path.read_text(encoding="utf-8"))
        result=seleccionar_notas(data["sesiones"])
        self.assertEqual(result,["Lluvia durante la salida",
                                  "Señal de mantenimiento en el parque",
                                  "Ruta alternativa señalizada"])

if __name__ == "__main__":
    unittest.main()
