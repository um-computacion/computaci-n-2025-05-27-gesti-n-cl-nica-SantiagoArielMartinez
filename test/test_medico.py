import unittest
from src.medico import Medico
from src.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def test_01_crear_medico_sin_especialidades(self):
        medico = Medico("12345", "Dr. Juan Pérez")
        self.assertEqual(medico.obtener_matricula(), "12345")
        self.assertEqual(len(medico.obtener_especialidad_para_dia("")), 0)

    def test_02_crear_medico_con_especialidades_iniciales(self):
        especialidad1 = Especialidad("Cardiología", ["lunes", "miércoles"])
        especialidad2 = Especialidad("Medicina General", ["martes", "jueves"])
        especialidades = [especialidad1, especialidad2]
        medico = Medico("67890", "Dra. María García", especialidades)
        self.assertEqual(medico.obtener_matricula(), "67890")
        self.assertEqual(len(medico.obtener_especialidad_para_dia("lunes, martes")), 2)

    def test_03_agregar_especialidad_nueva(self):
        medico = Medico("11111", "Dr. Carlos López")
        especialidad = Especialidad("Pediatría", ["lunes", "viernes"])
        medico.agregar_especialidad(especialidad)
        self.assertEqual(len(medico.obtener_especialidad_para_dia("lunes, viernes")), 1)
        self.assertIn("Pediatría", medico.obtener_especialidad_para_dia("lunes"))

    def test_04_agregar_multiples_especialidades(self):
        medico = Medico("22222", "Dra. Ana Martín")
        especialidad1 = Especialidad("Dermatología", ["lunes"])
        especialidad2 = Especialidad("Alergología", ["miércoles"])
        especialidad3 = Especialidad("Inmunología", ["viernes"])
        medico.agregar_especialidad(especialidad1)
        medico.agregar_especialidad(especialidad2)
        medico.agregar_especialidad(especialidad3)
        self.assertEqual(len(medico.obtener_especialidad_para_dia("lunes, miércoles,viernes")), 3)

    def test_05_obtener_especialidad_para_dia_existente(self):
        especialidad = Especialidad("Traumatología", ["lunes", "miércoles"])
        medico = Medico("33333", "Dr. Roberto Silva")
        medico.agregar_especialidad(especialidad)
        resultado = medico.obtener_especialidad_para_dia("lunes")
        self.assertEqual(resultado, ["Traumatología"])

    def test_06_obtener_especialidad_para_dia_no_existente(self):
        especialidad = Especialidad("Neurología", ["martes", "jueves"])
        medico = Medico("44444", "Dra. Laura González")
        medico.agregar_especialidad(especialidad) 
        resultado = medico.obtener_especialidad_para_dia("lunes")
        self.assertEqual(resultado, [])

    def test_07_obtener_matricula_correcta(self):
        matricula_esperada = "98765"
        medico = Medico(matricula_esperada, "Dr. Pedro Ramírez")
        self.assertEqual(medico.obtener_matricula(), matricula_esperada)

    def test_08_medico_con_especialidad_multiple_dias(self):
        especialidad = Especialidad("Medicina General", ["lunes", "martes", "miércoles", "jueves", "viernes"])
        medico = Medico("55555", "Dr. Fernando Torres")
        medico.agregar_especialidad(especialidad)
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), ["Medicina General"])
        self.assertEqual(medico.obtener_especialidad_para_dia("miércoles"), ["Medicina General"])
        self.assertEqual(medico.obtener_especialidad_para_dia("viernes"), ["Medicina General"])
        self.assertEqual(medico.obtener_especialidad_para_dia("sábado"), [])

    def test_09_medico_multiples_especialidades_diferentes_dias(self):
        especialidad1 = Especialidad("Cardiología", ["lunes", "miércoles"])
        especialidad2 = Especialidad("Medicina General", ["martes", "jueves"])
        medico = Medico("66666", "Dra. Carmen Ruiz")
        medico.agregar_especialidad(especialidad1)
        medico.agregar_especialidad(especialidad2)
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), ["Cardiología"])
        self.assertEqual(medico.obtener_especialidad_para_dia("martes"), ["Medicina General"])
        self.assertEqual(medico.obtener_especialidad_para_dia("miércoles"), ["Cardiología"])
        self.assertEqual(medico.obtener_especialidad_para_dia("jueves"), ["Medicina General"])
        self.assertEqual(medico.obtener_especialidad_para_dia("viernes"), [])

    def test_10_str_representation_contiene_datos(self):
        especialidad = Especialidad("Oftalmología", ["lunes"])
        medico = Medico("77777", "Dr. Miguel Herrera")
        medico.agregar_especialidad(especialidad)
        str_representation = str(medico)
        self.assertIn("Dr. Miguel Herrera", str_representation)
        self.assertIn("77777", str_representation)
        self.assertIn("Oftalmología", str_representation)

if __name__ == '__main__':
    unittest.main()