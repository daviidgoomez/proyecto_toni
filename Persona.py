from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre="", apellidos="", DNI=""):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI

    @abstractmethod
    def mostrarInformacion(self):
        pass

    def __str__(self):
        return f'{self.nombre} {self.apellidos} ({self.DNI})'
