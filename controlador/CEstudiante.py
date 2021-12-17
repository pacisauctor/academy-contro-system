from modelo.Estudiante import Estudiante


def gestionar(titulo: str, estudiantes: list, matriculas: list):
    while True:
        print(titulo.upper())
        print("Seleccione una opción")
        print("""
            1. Mostrar todas los estudiantes.
            2. Ingresar un nuevo estudiante
            3. Editar un estudiante.
            4. Eliminar un estudiante
            5. Gestionar notas de un estudiante
            6. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue
        if opcion == 1:
            Estudiante.listar_estudiantes()

        elif opcion == 2:
            Estudiante.agregar_estudiantes()
        elif opcion == 3:
            Estudiante.editar_estudiantes()

        elif opcion == 4:
            Estudiante.eliminar_estudiante()
        elif opcion == 5:
            # TODO
            pass
        elif opcion == 6:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")
