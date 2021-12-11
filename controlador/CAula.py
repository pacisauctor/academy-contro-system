def gestionar(titulo: str, aulas:list, edificios:list):
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
            print("1")
        elif opcion == 2:
            print("2")
        elif opcion == 3:
            print("3")
        elif opcion == 4:
            print("4")
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")