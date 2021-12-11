from modelo.Turno import Turno


def gestionar(titulo: str, turnos:list, tiposProfesor:list):
    
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
            print(Turno.listar_turno())
        elif opcion == 2:
            turno = input("Digita el turno a agregar: [horaInicio-horaFin]-> ")
            trn = Turno(turno)
            trn.agrega_turno()
        elif opcion == 3:
            print(Turno.listar_turno())
            op = input('[?] Digita tu opcion: ')
            turno = input('[?] Proporciona el Nuevo Horario [horaInicio-horaFin]-> ')
            Turno.edit_turnos(op, turno)
            print('Turno editado exitosamente!!!')
        elif opcion == 4:
            print(Turno.listar_turno())
            op = input('[?] Digita tu opcion: ')
            Turno.delete_turnos(op)
            print('La eliminacion se realizo con exito!!!')
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")