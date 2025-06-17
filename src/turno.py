from datetime import datetime
from src.paciente import Paciente
from src.medico import Medico
class Turno:

    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora__ 
    def obtener_medico(self) -> Medico:
        return self.__medico__
    def obtener_paciente(self) -> Paciente:
        return self.__paciente__
    def obtener_especialidad(self) -> str:
        return self.__especialidad__
    def __str__(self) -> str:
        return f'Turno: Paciente: {self.__paciente__}, Médico: {self.__medico__}, Fecha y Hora: {self.__fecha_hora__}, Especialidad: {self.__especialidad__}'