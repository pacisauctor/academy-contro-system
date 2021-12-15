from modelo.Aula import Aula
from modelo.Edificio import Edificio

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
            Aula.listar_aulas()
        elif opcion == 2:
            print("2")
            Aula.agregar_aula()
        elif opcion == 3:
            print("3")
            Aula.editar_aula()
        elif opcion == 4:
            print("4")
            Aula.eliminar_aula()
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")