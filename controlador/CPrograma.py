from datetime import date

from controlador.CReglasNegocio import valida_duracion_programa
from modelo.Programa import Programa


def gestionar(titulo:str, programas:list, profesores:list):
    
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
            programas.append(prg)

        elif opcion == 2:
            for program in programas:
                print(program.__str__())
        elif opcion == 3:
            for program in programas:
                print(program.__str__())
            op = int(input('[?] Digita el id del programa: '))
            print('Proporciona los siguientes datos...')
            programas[(op-1)].nombre_programa = input('Nombre del Programa: ')
            programas[(op-1)].fecha_programa = date.today()
            programas[(op-1)].duracion_anios = valida_duracion_programa()
            programas[(op-1)].director = input('Director: ')

        elif opcion == 4:
            for program in programas:
                print(program.__str__())
            op = int(input('[?] Digita el id del programa: '))
            desicion = input('Desea establecer el estado del programa, como abierto? y/n: ').lower()
            if desicion == 'y':
                programas[(op - 1)].status_programa = 'Abierto'
        elif opcion == 5:
            for program in programas:
                print(program.__str__())
            op = int(input('[?] Digita el id del programa: '))
            programas.pop((op-1))
        elif opcion == 5:
            print("Regresando...")
            break
        else:
            print("Escoja una opción válida")