from modelo.Edificio import Edificio


def gestionar(titulo: str):
    
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
            Edificio.listar_edificio()
        elif opcion == 2:
            Edificio.agregar_edificio()
        elif opcion == 3:
            Edificio.editar_edificio()
        elif opcion == 4:
            Edificio.eliminar_edificio()
        elif opcion == 5:
            
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")
