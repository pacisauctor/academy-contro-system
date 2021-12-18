from controlador.CAula import gestionar as gestionar_aulas
from controlador.CCurso import gestionar as gestionar_cursos
from controlador.CEdificio import gestionar as gestionar_edificios
from controlador.CMatricula import gestionar as gestionar_matriculas
from controlador.CReglasNegocio import * 
from controlador.CProfesor import gestionar as gestionar_profesores
from controlador.CPrograma import gestionar as gestionar_programas
from controlador.CTipoProfesor import gestionar as gestionar_tipoProfesor
from controlador.CTurno import gestionar as gestionar_turnos
from controlador.CEstudiante import gestionar as gestionar_estudiantes
from modelo.Estudiante import Estudiante


def main():
    while(True):
        print("-"*15)
        print("ACADEMICAL CONTROL SYSTEM")
        print("-"*15)
        print("Menu de opciones.")
        print("""
            1. Administración.
            2. Catalogos
            3. Matriculas.
            4. Salir
            """)
        try:
            opcion = int(input("-> "))
        except ValueError as ex:
            print(ex)
            print("Intente otra vez .")
            pass
        if opcion == 1:
            submenu_administracion()
        elif opcion == 2:
            submenu_catalogos()
        elif opcion == 3:
            submenu_matriculas()
        elif opcion == 4:
            print("Saliendo...")
            return
        else:
            print("Seleccione una opción válida.")
            

def submenu_administracion():
    while(True):
        print("Menu de opciones.")
        print("""
            1. Gestionar profesores.
            2. Gestionar estudiantes
            3. Editar reglas de negocio.
            4. Salir
            """)
        try:
            opcion = int(input("-> "))
        except ValueError as ex:
            print(ex)
            print("Intente otra vez .")
            pass
        if opcion == 1:
            gestionar_profesores("Gestionar profesores")
        elif opcion == 2:
            gestionar_estudiantes("Gestionar estudiantes")
        elif opcion == 3:
        
            while(True):
                print("-"*25)
                print("Editar Reglas de Negocio")
                print("-"*25)
                print("Menu de opciones.")
                print("""
                    1. Minimo y Maximo de curso de un Programa.
                    2. Maximo y Minimo de asignaturas a impartir por docente
                    3. Maximo y Minimo de asignaturas a recibir un Estudiante.
                    4. Matriculas, Maximo y Minimo de estudiante para aperturar el programa
                    5. Maximo y Minimo de años de duracion del programa del curso
                    6. Salir..
                    """)
                try:
                    opcion = int(input("-> "))
                except ValueError as ex:
                    print(ex)
                    print("Intente otra vez .")
                    pass
                if opcion == 1:
                    print("Minimo y Maximo de curso de un Programa")
                    editar_min_max_curso_programa()

                elif opcion == 2:
                    print("Maximo y Minimo de asignaturas a impartir por docente")
                    editar_minmax_asigna_xdocente()
                elif opcion == 3:
                    print("Maximo y Minimo de asignaturas a recibir un Estudiante")
                    editar_minmax_asigna_xrecibir_estu()
                elif opcion == 4:
                    print("Matriculas, Maximo y Minimo de estudiante para aperturar el programa")
                    editar_minmax_estudiante_aper_programa()
                elif opcion == 5:
                    print("Maximo y Minimo de años de duracion del programa del curso")
                    # editar_minmax_anios_programa()
                elif opcion == 6:
                    print("Saliendo...")
                    return
                else:
                    print("Seleccione una opción válida.")


        elif opcion == 4:
            print("Saliendo...")
            return
        else:
            print("Seleccione una opción válida.")


def submenu_catalogos():
    while(True):
        print("Menu de opciones.")
        print("""
            1. Gestionar aulas.
            2. Gestionar edificios
            3. Gestionar programas
            4. Gestionar cursos
            5. Gestionar turnos
            6. Gestionar tipo de profesor
            7. Salir
            """)
        try:
            opcion = int(input("-> "))
        except ValueError as ex:
            print(ex)
            print("Intente otra vez .")
            pass
        if opcion == 1:
            # TODO
            gestionar_aulas("Gestionar aulas")
        elif opcion == 2:
            gestionar_edificios("Gestionar edficicio")
        elif opcion == 3:
            gestionar_programas("Gestionar programas")
        elif opcion == 4:
            # TODO
            gestionar_cursos("Gestionar cursos")
        elif opcion == 5:
            gestionar_turnos("Gestionar turnos")
        elif opcion == 6:
            gestionar_tipoProfesor("Gestionar tipo de profesor")
        elif opcion == 7:
            print("Saliendo...")
            return
        else:
            print("Seleccione una opción válida.")


def submenu_matriculas():
    while(True):
        print("Menu de opciones.")
        print("""
            1. Agregar estudiantes.
            2. Agregar matrículas
            3. Salir
            """)
        try:
            opcion = int(input("-> "))
        except ValueError as ex:
            print(ex)
            print("Intente otra vez .")
            pass
        if opcion == 1:
            Estudiante.agregar_estudiantes()
        elif opcion == 2:
            Estudiante.matricular()
        elif opcion == 3:
            print("Saliendo...")
            return
        else:
            print("Seleccione una opción válida.")


if __name__ == "__main__":
    main()

            
