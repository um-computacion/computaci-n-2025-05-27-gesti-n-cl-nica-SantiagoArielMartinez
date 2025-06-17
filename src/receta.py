from datetime import datetime
from typing import List
from src.paciente import Paciente
from src.medico import Medico
from src.turno import Turno
class Receta:

    def __init__(self, paciente :Paciente , medico :Medico, medicamentos :List[str]):
        self.__paciente__ = paciente     
        self.__medico__ = medico          
        self.__medicamentos__ = medicamentos  
        self.__fecha__ = datetime.now()
    def obtener_paciente(self) -> Paciente:
        return self.__paciente__
    
    def obtener_medico(self) -> Medico:
        return self.__medico__
    
    def obtener_medicamentos(self) -> List[str]:
        return self.__medicamentos__
    
    def obtener_fecha(self) -> datetime:
        return self.__fecha__


    def __str__(self) -> str:
        medicamentos_str = ", ".join(self.__medicamentos__)
        return f"Receta(Paciente({self.__paciente__}), Medico: ({self.__medico__}), Medicamentos: [{medicamentos_str}], Fecha: {self.__fecha__.strftime('%Y-%m-%d %H:%M:%S')})"