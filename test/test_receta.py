import unittest
from datetime import datetime
from unittest.mock import patch
from src.receta import Receta
from src.paciente import Paciente
from src.medico import Medico
from src.especialidad import Especialidad

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Juan Pérez", "1985-05-15")
        self.medico = Medico("98765", "Dr. María García")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)
        self.medicamentos = ["Aspirina 100mg", "Atorvastatina 20mg"]

    def test_01_crear_receta_exitosa(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        self.assertIsInstance(receta, Receta)
        self.assertEqual(receta.obtener_paciente(), self.paciente)
        self.assertEqual(receta.obtener_medico(), self.medico)
        self.assertEqual(receta.obtener_medicamentos(), self.medicamentos)

    def test_02_crear_receta_con_un_medicamento(self):
        medicamento_unico = ["Paracetamol 500mg"]
        receta = Receta(self.paciente, self.medico, medicamento_unico)
        self.assertEqual(receta.obtener_medicamentos(), medicamento_unico)
        self.assertEqual(len(receta.obtener_medicamentos()), 1)

    def test_03_crear_receta_con_multiples_medicamentos(self):
        medicamentos_multiples = [
            "Ibuprofeno 400mg",
            "Omeprazol 20mg",
            "Vitamina D 1000 UI",
            "Complejo B"
        ]
        receta = Receta(self.paciente, self.medico, medicamentos_multiples)
        self.assertEqual(len(receta.obtener_medicamentos()), 4)
        self.assertEqual(receta.obtener_medicamentos(), medicamentos_multiples)

    @patch('src.receta.datetime')
    def test_04_fecha_creacion_automatica(self, mock_datetime):
        fecha_mock = datetime(2024, 6, 15, 14, 30, 0)
        mock_datetime.now.return_value = fecha_mock
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        self.assertEqual(receta.obtener_fecha(), fecha_mock)
        mock_datetime.now.assert_called_once()

    def test_05_receta_con_medicamentos_nombres_largos(self):
        medicamentos_largos = [
            "Acetilsalicilato de lisina 900mg comprimidos efervescentes",
            "Clorhidrato de metformina 850mg comprimidos de liberación prolongada"
        ]
        receta = Receta(self.paciente, self.medico, medicamentos_largos)
        self.assertEqual(receta.obtener_medicamentos(), medicamentos_largos)

    def test_06_receta_con_paciente_diferente(self):
        paciente2 = Paciente("87654321", "Ana Martín", "1990-03-20")
        receta1 = Receta(self.paciente, self.medico, ["Medicamento A"])
        receta2 = Receta(paciente2, self.medico, ["Medicamento B"])
        self.assertNotEqual(receta1.obtener_paciente(), receta2.obtener_paciente())
        self.assertEqual(receta1.obtener_paciente().obtener_dni(), "12345678")
        self.assertEqual(receta2.obtener_paciente().obtener_dni(), "87654321")

    def test_07_receta_con_medico_diferente(self):
        medico2 = Medico("11111", "Dr. Carlos López")
        receta1 = Receta(self.paciente, self.medico, ["Medicamento A"])
        receta2 = Receta(self.paciente, medico2, ["Medicamento B"])
        self.assertNotEqual(receta1.obtener_medico(), receta2.obtener_medico())
        self.assertEqual(receta1.obtener_medico().obtener_matricula(), "98765")
        self.assertEqual(receta2.obtener_medico().obtener_matricula(), "11111")

    def test_08_str_representation_contiene_datos_basicos(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        str_representation = str(receta)
        self.assertIn("Receta", str_representation)
        self.assertIn("Paciente", str_representation)
        self.assertIn("Medico", str_representation)
        self.assertIn("Medicamentos", str_representation)
        self.assertIn("Aspirina 100mg", str_representation)
        self.assertIn("Atorvastatina 20mg", str_representation)

    def test_09_receta_con_lista_medicamentos_vacia(self):
        medicamentos_vacios = []
        receta = Receta(self.paciente, self.medico, medicamentos_vacios)
        self.assertEqual(receta.obtener_medicamentos(), medicamentos_vacios)
        self.assertEqual(len(receta.obtener_medicamentos()), 0)

    def test_10_consistencia_datos_despues_creacion(self):
        medicamentos_originales = ["Losartán 50mg", "Hidroclorotiazida 25mg"]
        receta = Receta(self.paciente, self.medico, medicamentos_originales)
        self.assertIs(receta.obtener_paciente(), self.paciente)
        self.assertIs(receta.obtener_medico(), self.medico)
        self.assertEqual(receta.obtener_medicamentos(), medicamentos_originales)
        self.assertIsInstance(receta.obtener_fecha(), datetime)

if __name__ == '__main__':
    unittest.main()