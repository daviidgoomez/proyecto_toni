from Persona import Persona
from Escuela import Escuela

class Alumno(Persona):
    def __init__(self, nombre="", apellidos="", DNI="", escuela=None, curso=""):
        super().__init__(nombre, apellidos, DNI)
        self.escuela = escuela
        self.curso = curso

    def mostrarInformacion(self):
        print('INFORMACIÓN DEL ALUMNO')
        print('************************')
        print(f'Nombre: {self.nombre}')
        print(f'Apellidos: {self.apellidos}')
        print(f'DNI: {self.DNI}')
        print(f'Escuela: {self.escuela.nombre if self.escuela else ""}')
        print(f'Curso: {self.curso}')