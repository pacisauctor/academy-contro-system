from controlador import CReglasNegocio
from modelo.Curso import Curso
from modelo.Programa import Programa


def gestionar(titulo: str):
    while True:
        print(titulo.upper())
        print("Seleccione una opción")
        print("""
            1. Mostrar todas los registros.
            2. Ingresar un nuevo registro
            3. Editar un registro existente.
            4. Eliminar un registro
            5. Ver Cursos de un Programa
            6. Regresar al menú principal
            """)
        try:
            opcion = int(input("-->"))
        except ValueError as exc:
            print(exc)
            print("Escoja una opción válida")
            continue

        if opcion == 1:
            Curso.listar_registros_cursos()
            print('Preciona enter para continuar...')
            input()

        elif opcion == 2:
            cur = Curso()
            cur.nombre_curso = input('Proporciona el nombre del curso: ')
            cur.creditos = int(input('Proporciona la cantidad de creditos del curso: '))
            cur.cant_hrs_semanales = float(input('Proporciona la cantidad de horas semanales: '))
            cur.precio = float(input('Proporciona el precio del curso: '))
            desc = input('[?] Desea agregar un aula al curso (y/n): ').lower()
            if desc == 'y':
                aul = Aula.obtener_aula()
                cur.add_aula(aul)

            desc = input('[?] Desea agregar el curso a un programa (y/n): ').lower()
            if desc == 'y':
                prog = Programa.obtener_programa()
                can_curso = prog.cant_curso
                if not (CReglasNegocio.valida_maxmin_curso_program(can_curso)):
                    print('Error. No se pueden agregar mas cursos al programa...')
                else:
                    cur.add_programa(prog)

            Curso.add_registro_curso(cur)
            print('Curso agregado exitosamente!!!\nPresione Enter para continuar')
            input()

        elif opcion == 3:
            Curso.editar_registro_curso()
            print('Curso editado exitosamente!!!')
            input()
        elif opcion == 4:
            Curso.eliminar_registro_curso()
            print('Curso eliminado exitosamente!!!')
            input()
        elif opcion == 5:
            prg = Programa.obtener_programa()
            Curso.listar_curso_en_programa(prg)
        elif opcion == 6:
            print("Regresando...")
            break

        else:
            print("Escoja una opción válida")
