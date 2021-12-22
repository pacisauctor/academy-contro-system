from controlador.Editar_CReglasNegocio import reglas_de_negocio


# 1 Un programa tiene un minimo y un maximo de cursos o asignaturas.
def valida_max_curso_program(cant_curso):
    while True:
        cat_progr_curso = cant_curso
        if (cat_progr_curso > reglas_de_negocio["max_cursos_por_programa"]):
            print(f'No puede ecceder el numero de asignatura : {reglas_de_negocio["max_cursos_por_programa"]}')
            return False
        else:
            return True

def valida_min_curso_program(cant_curso):
    while True:
        cat_progr_curso = cant_curso
        if (cat_progr_curso < reglas_de_negocio["min_cursos_por_programa"]):

            print(f'El programa tiene un minimo de : {reglas_de_negocio["max_cursos_por_programa"]} '
                  f'cursos los cuales no cumple')
            return False
        else:
            return True


# 2 Tanto un estudiante como los profesores pueden recibir o impartir un numero 
# minimo y maximo de asignaturas (cursos) respectivamente.

def valida_min_estudiante_asign(cant_asignaturas):
    while True:
        cat_asig_estud = cant_asignaturas
        if (cat_asig_estud < reglas_de_negocio["min_cursos_estudiante"]):

            print(f'No se cumple con el minimo de asignaturas: {reglas_de_negocio["min_cursos_estudiante"]}')
            return False
        else:
            return True


def valida_max_estudiante_asign(cant_asignaturas):
    while True:
        cat_asig_estud = cant_asignaturas
        if (cat_asig_estud > reglas_de_negocio["max_cursos_estudiante"]):

            print(f'No puede ecceder el numero {reglas_de_negocio["max_cursos_estudiante"]} de asignatura')
            return False
        else:
            return True


def valida_min_docente_asign(cant_asignaturas):
    while True:
        cat_asig_docen = cant_asignaturas

        if (cat_asig_docen < reglas_de_negocio["min_cursos_docente"]):

            print(f'No se cumple el minimo de cursos :{reglas_de_negocio["min_cursos_docente"]}')
            return False
        else:
            return True


def valida_max_docente_asign(cant_asignaturas):
    while True:
        cat_asig_docen = cant_asignaturas

        if (cat_asig_docen > reglas_de_negocio["max_cursos_docente"]):

            print(f'No puede ecceder el numero {reglas_de_negocio["max_cursos_docente"]} de asignatura asignadas')
            return False
        else:
            return True

# 3 Respecto a la matricula existe como regla de negocio un minimo y maximo de 
# estudiantes para poder aperturar un programa de estudios, así como los cursos
# de la carrera

def valida_maxmin_estud_programa(cant_matriculas) -> bool:
    while True:
        if (cant_matriculas < reglas_de_negocio["min_estud_programa"]
                or cant_matriculas > reglas_de_negocio["max_estud_programa"]):

            print(f'Para aperturar un Programa debes cumplir el minimo de {reglas_de_negocio["min_estud_programa"]}'
                  f'estudiantes matriculados y no exceder el maximo de {reglas_de_negocio["max_estud_programa"]}')
            return False
        else:
            return True


def valida_maxmin_estud_curso(cant_matriculas) -> bool:
    while True:
        if (cant_matriculas < reglas_de_negocio["min_estud_curso"]
                or cant_matriculas > reglas_de_negocio["max_estud_curso"]):

            print(f'Para aperturar un Curso debes cumplir el minimo de {reglas_de_negocio["min_estud_programa"]}\
                    estudiantes matriculados y no exceder el maximo de {reglas_de_negocio["max_estud_curso"]}')
            return False
        else:
            return True


# 4 Si el programa de estudios es de cinco años se le aplica un 10% de descuento por 
# curso matriculado respecto al precio de lista, y si es de cuatro años se le aplica un
# %5 (Importante mencionar que no existen programas de menor duración).
def valida_duracion_programa():
    while True:
        anios = int(input('Duracion de la Carrera : '))
        if (anios < int(reglas_de_negocio["min_estud_curso"])
                or anios > int(reglas_de_negocio["max_estud_curso"])):

            print(f'La duracion de la carrera no puede ser menor a {reglas_de_negocio["min_estud_curso"]}'
                  f' o mayor a {reglas_de_negocio["max_estud_curso"]} años')
        else:
            if anios == 5:
                anios = 5
            elif anios == 4:
                anios = 4

            return anios


# 5 Si las calificaciones del estudiante por cada curso matriculado son mayores o 
# iguales a 90/100, se les otorga un descuento adicional del 10%, que se gestiona 
# como bono para las materias futuras a matricular

def descuentor_por_notas():
    while True:
        resul_notas = int(input('Agregar Notas : '))
        if int(reglas_de_negocio["min_notas"]) <= resul_notas <= int(reglas_de_negocio["max_notas"]):
            print("Descuento de 10 % adicional para su proximo curso")
        else: 
            print("Agregar sin descuentos")
            
        return resul_notas
