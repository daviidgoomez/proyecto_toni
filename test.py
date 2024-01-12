
from Profesor import Profesor
from Alumno import Alumno
from Escuela import Escuela

class GestionEscuela:
    def __init__(self):
        self.escuela = Escuela()
        self.profesores = []
        self.alumnos = []

    def menuPrincipal(info):
        while True:
            print("\nMENÚ PRINCIPAL")
            print('*************')
            print("1. Gestión de Profesores")
            print("2. Gestión de Alumnos")
            print("3. Mostrar Información de la Escuela")
            print("4. SALIR")

            opcion = input("Selecciona una opción (1-4): ")

            if opcion == "1":
                info.menu_profesores()
            elif opcion == "2":
                info.menu_alumnos()
            elif opcion == "3":
                info.escuela.mostrarEscuela()
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. VUELVE A INTENTARLO")

    def menu_profesores(self):
        while True:
            print("\nMENÚ DE PROFESORES")
            print('*****************')
            print("1. Añadir Profesor")
            print("2. Modificar Profesor")
            print("3. Borrar Profesor")
            print("4. Mostrar Profesores")
            print("5. Volver al Menú Principal")

            opcion = input("Selecciona una opción (1-5): ")

            if opcion == "1":
                self.crear_profesor()
            elif opcion == "2":
                self.modificar_profesor()
            elif opcion == "3":
                self.borrar_profesor()
            elif opcion == "4":
                self.mostrar_profesores()
            elif opcion == "5":
                break
            else:
                print("Opción no válida. VUELVE A INTENTARLO.")

    def crear_profesor(self):
        print('REGISTRO DE NUEVO PROFESOR')
        print('*************************')
        nombre = input("Introduce el nombre del profesor: ")
        apellidos = input("Introduce los apellidos del profesor: ")
        DNI = input("Introduce el DNI del profesor: ")
        asignatura = input("Intrduce la asignatura que imparte el profesor: ")

        profesor = Profesor(nombre, apellidos, DNI, self.escuela, asignatura)
        self.profesores.append(profesor)
        print("Profesor añadido con éxito.")

    def modificar_profesor(self):
        if not self.profesores:
            print("No hay profesores para modificar.")
            return

        self.mostrar_profesores()
        indice = int(input("Introduce la posición del profesor a modificar (ASEGÚRATE DE NO PONER UNA LETRA): "))

        if 1 <= indice <= len(self.profesores):
            profesor = self.profesores[indice - 1]
            print("\nMODIFICAR PROFESORES")
            print("**********************")
            print("1. Modificar Asignatura")
            print("2. Volver al Menú de Profesores")
            opcion = input("Selecciona una opción (1-2): ")

            if opcion == "1":
                nueva_asignatura = input("Introduce la nueva asignatura que imparte el profesor: ")
                profesor.asignatura = nueva_asignatura
                print("Asignatura modificada con éxito.")
        else:
            print("Posición de profesor no válido. INTRODÚCELO DE NUEVO.")

    def borrar_profesor(self):
        if not self.profesores:
            print("No hay profesores para borrar.")
            return

        self.mostrar_profesores()
        indice = int(input("Introduce la posición del profesor a borrar: "))

        if 1 <= indice <= len(self.profesores):
            profesor_borrado = self.profesores.pop(indice - 1)
            print(f"Profesor '{profesor_borrado.nombre}' borrado con éxito.")
        else:
            print("Posición de profesor no válida. HAZLO DE NUEVO.")

    def mostrar_profesores(self):
        if not self.profesores:
            print("No hay profesores para mostrar.")
        else:
            print("\nLISTA DE PROFESORES")
            print("********************")
            for i, profesor in enumerate(self.profesores, start=1):
                print(f"{i}. {profesor.nombre} {profesor.apellidos} - Asignatura: {profesor.asignatura}")

    def menu_alumnos(self):
        while True:
            print("\nMENU DE ALUMNOS")
            print("******************")
            print("1. Añadir un Alumno")
            print("2. Modificar Alumno")
            print("3. Borrar Alumno")
            print("4. Mostrar Alumnos")
            print("5. Volver al Menú Principal")

            opcion = input("Introduce una opción (1-5): ")

            if opcion == "1":
                self.crear_alumno()
            elif opcion == "2":
                self.modificar_alumno()
            elif opcion == "3":
                self.borrar_alumno()
            elif opcion == "4":
                self.mostrar_alumnos()
            elif opcion == "5":
                break
            else:
                print("Opción no válida. VUELVE A INTENTARLO.")

    def crear_alumno(self):
        nombre = input("Introduce el nombre del alumno: ")
        apellidos = input("Introduce los apellidos del alumno: ")
        DNI = input("Introduce el DNI del alumno: ")
        curso = input("Introduce el curso del alumno: ")

        alumno = Alumno(nombre, apellidos, DNI, self.escuela, curso)
        self.alumnos.append(alumno)
        print("Alumno creado satisfactoriamente.")

    def modificar_alumno(self):
        if not self.alumnos:
            print("No hay alumnos para modificar.")
            return

        
        
        
        
    menuPrincipal()
    

