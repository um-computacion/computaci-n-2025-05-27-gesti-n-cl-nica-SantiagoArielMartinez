from datetime import datetime
from typing import List

class Especialidad:
    def __init__(self, tipo_especialidad: str, dias: List[str]):
        self.__tipo__: str = tipo_especialidad
        # Convertir todos los días a minúsculas y eliminar duplicados manteniendo el orden
        self.__dias__: List[str] = []
        for dia in dias:
            dia_lower = dia.lower()
            if dia_lower not in self.__dias__:
                self.__dias__.append(dia_lower)
    
    def obtener_especialidad(self) -> str:
        return self.__tipo__
    
    def obtener_dias(self) -> List[str]:
        return self.__dias__
    
    def verificar_dia(self, dia: str) -> bool:
        if not self.__dias__:
            return False
        # Convertir el día a verificar a minúsculas para comparación case insensitive
        dia_lower = dia.lower()
        return dia_lower in self.__dias__
    
    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias__)
        return f"{self.__tipo__} (Días: {dias_str})"