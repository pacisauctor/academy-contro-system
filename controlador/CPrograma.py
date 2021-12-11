from helpers import load_data, save_data
from modelo.Programa import Programa


def gestionar(titulo:str):
    programas = load_data("database/programas.csv", "programa")
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
            Programa.mostrar_programas(programas)
        elif opcion == 2:
            programas.append(Programa.agregar_programa())
        elif opcion == 3:
            eleccion = int(input("Seleccione el programa a editar: "))
            Programa.editar_programa(programas[eleccion-1])
        elif opcion == 4:
            print("4")
        elif opcion == 5:
            print("Regresando...")
            save_data("database/programas.csv", programas)
            break
        else:
            print("Escoja una opción válida")