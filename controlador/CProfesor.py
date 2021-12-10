from helpers import load_data, save_data
from modelo.Profesor import Profesor


def gestionar(titulo:str):
    profesores = load_data("database/profesores.csv", "profesor")
    while True:
        print(titulo.upper())
        print("Seleccione una opción")
        print("""
            1. Mostrar todas los registros.
            2. Ingresar un nuevo registro
            3. Editar un registro existente.
            4. Eliminar un registro
            5. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue
        if opcion == 1:
            Profesor.mostrar_profesores(profesores)
        elif opcion == 2:
            profesores.append(Profesor.crear_profesor())
        elif opcion == 3:
            eleccion = int(input("Seleccione el ID del profesor:"))
            Profesor.editar_profesor(profesores[eleccion-1])
        elif opcion == 4:
            eleccion = int(input("Seleccione el ID del profesor:"))
            profesores.pop(eleccion)
        elif opcion == 5:
            save_data("database/profesores.csv", profesores)
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")