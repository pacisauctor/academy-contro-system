reglas_de_negocio = {
    "min_cursos_por_programa": 2,
    "max_cursos_por_programa": 6,
    "min_cursos_docente": 1,
    "max_cursos_docente": 5,
    "min_cursos_estudiante": 1,
    "max_cursos_estudiante": 5,
    "min_estud_programa":3,  
    "max_estud_programa":15, 
    "min_estud_curso":4,
    "max_estud_curso":5,
    "max_notas":100,
    "min_notas":90
        }
"""print()
print(reglas_de_negocio)
print()"""

            #1. Minimo y Maximo de curso de un Programa.
            #2. Maximo y Minimo de asignaturas a impartir por docente
            #3. Maximo y Minimo de asignaturas a recibir un Estudiante.
            #4. Matriculas, Maximo y Minimo de estudiante para aperturar el programa
            #5. Maximo y Minimo de años de duracion del programa del curso
            #6. Salir..

            
def editar_min_max_curso_programa():
    while True:
        try:
            max_edit_p = int(input('Digita el Maximo de curso de un programa : '))
            min_edit_p = int(input('Digita el Minimo de curso de un programa : '))

            if max_edit_p > min_edit_p:
                reglas_de_negocio["max_cursos_por_programa"] = max_edit_p
                reglas_de_negocio["min_cursos_por_programa"] = min_edit_p
                break

            else: 
                print("\nError el valor minimo es mas alto que el maximo verifica.\n")

        except ValueError as ex:
            print(ex)
            print("Error digita un valor valido")

def editar_minmax_asigna_xdocente():
    while True:
        try:
            max_edit_asiD = int(input('Digita el Maximo de asignatura a impartir por docente : '))
            min_edit_asiD = int(input('Digita el Minimo de asignatura a impartir por docente : '))

            if max_edit_asiD > min_edit_asiD:
                reglas_de_negocio["max_cursos_docente"] = max_edit_asiD
                reglas_de_negocio["min_cursos_docente"] = min_edit_asiD
                break

            else: 
                print("\nError el valor minimo es mas alto que el maximo verifica.\n")

        except ValueError as ex:
            print(ex)
            print("Error digita un valor valido")

def editar_minmax_asigna_xrecibir_estu():
    while True:
        try:
            max_edit_asiE = int(input('Digita el Maximo de asignatura a recibir por estudiante : '))
            min_edit_asiE = int(input('Digita el Minimo de asignatura a recibir por estudiante : '))

            if max_edit_asiE > min_edit_asiE:
                reglas_de_negocio["max_cursos_estudiante"] = max_edit_asiE
                reglas_de_negocio["min_cursos_estudiante"] = min_edit_asiE
                break

            else: 
                print("\nError el valor minimo es mas alto que el maximo verifica.\n")

        except ValueError as ex:
            print(ex)
            print("Error digita un valor valido")

def editar_minmax_estudiante_aper_programa():
    while True:
        try:
            max_edit_estpro = int(input('Digita el Maximo de estudiante para aperturar el programa : '))
            min_edit_estpro = int(input('Digita el Minimo de estudiante para aperturar el programa : '))

            if max_edit_estpro > min_edit_estpro:
                reglas_de_negocio["max_estud_programa"] = max_edit_estpro
                reglas_de_negocio["min_estud_programa"] = min_edit_estpro
                break

            else: 
                print("\nError el valor minimo es mas alto que el maximo verifica.\n")

        except ValueError as ex:
            print(ex)
            print("Error digita un valor valido")

def editar_minmax_anios_programa():
    while True:
        try:
            max_edit_anios = int(input('Digita el Maximo de Años del curso : '))
            min_edit_anios = int(input('Digita el Minimo de Años del curso : '))

            if max_edit_anios > min_edit_anios:
                reglas_de_negocio["max_estud_curso"] = max_edit_anios
                reglas_de_negocio["min_estud_curso"] = min_edit_anios
                break

            else: 
                print("\nError el valor minimo es mas alto que el maximo verifica.\n")

        except ValueError as ex:
            print(ex)
            print("Error digita un valor valido")

"""editar_minmax_anios_programa()

print()
print(reglas_de_negocio)
print()"""

