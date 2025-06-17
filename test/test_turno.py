import unittest
from datetime import datetime
from src.turno import Turno
from src.paciente import Paciente
from src.medico import Medico
from src.especialidad import Especialidad

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Juan Pérez", "1985-05-15")
        self.medico = Medico("98765", "Dr. María García")
        self.especialidad_obj = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad_obj)
        self.fecha_hora = datetime(2024, 6, 17, 10, 30)  # Lunes a las 10:30
        self.especialidad_str = "Cardiología"

    def test_01_crear_turno_exitoso(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad_str)
        self.assertIsInstance(turno, Turno)
        self.assertEqual(turno.obtener_paciente(), self.paciente)
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)
        self.assertEqual(turno.obtener_especialidad(), self.especialidad_str)

    def test_02_obtener_fecha_hora_correcta(self):
        fecha_esperada = datetime(2024, 12, 25, 14, 45)
        turno = Turno(self.paciente, self.medico, fecha_esperada, self.especialidad_str)
        self.assertEqual(turno.obtener_fecha_hora(), fecha_esperada)
        self.assertIsInstance(turno.obtener_fecha_hora(), datetime)

    def test_03_obtener_medico_correcto(self):
        medico_especifico = Medico("11111", "Dr. Carlos López")
        turno = Turno(self.paciente, medico_especifico, self.fecha_hora, self.especialidad_str)
        self.assertEqual(turno.obtener_medico(), medico_especifico)
        self.assertEqual(turno.obtener_medico().obtener_matricula(), "11111")

    def test_04_obtener_paciente_correcto(self):
        paciente_especifico = Paciente("87654321", "Ana Martín", "1990-03-20")
        turno = Turno(paciente_especifico, self.medico, self.fecha_hora, self.especialidad_str)
        self.assertEqual(turno.obtener_paciente(), paciente_especifico)
        self.assertEqual(turno.obtener_paciente().obtener_dni(), "87654321")

    def test_05_obtener_especialidad_correcta(self):
        especialidad_especifica = "Dermatología"
        turno = Turno(self.paciente, self.medico, self.fecha_hora, especialidad_especifica)
        self.assertEqual(turno.obtener_especialidad(), especialidad_especifica)

    def test_06_turno_con_diferentes_especialidades(self):
        turno1 = Turno(self.paciente, self.medico, self.fecha_hora, "Cardiología")
        turno2 = Turno(self.paciente, self.medico, self.fecha_hora, "Medicina General")
        self.assertEqual(turno1.obtener_especialidad(), "Cardiología")
        self.assertEqual(turno2.obtener_especialidad(), "Medicina General")
        self.assertNotEqual(turno1.obtener_especialidad(), turno2.obtener_especialidad())

    def test_07_turno_con_fecha_futura(self):
        fecha_futura = datetime(2025, 12, 31, 9, 0)
        turno = Turno(self.paciente, self.medico, fecha_futura, self.especialidad_str)
        self.assertEqual(turno.obtener_fecha_hora(), fecha_futura)
        self.assertGreater(turno.obtener_fecha_hora(), datetime.now())

    def test_08_turno_con_fecha_pasada(self):
        fecha_pasada = datetime(2020, 1, 1, 8, 30)
        turno = Turno(self.paciente, self.medico, fecha_pasada, self.especialidad_str)
        self.assertEqual(turno.obtener_fecha_hora(), fecha_pasada)
        self.assertLess(turno.obtener_fecha_hora(), datetime.now())

    def test_09_str_representation_contiene_datos(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad_str)
        str_representation = str(turno)
        self.assertIn("Turno", str_representation)
        self.assertIn("Paciente", str_representation)
        self.assertIn("Médico", str_representation)
        self.assertIn("Fecha", str_representation)
        self.assertIn("Especialidad", str_representation)

    def test_10_consistencia_datos_despues_creacion(self):
        turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad_str)
        self.assertEqual(turno.obtener_paciente(), turno.obtener_paciente())
        self.assertEqual(turno.obtener_medico(), turno.obtener_medico())
        self.assertEqual(turno.obtener_fecha_hora(), turno.obtener_fecha_hora())
        self.assertEqual(turno.obtener_especialidad(), turno.obtener_especialidad())
        self.assertIs(turno.obtener_paciente(), self.paciente)
        self.assertIs(turno.obtener_medico(), self.medico)

if __name__ == '__main__':
    unittest.main()