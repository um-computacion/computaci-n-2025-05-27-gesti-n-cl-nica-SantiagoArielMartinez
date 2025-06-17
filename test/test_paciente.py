import unittest
from src.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_01_crear_paciente_exitoso(self):
        paciente = Paciente("12345678", "Juan Pérez", "1985-05-15")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertIsInstance(paciente, Paciente)

    def test_02_obtener_dni_correcto(self):
        dni_esperado = "87654321"
        paciente = Paciente(dni_esperado, "María García", "1990-12-03")
        self.assertEqual(paciente.obtener_dni(), dni_esperado)

    def test_03_crear_paciente_con_dni_numerico_string(self):
        paciente = Paciente("45123789", "Carlos López", "1978-08-22")
        self.assertEqual(paciente.obtener_dni(), "45123789")
        self.assertIsInstance(paciente.obtener_dni(), str)

    def test_04_crear_paciente_con_nombre_compuesto(self):
        paciente = Paciente("11223344", "Ana María Rodríguez González", "1995-01-10")
        self.assertEqual(paciente.obtener_dni(), "11223344")
        self.assertIsNotNone(paciente)

    def test_05_crear_paciente_con_fecha_formato_diferente(self):
        paciente = Paciente("99887766", "Roberto Silva", "2000-06-30")
        self.assertEqual(paciente.obtener_dni(), "99887766")

    def test_06_str_representation_contiene_datos_basicos(self):
        paciente = Paciente("55443322", "Laura Martín", "1988-11-15")
        str_representation = str(paciente)
        self.assertIn("55443322", str_representation)
        self.assertIn("Laura Martín", str_representation)
        self.assertIn("1988-11-15", str_representation)

    def test_07_crear_paciente_con_dni_con_espacios(self):
        paciente = Paciente(" 12345678 ", "Pedro González", "1980-04-25")
        self.assertEqual(paciente.obtener_dni(), " 12345678 ")

    def test_08_crear_paciente_con_nombre_vacio(self):
        paciente = Paciente("77889900", "", "1992-09-18")
        self.assertEqual(paciente.obtener_dni(), "77889900")

    def test_09_crear_multiples_pacientes_diferentes(self):
        paciente1 = Paciente("11111111", "Paciente Uno", "1985-01-01")
        paciente2 = Paciente("22222222", "Paciente Dos", "1990-02-02")
        self.assertNotEqual(paciente1.obtener_dni(), paciente2.obtener_dni())
        self.assertEqual(paciente1.obtener_dni(), "11111111")
        self.assertEqual(paciente2.obtener_dni(), "22222222")

    def test_10_consistencia_datos_despues_creacion(self):
        dni_original = "33445566"
        nombre_original = "Sofía Hernández"
        fecha_original = "1987-07-12"
        paciente = Paciente(dni_original, nombre_original, fecha_original)
        self.assertEqual(paciente.obtener_dni(), dni_original)
        self.assertEqual(paciente.obtener_dni(), paciente.obtener_dni())

if __name__ == '__main__':
    unittest.main()