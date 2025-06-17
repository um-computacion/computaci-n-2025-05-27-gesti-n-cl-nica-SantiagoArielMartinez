import unittest
from src.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_01_crear_especialidad_con_un_dia(self):
        especialidad = Especialidad("Cardiología", ["lunes"])
        self.assertEqual(especialidad.obtener_especialidad(), "Cardiología")
        self.assertEqual(especialidad.obtener_dias(), ["lunes"])

    def test_02_crear_especialidad_con_multiples_dias(self):
        dias = ["lunes", "miércoles", "viernes"]
        especialidad = Especialidad("Dermatología", dias)
        self.assertEqual(especialidad.obtener_especialidad(), "Dermatología")
        self.assertEqual(len(especialidad.obtener_dias()), 3)
        self.assertIn("lunes", especialidad.obtener_dias())
        self.assertIn("miércoles", especialidad.obtener_dias())
        self.assertIn("viernes", especialidad.obtener_dias())

    def test_03_verificar_dia_existente_minusculas(self):
        especialidad = Especialidad("Pediatría", ["martes", "jueves"])
        self.assertTrue(especialidad.verificar_dia("martes"))
        self.assertTrue(especialidad.verificar_dia("jueves"))

    def test_04_verificar_dia_existente_mayusculas(self):
        especialidad = Especialidad("Neurología", ["lunes", "miércoles"])
        self.assertTrue(especialidad.verificar_dia("LUNES"))
        self.assertTrue(especialidad.verificar_dia("Miércoles"))
        self.assertTrue(especialidad.verificar_dia("MIÉRCOLES"))

    def test_05_verificar_dia_no_existente(self):
        especialidad = Especialidad("Traumatología", ["lunes", "viernes"])
        self.assertFalse(especialidad.verificar_dia("martes"))
        self.assertFalse(especialidad.verificar_dia("sábado"))
        self.assertFalse(especialidad.verificar_dia("domingo"))

    def test_06_obtener_especialidad_correcta(self):
        nombre_especialidad = "Ginecología"
        especialidad = Especialidad(nombre_especialidad, ["martes"])
        self.assertEqual(especialidad.obtener_especialidad(), nombre_especialidad)

    def test_07_obtener_dias_lista_completa(self):
        dias_originales = ["lunes", "martes", "miércoles", "jueves", "viernes"]
        especialidad = Especialidad("Medicina General", dias_originales)
        dias_obtenidos = especialidad.obtener_dias()
        self.assertEqual(len(dias_obtenidos), 5)
        for dia in dias_originales:
            self.assertIn(dia, dias_obtenidos)

    def test_08_case_insensitive_en_construccion(self):
        especialidad = Especialidad("Oftalmología", ["LUNES", "Martes", "MIÉRCOLES"])
        dias = especialidad.obtener_dias()
        self.assertIn("lunes", dias)
        self.assertIn("martes", dias)
        self.assertIn("miércoles", dias)

    def test_09_str_representation_contiene_datos(self):
        especialidad = Especialidad("Psiquiatría", ["lunes", "miércoles"])
        str_representation = str(especialidad)
        self.assertIn("Psiquiatría", str_representation)
        self.assertIn("lunes", str_representation)
        self.assertIn("miércoles", str_representation)

    def test_10_crear_especialidad_con_dias_repetidos(self):
        # El sistema debería manejar días duplicados
        especialidad = Especialidad("Urología", ["lunes", "lunes", "martes", "martes"])
        self.assertEqual(especialidad.obtener_especialidad(), "Urología")
        # Verificar que los días duplicados se manejan correctamente
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertTrue(especialidad.verificar_dia("martes"))

if __name__ == '__main__':
    unittest.main()