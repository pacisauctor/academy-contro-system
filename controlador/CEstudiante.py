from modelo.Estudiante import Estudiante

def gestionar(titulo:str):
    estudiantes = []
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
        # mostrar los registros
        if opcion == 1:
            print("Mostrando todos los registros")
            Estudiante.listar_estudiantes(estudiantes)
        elif opcion == 2:
            estudiantes.append(Estudiante.agregar_estudiantes())
            print("Estudiante agregado")
        elif opcion == 3:
            indice = int(input("Id del estudiante:"))
            estudiantes[indice] = Estudiante.editar_estudiantes(estudiantes[indice])
            
        elif opcion == 4:
            indice = int(input("Id del estudiante:"))
            estudiantes.pop(indice)
            print("Estudiante eliminado")
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")