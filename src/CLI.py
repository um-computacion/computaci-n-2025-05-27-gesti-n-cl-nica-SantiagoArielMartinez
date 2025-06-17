import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
from datetime import datetime


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresione ENTER para continuar...")

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n" + "="*40)
        print("   SISTEMA DE GESTIÓN DE CLÍNICA")
        print("="*40)
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agregar especialidad a médico")
        print("4) Agendar turno")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")
        print("="*40)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opc = input("Opción: ").strip()
            limpiar_pantalla()
            try:
                if opc == "1":
                    self.agregar_paciente()
                elif opc == "2":
                    self.agregar_medico()
                elif opc == "3":
                    self.agregar_especialidad()
                elif opc == "4":
                    self.agendar_turno()
                elif opc == "5":
                    self.emitir_receta()
                elif opc == "6":
                    self.ver_historia()
                elif opc == "7":
                    self.ver_turnos()
                elif opc == "8":
                    self.ver_pacientes()
                elif opc == "9":
                    self.ver_medicos()
                elif opc == "0":
                    print("¡Hasta luego! Muchas gracias por usar el sistema.")
                    break
                else:
                    print("Opción inválida.")
            except (ValueError,
                    PacienteNoEncontradoException,
                    MedicoNoDisponibleException,
                    TurnoOcupadoException,
                    RecetaInvalidaException) as e:
                print(f"Error: {e}")
            pausar()

    def agregar_paciente(self):
        dni = input("DNI: ").strip()
        nombre = input("Nombre: ").strip()
        fn = input("Fecha nacimiento (dd/mm/aaaa): ").strip()

        try:
            fecha_nac = datetime.strptime(fn, "%d/%m/%Y")
        except ValueError:
            return print("Formato de fecha inválido. Usá el formato dd/mm/aaaa.")

        p = Paciente(dni, nombre, fecha_nac)
        self.clinica.agregar_paciente(p)
        print("Paciente registrado.")

    def agregar_medico(self):
        mat = input("Matrícula: ").strip()
        nombre = input("Nombre: ").strip()
        m = Medico(mat, nombre)
        self.clinica.agregar_medico(m)
        print("Médico agregado.")

    def agregar_especialidad(self):
        mat = input("Matrícula del médico: ").strip()
        medico = self.clinica.obtener_medico_por_matricula(mat)
        tipo = input("Tipo de especialidad: ").strip()
        dias = [d.strip() for d in input("Días (separados por coma): ").split(",")]
        esp = Especialidad(tipo, dias)
        medico.agregar_especialidad(esp)
        print("Especialidad agregada.")
        

    def agendar_turno(self):
        dni = input("DNI paciente: ").strip()
        mat = input("Matrícula médico: ").strip()
        fecha = input("Fecha (dd/mm/aaaa): ").strip()
        hora = input("Hora (HH:MM): ").strip()

        try:
            dt = datetime.strptime(f"{fecha} {hora}", "%d/%m/%Y %H:%M")
        except ValueError:
            print("Fecha u hora inválida. Usá el formato dd/mm/aaaa y HH:MM.")
            return
        esp = input("Especialidad: ").strip()
        self.clinica.agendar_turno(dni, mat, esp,dt)
        print("Turno agendado.")

    def emitir_receta(self):
        dni = input("DNI paciente: ").strip()
        mat = input("Matrícula médico: ").strip()
        meds = [m.strip() for m in input("Medicamentos (separados por coma): ").split(",") if m.strip()]
        self.clinica.emitir_receta(dni, mat, meds)
        print("Receta emitida.")

    def ver_historia(self):
        dni = input("DNI paciente: ").strip()
        historia = self.clinica.obtener_historiales_por_dni(dni)
        print(historia)

    def ver_turnos(self):
        turnos = self.clinica.obtener_turnos()
        if not turnos:
            print("No hay turnos agendados.")
        else:
            for t in turnos:
                print(t)

    def ver_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        if not pacientes:
            print("No hay pacientes registrados.")
        else:
            for p in pacientes:
                print(p)

    def ver_medicos(self):
        medicos = self.clinica.obtener_medicos()
        if not medicos:
            print("No hay médicos registrados.")
        else:
            for m in medicos:
                print(m)

if __name__ == "__main__":
    CLI().ejecutar()