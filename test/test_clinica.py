import unittest
from datetime import datetime
from src.clinica import (
    Clinica, 
    PacienteNoEncontradoException, 
    MedicoNoDisponibleException, 
    TurnoOcupadoException,
    RecetaInvalidaException
)
from src.paciente import Paciente
from src.medico import Medico
from src.especialidad import Especialidad

class TestClinica(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("12345678", "Juan Pérez", "1985-05-15")
        self.medico = Medico("98765", "Dr. María García")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)

    def test_01_crear_clinica_exitosa(self):
        clinica = Clinica()
        self.assertIsInstance(clinica, Clinica)
        self.assertEqual(len(clinica.obtener_pacientes()), 0)
        self.assertEqual(len(clinica.obtener_medicos()), 0)
        self.assertEqual(len(clinica.obtener_turnos()), 0)

    def test_02_agregar_paciente_exitoso(self):
        self.clinica.agregar_paciente(self.paciente)
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)
        self.assertIn(self.paciente, pacientes)

    def test_03_agregar_paciente_duplicado_falla(self):
        self.clinica.agregar_paciente(self.paciente)
        paciente_duplicado = Paciente("12345678", "Otro Nombre", "1990-01-01")
        with self.assertRaises(ValueError) as context:
            self.clinica.agregar_paciente(paciente_duplicado)
        self.assertIn("ya está registrado", str(context.exception))

    def test_04_agregar_medico_exitoso(self):
        self.clinica.agregar_medico(self.medico)
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertIn(self.medico, medicos)

    def test_05_agregar_medico_duplicado_falla(self):
        self.clinica.agregar_medico(self.medico)
        medico_duplicado = Medico("98765", "Dr. Otro Nombre")
        with self.assertRaises(MedicoNoDisponibleException) as context:
            self.clinica.agregar_medico(medico_duplicado)
        self.assertIn("ya está registrado", str(context.exception))

    def test_06_agendar_turno_exitoso(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        fecha_lunes = datetime(2024, 6, 17, 10, 30)  # Lunes
        self.clinica.agendar_turno(
            self.paciente.obtener_dni(),
            self.medico.obtener_matricula(),
            "Cardiología",
            fecha_lunes
        )
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_07_agendar_turno_paciente_no_existe_falla(self):
        self.clinica.agregar_medico(self.medico)
        fecha_lunes = datetime(2024, 6, 17, 10, 30)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno(
            "DNI_INEXISTENTE",
            self.medico.obtener_matricula(),
            "Cardiología",
            fecha_lunes
    )
            
    def test_08_agendar_turno_medico_no_existe_falla(self):
        self.clinica.agregar_paciente(self.paciente)
        fecha_lunes = datetime(2025, 6, 17, 10, 30)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno(
                self.paciente.obtener_dni(),
                "MATRICULA_INEXISTENTE",
                "Cardiología",
                fecha_lunes
            )

    def test_09_emitir_receta_exitosa(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        medicamentos = ["Aspirina 100mg", "Atorvastatina 20mg"]
        try:
            self.clinica.emitir_receta(
                self.paciente.obtener_dni(),
                self.medico.obtener_matricula(),
                medicamentos
            )
        except Exception as e:
            self.fail(f"emitir_receta() lanzó excepción inesperada: {e}")
        
    def test_10_emitir_receta_sin_medicamentos_falla(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        medicamentos_vacios = []
        with self.assertRaises(RecetaInvalidaException) as context:
            self.clinica.emitir_receta(
                self.paciente.obtener_dni(),
                self.medico.obtener_matricula(),
                medicamentos_vacios
            )
        self.assertIn("no puede estar vacía", str(context.exception))

if __name__ == '__main__':
    unittest.main()