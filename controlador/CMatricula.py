from modelo.Matricula import Matricula

def gestionar(titulo:str, matriculas:list):
    
    while True:
        
        print(titulo.upper())
        print("Seleccione una opción")
        print("""
            1. Mostrar todas los registros de matricula.
            2. Ingresar un nuevo registro de matricula.
            3. Editar un registro existente de matricula.
            4. Eliminar un registro de matricula.
            5. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue
        if opcion == 1:
            Matricula.listar_matricula()
        elif opcion == 2:
            Matricula.agregar_matricula()
        elif opcion == 3:
            Matricula.editar_matricula()
        elif opcion == 4:
            Matricula.eliminar_matricula()
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")
            
