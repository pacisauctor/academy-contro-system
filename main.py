from controlador.CAula import gestionar as gestionar_aulas
from controlador.CCurso import gestionar as gestionar_cursos
from controlador.CEdificio import gestionar as gestionar_edificios
from controlador.CMatricula import gestionar as gestionar_matriculas
from controlador.CProfesor import gestionar as gestionar_profesores
from controlador.CPrograma import gestionar as gestionar_programas
from controlador.CTipoProfesor import gestionar as gestionar_tipoProfesor
from controlador.CTurno import gestionar as gestionar_turnos
from controlador.CEstudiante import gestionar as gestionar_estudiantes

aulas = []
cursos = []
edificios = []
matriculas = []
profesores = []
programas = []
tiposProfesor = []
turnos = []
estudiantes = []

reglas_de_negocio={
    "min_cursos_por_programa": 4,
    "max_cursos_por_programa": 6,
    "min_cursos_docente": 1,
    "max_cursos_docente": 5,
    "min_cursos_estudiante": 1,
    "max_cursos_estudiante": 5,
    "min_estud_programa":3,
    "max_estud_programa":15,
    "min_estud_curso":3,
    "max_estud_curso":10,
}


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
            3. Salir
            """)
        try:
            opcion = int(input("-> "))
        except ValueError as ex:
            print(ex)
            print("Intente otra vez .")
            pass
        if opcion == 1:
            gestionar_profesores("Gestionar profesores", profesores)
        elif opcion == 2:
            gestionar_estudiantes("Gestionar estudiantes", estudiantes, matriculas)
        elif opcion == 3:
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
            gestionar_aulas("Gestionar aulas", aulas)
        elif opcion == 2:
            gestionar_edificios("Gestionar edficicio", edificios)
        elif opcion == 3:
            gestionar_programas("Gestionar programas", programas)
        elif opcion == 4:
            # TODO
            gestionar_cursos("Gestionar cursos", cursos)
        elif opcion == 5:
            gestionar_turnos("Gestionar turnos", turnos)
        elif opcion == 6:
            gestionar_tipoProfesor("Gestionar tipo de profesor", tiposProfesor)
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
            2. Agregar y ver matrículas
            3. Salir
            """)
        try:
            opcion = int(input("-> "))
        except ValueError as ex:
            print(ex)
            print("Intente otra vez .")
            pass
        if opcion == 1:
            print("Opción 1: TODO\n")
        elif opcion == 2:
            print("Opción 2: TODO\n")
        elif opcion == 3:
            print("Saliendo...")
            return
        else:
            print("Seleccione una opción válida.")


if __name__ == "__main__":
    main()

            
