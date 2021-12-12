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
            for estudiante in estudiantes:
                print(f"{estudiante.num_carnet}: {estudiante.nombre} {estudiante.apellido} ")

        elif opcion == 2:
            numero_carnet = input("Ingrese el numero de carnet del estudiante: ")
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            cedula = input("Ingrese el cedula del estudiante: ")
            direccion = input("Ingrese el direccion del estudiante: ")
            telefono = input("Ingrese el telefono del estudiante: ")
            fecha_nac = input("Ingrese la fecha de nacimiento del estudiante: ")
            email = input("Ingrese el email del estudiante: ")
            est = Estudiante(nombre,apellido,cedula,direccion,telefono,fecha_nac,email,numero_carnet,None)

            estudiantes.append(est)
        elif opcion == 3:
            eleccion = int(input("Ingrese el ID del estudiante: "))
            Estudiante.editar_estudiantes(estudiantes[eleccion - 1])
        elif opcion == 4:
            eleccion = int(input("Ingrese el ID del estudiante: "))
            estudiantes.pop(eleccion - 1)
        elif opcion == 5:
            # TODO
            pass
        elif opcion == 6:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")
