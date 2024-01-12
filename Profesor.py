from Persona import Persona
from Escuela import Escuela

class Profesor(Persona):
    def __init__(self, nombre="", apellidos="", DNI="", escuela=None, asignatura=""):
        super().__init__(nombre, apellidos, DNI)
        self.escuela = escuela
        self.asignatura = asignatura

    def mostrarInformacion(self):
        print('INFORMACIÓN DEL PROFESOR')
        print('*************************')
        print(f'Nombre: {self.nombre}')
        print(f'Apellidos: {self.apellidos}')
        print(f'DNI: {self.DNI}')
        print(f'Escuela: {self.escuela.nombre if self.escuela else ""}')
        print(f'Asignatura: {self.asignatura}')


