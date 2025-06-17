from typing import List
from src.especialidad import Especialidad

class Medico:

    def __init__(self, matricula_medico :str , nombre_medico :str , especialidad :List[Especialidad] = None):
        self.__matricula__  = matricula_medico
        self.__medico__  = nombre_medico
        self.__especialidad__ = especialidad if especialidad else []
        
    def agregar_especialidad(self, especialidad : Especialidad):
        self.__especialidad__.append(especialidad)
        
    def obtener_matricula(self) -> str:
        return self.__matricula__
        
    def obtener_especialidad_para_dia(self, dia: str) -> List[str]:
        if not dia or dia.strip() == "":
            return []
        especialidades_encontradas = []
        dias_lista = [d.strip() for d in dia.split(",")]
        for dia_individual in dias_lista:
            for especialidad in self.__especialidad__:
                if especialidad.verificar_dia(dia_individual):
                        esp_name = especialidad.obtener_especialidad()
                        if esp_name not in especialidades_encontradas:
                            especialidades_encontradas.append(esp_name)
        else:
            # Día único
            for especialidad in self.__especialidad__:
                if especialidad.verificar_dia(dia):
                    esp_name = especialidad.obtener_especialidad()
                    if esp_name not in especialidades_encontradas:
                        especialidades_encontradas.append(esp_name)
        
        return especialidades_encontradas
     
    def __str__(self) -> str:
            especialidades_str = ",\n".join([str(esp) for esp in self.__especialidad__])
            return f"{self.__medico__}, {self.__matricula__}, [{especialidades_str}]"