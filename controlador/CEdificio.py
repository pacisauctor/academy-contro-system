from helpers import load_data, save_data
from modelo.Edificio import Edificio


def gestionar(titulo: str):
    edificios = load_data("database/edificios.csv", "edificio")
    while True:
        print(titulo.upper())
        print("Seleccione una opción")
        print("""
            1. Mostrar todas los edificios.
            2. Ingresar un nuevo registro de edificio.
            3. Editar un registro existente de edificio.
            4. Eliminar un registro de edificio.
            5. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue
        if opcion == 1:
            Edificio.listar_edificio(edificios)
        elif opcion == 2:
            Edificio.append(Edificio.agregar_edificio())
        elif opcion == 3:
            eleccion = int(input("Ingrese el ID del edificio: "))
            Edificio.editar_edificio(edificios[eleccion - 1])
        elif opcion == 4:
            eleccion = int(input("Ingrese el ID del estudiante: "))
            edificios.pop(eleccion -1)
        elif opcion == 5:
            save_data("database/edificios.csv", edificios)
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")
