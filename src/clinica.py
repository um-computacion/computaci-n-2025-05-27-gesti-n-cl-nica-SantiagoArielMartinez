from datetime import datetime
from typing import List, Dict
from src.paciente import Paciente
from src.medico import Medico
from src.historiaclinica import HistoriaClinica
from src.turno import Turno
from src.receta import Receta

class PacienteNoEncontradoException(Exception):
    pass
class MedicoNoDisponibleException(Exception):
    pass
class TurnoOcupadoException(Exception):
    pass
class RecetaInvalidaException(Exception):
    pass

class Clinica:

    def __init__(self):
        self.__paciente__: Dict[str, Paciente] = {}
        self.__medico__: Dict[str, Medico] = {}
        self.__historias_clinicas__: Dict[str, HistoriaClinica] = {}
        self.__turnos__: List[Turno] = []

    def agregar_paciente(self, paciente : Paciente):
        
            dni = paciente.obtener_dni()
            if dni in self.__paciente__:
                raise ValueError(f"El paciente con DNI {dni} ya está registrado")
            self.__paciente__[dni] = paciente
            self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico : Medico):
            matricula = medico.obtener_matricula()
            if matricula in self.__medico__:
                raise MedicoNoDisponibleException(f"El médico con matrícula {matricula} ya está registrado")
            self.__medico__[matricula] = medico
    
    def agregar_especialidad_a_medico(self, matricula: str, especialidad):
        """Agrega una especialidad a un médico ya registrado."""
        if matricula not in self.__medico__:
            raise MedicoNoDisponibleException(f"El médico con matrícula {matricula} no está registrado")
        medico = self.__medico__[matricula]
        medico.agregar_especialidad(especialidad)
        

    def agendar_turno(self, dni:str , matricula:str , especialidad:str, fecha_hora:datetime):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        if isinstance(fecha_hora, str):
            fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M:%S")
        dia = self.obtener_dia_semana_en_espanol(fecha_hora)
        medico = self.__medico__[matricula]
        especialidad_disponible = medico.obtener_especialidad_para_dia(dia)
        if especialidad not in especialidad_disponible:
            raise MedicoNoDisponibleException(f"El médico {medico.obtener_matricula()} no tiene la especialidad {especialidad} para el día {dia}")
        self.validar_turno(dni, matricula, especialidad, fecha_hora)
        turno = Turno(self.__paciente__[dni], medico, fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)
        
    def obtener_pacientes(self) -> List[Paciente]:
        return list(self.__paciente__.values())
    
    def obtener_medicos(self) -> List[Medico]:
        return list(self.__medico__.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        medico = self.__medico__.get(matricula)
        if not medico:
            raise MedicoNoDisponibleException(f"El médico con matrícula {matricula} no está registrado")
        return medico
    
    def obtener_turnos(self) -> List[Turno]:
        return self.__turnos__
    
    def emitir_receta(self, dni:str, matricula: str, medicamentos: List[str]):
            self.validar_existencia_paciente(dni)
            self.validar_existencia_medico(matricula)
            
            if not medicamentos or len(medicamentos) == 0:
                raise RecetaInvalidaException("La lista de medicamentos no puede estar vacía")
        
            receta = Receta(self.__paciente__[dni], self.__medico__[matricula], medicamentos)
            self.__historias_clinicas__[dni].agregar_receta(receta)
            

    def obtener_historiales_por_dni(self, dni: str) -> HistoriaClinica:
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas__[dni]

    #validaciones
    
    
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__paciente__:
            raise PacienteNoEncontradoException(f"El paciente con DNI {dni} no está registrado")


    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medico__:
            raise MedicoNoDisponibleException(f"El médico con matrícula {matricula} no está registrado")


    def validar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
       turno = Turno(self.__paciente__[dni], self.__medico__[matricula], fecha_hora, especialidad)
       if turno in self.__turnos__:
            if turno.obtener_medico().obtener_matricula() == matricula and turno.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException(f"Ya existe un turno agendado para el paciente {dni} con el médico {matricula} en la fecha y hora {fecha_hora}")
    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado","domingo"]
        return dias[fecha_hora.weekday()]
    
    def obtener_especialidad_disponible(self, medico: Medico, dia: str) -> str:
        return medico.obtener_especialidad_para_dia(dia)
    

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str, matricula:Medico) -> bool:
        especialidad_disponible = medico.obtener_especialidad_para_dia(dia_semana)
        if especialidad_disponible is None:
           raise MedicoNoDisponibleException(f"El médico {medico.obtener_matricula()} no tiene la especialidad {especialidad_solicitada} para el día {dia_semana}")

        if especialidad_disponible not in especialidad_solicitada:
            raise MedicoNoDisponibleException(f"La especialidad {especialidad_solicitada} no está disponible para el médico {medico.obtener_matricula()} en el día {dia_semana}")

    def validar_receta(self, dni: Paciente, matricula: Medico, medicamentos: List[Receta]):
        # Validate patient exists
        paciente = self.obtener_historiales_por_dni(dni)
        if not paciente:
            raise RecetaInvalidaException("Paciente no encontrado")

    # Validate doctor exists
        medico = self.obtener_medico_por_matricula(matricula)
        if not medico:
            raise MedicoNoDisponibleException("Médico no encontrado")
    
    # Validate medications list is not empty
        if not medicamentos or len(medicamentos) == 0:
            raise RecetaInvalidaException("La lista de medicamentos no puede estar vacía")