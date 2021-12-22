from controlador.CReglasNegocio import valida_max_curso_program
from modelo.Aula import Aula
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
            6. Cerrar un curso
            7. Aperturar un curso
            8. Regresar al menú principal
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

            if Aula.obtener_cant_registro_aulas() > 0:
                desc = input('[?] Desea agregar un aula al curso (y/n): ').lower()
                if desc == 'y':
                    aul = Aula.obtener_aula()
                    cur.add_aula(aul)

            if Programa.obtener_cant_registros_programas() > 0:
                desc = input('[?] Desea agregar el curso a un programa (y/n): ').lower()
                if desc == 'y':
                    prog = Programa.obtener_programa()
                    can_curso = prog.cant_curso
                    if not (valida_max_curso_program(can_curso)):
                        print('Error. No se pueden agregar mas cursos al programa...')
                    else:
                        cur.add_programa(prog)

            Curso.add_registro_curso(cur)
            print('Curso agregado exitosamente!!!\nPresione Enter para continuar')
            input()

        elif opcion == 3:

            curs = Curso.obtener_curso(True)
            if curs == 0:
                print('No existen registros de cursos')
            else:
                curs.editar_registro_curso()
                if Aula.obtener_cant_registro_aulas() > 0:
                    op = input('[?] Desea agregar un aula (y/n): ').lower()
                    if op == 'y':
                        aula_agregar = Aula.obtener_aula()
                        curs.add_aula(aula_agregar)
                if Programa.obtener_cant_registros_programas() > 0:
                    op = input('[?] Desea agregar un programa (y/n): ').lower()
                    if op == 'y':
                        pro_agregar = Programa.obtener_programa()
                        can_curso = pro_agregar.cant_curso
                        if not (valida_max_curso_program(can_curso)):
                            print('Error. No se pueden agregar mas cursos al programa...')
                        else:
                            curs.add_programa(pro_agregar)
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
            cur = Curso.obtener_curso(True)
            if cur == 0:
                print('Error. No existen registros de cursos')
            else:
                cur.estado = 'Cerrado'
        elif opcion == 7:
            cur = Curso.obtener_curso(True)
            if cur == 0:
                print('Error. No existen registros de cursos')
            else:
                cur.estado = 'Abierto'
        elif opcion == 8:
            print("Regresando...")
            break

        else:
            print("Escoja una opción válida")
