
class Escuela:
    # Constructor por defecto de la clase
    def __init__(self, nombre="IES El Grao", localidad="Valencia", responsable="Generalitat Valenciana", ubicacion="El Grao"):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.ubicacion = ubicacion

    # Método de instancia de la clase
    def mostrarEscuela(self):
        print('ESCUELA')
        print('*****************')
        print("Nombre:", self.nombre)
        print("Localidad:", self.localidad)
        print("Responsable:", self.responsable)
        print("Ubicación:", self.ubicacion)

# Crear una instancia de la clase con valores predeterminados
mi_escuela = Escuela()
