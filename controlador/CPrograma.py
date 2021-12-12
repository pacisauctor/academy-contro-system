from datetime import date

from controlador.CReglasNegocio import valida_duracion_programa
from modelo.Programa import Programa


def gestionar(titulo:str):
    
    while True:
        
        print(titulo.upper())
        print("Seleccione una opción")
        print("""
            1. Ingresar un nuevo registro
            2. Mostrar todas los registros.
            3. Editar un registro existente.
            4. Aperturar programa.
            5. Eliminar un registro
            6. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue
        if opcion == 1:

            prg = Programa()
            print('Proporciona los siguientes datos...')
            prg.nombre_programa = input('Nombre del Programa: ')
            prg.fecha_programa = date.today()
            prg.duracion_anios = valida_duracion_programa()
            prg.director = input('Director: ')
            Programa.ingresar_registro(prg)
            print('Programa agregado correctamente...')
            print('Precione enter para continuar...')
            input()
        elif opcion == 2:

            Programa.listar_programas()
            print('Precione enter para continuar...')
            input()
        elif opcion == 3:

            Programa.listar_programas()
            Programa.editar_programa()
            print('Programa editado correctamente...')
            print('Precione enter para continuar...')
            input()
        elif opcion == 4:

            print('Por defecto los programas se encuentrar "Cerrados"')
            Programa.listar_programas()
            Programa.modificar_status_programa()
            print('Programa editado correctamente...')
            print('Precione enter para continuar...')
            input()
        elif opcion == 5:
            Programa.listar_programas()
            Programa.eliminar_programa()
            print('Programa eliminado correctamente...')
            print('Precione enter para continuar...')
            input()
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")