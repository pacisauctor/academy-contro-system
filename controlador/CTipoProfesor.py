from modelo.Profesor import Profesor
from modelo.TipoProfesor import TipoProfesor


def gestionar(titulo: str):
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
            TipoProfesor.listar_registros()
        elif opcion == 2:
            TipoProfesor.agregar_registro()
            print('Elemento agregado exitosamente!!!')
        elif opcion == 3:
            TipoProfesor.editar_registro()
            print('Elemento editado exitosamente!!!')
        elif opcion == 4:
            TipoProfesor.eliminar_registro()
            print('El tipo de profesor se a eliminado exitosamente!!!')
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")
