from modelo.Profesor import Profesor
from modelo.TipoProfesor import TipoProfesor


def gestionar(titulo:str, tiposProfesor:list, profesores:list):
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
            print("ID | Nombre")
            for tipoProfesor in tiposProfesor:
                print(f"{tipoProfesor.id_tipo_profesor}: {tipoProfesor.tipo}")
                
        elif opcion == 2:
            tipo = input('Digita el tipo de profesor a agregar: ')
            TipoProfesor.agregar_tipo(tipo)
            tiposProfesor.append(TipoProfesor(tipo))
            print('Elemento agregado exitosamente!!!')
        elif opcion == 3:
            TipoProfesor.edit_tipo()
            print('Elemento agregado exitosamente!!!')
        elif opcion == 4:
            TipoProfesor.delete_tipo()
            print('El tipo de profesor se a eliminado exitosamente!!!')
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")