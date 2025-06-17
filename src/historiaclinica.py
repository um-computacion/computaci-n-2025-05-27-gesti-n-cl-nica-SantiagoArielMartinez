from datetime import datetime
from typing import List, Optional, Dict
from src.paciente import Paciente
from src.turno import Turno
from src.receta import Receta

class HistoriaClinica:

    def __init__(self, paciente: Paciente):
        self.__paciente__ = paciente
        self.__turnos__ : List[Turno] = []
        self.__recetas__ : List[Receta] = []

    def agregar_turno(self, turno: Turno):
        self.__turnos__.append(turno)
    
    def agregar_receta(self, receta: Receta):
        self.__recetas__.append(receta)

    def obtener_turnos(self) -> List[Turno]:
        return self.__turnos__
    
    def obtener_recetas(self) -> List[Receta]:
        return self.__recetas__
    def obtener_paciente(self) -> Paciente:
        return self.__paciente__
    def __str__(self) -> str:
        turnos_str = "\n".join(str(turno) for turno in self.__turnos__)
        recetas_str = "\n".join(str(receta) for receta in self.__recetas__)
        return f"HistoriaClinica(Paciente({self.__paciente__}), [{turnos_str}], [{recetas_str}])"