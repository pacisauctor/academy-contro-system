from modelo.Turno import Turno
from modelo.TipoProfesor import TipoProfesor

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
            Turno.mostrar_registros()
        elif opcion == 2:
            turno = input("Digita el turno a agregar: ")
            trn = Turno(turno)
            
            while True:
                option = input("¿Desea agregar un tipo de profesor en el turno?(Y/N)")
                if option.lower() == "y":
                    TipoProfesor.listar_registros()
                    id_tipo =  int(input("ID del tipo de profesor: "))
                    trn.agregar_tipoProfesor(TipoProfesor.obtener_registro(id_tipo))
                else:
                    break
            Turno.agregar_registro(trn)
                
            print("Elemento añadido correctamente")
            
        elif opcion == 3:
            Turno.edit_turnos()
            print('Turno editado exitosamente!!!')
        elif opcion == 4:
            Turno.delete_turno()
            print('La eliminacion se realizo con exito!!!')
        elif opcion == 5:
            Turno.ver_detalle()
        elif opcion == 6:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")