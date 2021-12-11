from modelo.Programa import Programa


def gestionar(titulo:str, programas:list):
    
    while True:
        
        print(titulo.upper())
        print("Seleccione una opción")
        print("""
            1. Ingresar un nuevo registro
            2. Mostrar todas los registros.
            3. Editar un registro existente.
            4. Aperturar programa.
            5. Eliminar un registro
            6. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue
        if opcion == 1:
            programas.append(Programa.agregar_programa())
        elif opcion == 2:
            Programa.mostrar_programas(programas)
        elif opcion == 3:
            eleccion = int(input("Seleccione el programa a editar: "))
            Programa.editar_programa(programas[eleccion-1])
        elif opcion == 4:
            print("4 todo")
        elif opcion == 5:
            print("5 todo")
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")