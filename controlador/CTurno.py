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
            5. Ver Detalle
            6. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue
        if opcion == 1:
            print("ID  | Nombre")
            for turno in turnos:
                print(f"{turno.id_turno}: {turno.turno}")
        elif opcion == 2:
            turno = input("Digita el turno a agregar: ")
            trn = Turno(turno)
            trn.agrega_turno()
            seguir = True
            while(seguir):
                print("ID  | Nombre")
                for i in range(len(tiposProfesor)):
                    print(f"{i} | {tiposProfesor[i].tipo}")
                eleccion = int(input("Esriba el ID del Tipo de Profesor a agregar en el turno(-1 para salir):\n"))
                if eleccion == -1:
                   seguir = False 
                else:
                    trn.agregar_tipoProfesor(tiposProfesor[eleccion])
            turnos.append(trn)
            print("Elemento añadido correctamente")
            
        elif opcion == 3:
            print("ID  | Nombre")
            for turno in turnos:
                print(f"{turno.id_turno}: {turno.turno}")
            op = int(input('[?] Digita tu opcion: '))
            turno_value = input("Nuevo valor: ")
            turnos[op].turno = turno_value
            print('Turno editado exitosamente!!!')
        elif opcion == 4:
            print("ID  | Nombre")
            for i in len(turnos):
                print(f"{i}: {turnos[i].turno}")
            op = int(input('[?] Digita tu opcion: '))
            turnos.pop(op)
            print('La eliminacion se realizo con exito!!!')
        elif opcion == 5:
            print("ID  | Nombre | TiposProfesor")
            for turno in turnos:
                print(f"{turno.id_turno}: {turno.turno}  |", end="")
                for tipo in turno.tipoProfesores:
                    print(f"{tipo.tipo} |", end="")
                print()  
        elif opcion == 6:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")