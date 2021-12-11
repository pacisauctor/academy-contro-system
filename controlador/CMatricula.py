from modelo.Matricula import Matricula
from helpers import load_data, save_data

def gestionar(titulo:str):
    matriculas = load_data("database/matriculas.csv", "matricula")
    while True:
        
        print(titulo.upper())
        print("Seleccione una opción")
        print("""
            1. Mostrar todas los registros de matricula.
            2. Ingresar un nuevo registro de matricula.
            3. Editar un registro existente de matricula.
            4. Eliminar un registro de matricula.
            5. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue
        if opcion == 1:
            Matricula.listar_matricula(matriculas)
        elif opcion == 2:
            Matricula.append(Matricula.agregar_matricula())
        elif opcion == 3:
            eleccion = int(input("Ingrese el ID de matricula: "))
            Matricula.editar_matricula(matriculas[eleccion - 1])
        elif opcion == 4:
            eleccion = int(input("Ingrese el ID de matricula: "))
            matriculas.pop(eleccion -1)
        elif opcion == 5:
            save_data("database/matriculas.csv", matriculas)
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")