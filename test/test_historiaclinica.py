import unittest
from datetime import datetime
from src.historiaclinica import HistoriaClinica
from src.paciente import Paciente
from src.medico import Medico
from src.turno import Turno
from src.receta import Receta
from src.especialidad import Especialidad

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("12345678", "Juan Pérez", "1985-05-15")
        self.medico = Medico("98765", "Dr. María García")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.fecha_hora = datetime(2024, 6, 17, 10, 30)
        self.medicamentos = ["Aspirina 100mg", "Atorvastatina 20mg"]

    def test_01_crear_historia_clinica_exitosa(self):
        historia = HistoriaClinica(self.paciente)
        self.assertIsInstance(historia, HistoriaClinica)
        self.assertEqual(historia.obtener_paciente(), self.paciente)
        self.assertEqual(len(historia.obtener_turnos()), 0)
        self.assertEqual(len(historia.obtener_recetas()), 0)

    def test_02_agregar_turno_exitoso(self):
        historia = HistoriaClinica(self.paciente)
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Cardiología")
        historia.agregar_turno(turno)
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(historia.obtener_turnos()[0], turno)

    def test_03_agregar_multiple_turnos(self):
        historia = HistoriaClinica(self.paciente)
        turno1 = Turno(self.paciente, self.medico, self.fecha_hora, "Cardiología")
        turno2 = Turno(self.paciente, self.medico, datetime(2024, 6, 20, 14, 0), "Medicina General")
        turno3 = Turno(self.paciente, self.medico, datetime(2024, 6, 25, 9, 30), "Cardiología")
        historia.agregar_turno(turno1)
        historia.agregar_turno(turno2)
        historia.agregar_turno(turno3)
        self.assertEqual(len(historia.obtener_turnos()), 3)
        self.assertIn(turno1, historia.obtener_turnos())
        self.assertIn(turno2, historia.obtener_turnos())
        self.assertIn(turno3, historia.obtener_turnos())

    def test_04_agregar_receta_exitosa(self):
        historia = HistoriaClinica(self.paciente)
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        historia.agregar_receta(receta)
        self.assertEqual(len(historia.obtener_recetas()), 1)
        self.assertEqual(historia.obtener_recetas()[0], receta)

    def test_05_agregar_multiples_recetas(self):
        historia = HistoriaClinica(self.paciente)
        receta1 = Receta(self.paciente, self.medico, ["Medicamento A"])
        receta2 = Receta(self.paciente, self.medico, ["Medicamento B", "Medicamento C"])
        receta3 = Receta(self.paciente, self.medico, ["Medicamento D"])
        historia.agregar_receta(receta1)
        historia.agregar_receta(receta2)
        historia.agregar_receta(receta3)
        self.assertEqual(len(historia.obtener_recetas()), 3)
        self.assertIn(receta1, historia.obtener_recetas())
        self.assertIn(receta2, historia.obtener_recetas())
        self.assertIn(receta3, historia.obtener_recetas())

    def test_06_obtener_turnos_lista_vacia_inicial(self):
        historia = HistoriaClinica(self.paciente)
        turnos = historia.obtener_turnos()
        self.assertIsInstance(turnos, list)
        self.assertEqual(len(turnos), 0)

    def test_07_obtener_recetas_lista_vacia_inicial(self):
        historia = HistoriaClinica(self.paciente)
        recetas = historia.obtener_recetas()
        self.assertIsInstance(recetas, list)
        self.assertEqual(len(recetas), 0)

    def test_08_historia_completa_con_turnos_y_recetas(self):
        historia = HistoriaClinica(self.paciente)
        turno1 = Turno(self.paciente, self.medico, self.fecha_hora, "Cardiología")
        turno2 = Turno(self.paciente, self.medico, datetime(2024, 6, 20, 14, 0), "Medicina General")
        historia.agregar_turno(turno1)
        historia.agregar_turno(turno2)
        receta1 = Receta(self.paciente, self.medico, ["Medicamento A"])
        receta2 = Receta(self.paciente, self.medico, ["Medicamento B"])
        historia.agregar_receta(receta1)
        historia.agregar_receta(receta2)
        self.assertEqual(len(historia.obtener_turnos()), 2)
        self.assertEqual(len(historia.obtener_recetas()), 2)

    def test_09_str_representation_contiene_datos(self):
        historia = HistoriaClinica(self.paciente)
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Cardiología")
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        historia.agregar_turno(turno)
        historia.agregar_receta(receta)
        str_representation = str(historia)
        self.assertIn("HistoriaClinica", str_representation)
        self.assertIn("Paciente", str_representation)

    def test_10_integridad_datos_despues_operaciones(self):
        historia = HistoriaClinica(self.paciente)
        turno_inicial = Turno(self.paciente, self.medico, self.fecha_hora, "Cardiología")
        receta_inicial = Receta(self.paciente, self.medico, ["Medicamento Inicial"])
        historia.agregar_turno(turno_inicial)
        historia.agregar_receta(receta_inicial)
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(len(historia.obtener_recetas()), 1)
        turno_adicional = Turno(self.paciente, self.medico, datetime(2024, 6, 25, 11, 0), "Medicina General")
        receta_adicional = Receta(self.paciente, self.medico, ["Medicamento Adicional"])
        historia.agregar_turno(turno_adicional)
        historia.agregar_receta(receta_adicional)
        self.assertEqual(len(historia.obtener_turnos()), 2)
        self.assertEqual(len(historia.obtener_recetas()), 2)
        self.assertIn(turno_inicial, historia.obtener_turnos())
        self.assertIn(receta_inicial, historia.obtener_recetas())
        self.assertIn(turno_adicional, historia.obtener_turnos())
        self.assertIn(receta_adicional, historia.obtener_recetas())

if __name__ == '__main__':
    unittest.main()