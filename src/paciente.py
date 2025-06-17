class Paciente:

    def __init__(self, dni_paciente :str , nombre_paciente :str , fecha_nacimiento :str):
        self.__DNI__ = dni_paciente
        self.__paciente__ = nombre_paciente
        self.__nacimiento__ = fecha_nacimiento

    def obtener_dni(self):
        return self.__DNI__
    
    def __str__(self):
        return f'Paciente: {self.__paciente__}, DNI: {self.__DNI__}, Fecha de Nacimiento: {self.__nacimiento__}'