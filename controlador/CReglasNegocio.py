from controlador.Editar_CReglasNegocio import reglas_de_negocio, editar_min_max_curso_programa, editar_minmax_asigna_xdocente, editar_minmax_asigna_xrecibir_estu, editar_minmax_estudiante_aper_programa

# 1 Un programa tiene un minimo y un maximo de cursos o asignaturas.
def valida_maxmin_curso_program(cant_curso):
    while True:
        cat_progr_curso = cant_curso
        if cat_progr_curso < int(reglas_de_negocio["min_cursos_por_programa"])  or cat_progr_curso > int(reglas_de_negocio["max_cursos_por_programa"]):
              print(f'No puede ecceder el numero de asignatura entre : {reglas_de_negocio["min_cursos_por_programa"]} <--y--> {reglas_de_negocio["max_cursos_por_programa"]}')
              return False
        else:
            return  True


# 2 Tanto un estudiante como los profesores pueden recibir o impartir un numero 
# minimo y maximo de asignaturas (cursos) respectivamente.
class max_min_doc_est:
    def valida_maxmin_estudiante_asign(self):
        while True:
            cat_asig_estud = int(input('Digita la cantidad de asignatura : '))
            if cat_asig_estud < int(reglas_de_negocio["min_cursos_estudiante"])  or cat_asig_estud > int(reglas_de_negocio["max_cursos_estudiante"]):
                print(f'No puede ecceder el numero de asignatura entre : {reglas_de_negocio["min_cursos_estudiante"]} <--y--> {reglas_de_negocio["max_cursos_estudiante"]}')
            else:
                return  cat_asig_estud

    def valida_maxmin_docente_asign(self):
        while True:
            print("Hi docente..:")
            cat_asig_docen = int(input('Digita la cantidad de asignatura : '))
            if cat_asig_docen < int(reglas_de_negocio["min_cursos_docente"])  or cat_asig_docen > int(reglas_de_negocio["max_cursos_docente"]):
                print(f'No puede ecceder el numero de asignatura asignadas entre : {reglas_de_negocio["min_cursos_docente"]} <--y--> {reglas_de_negocio["max_cursos_docente"]}')
            else:
                return  cat_asig_docen

# 3 Respecto a la matricula existe como regla de negocio un minimo y maximo de 
# estudiantes para poder aperturar un programa de estudios, así como los cursos
# de la carrera
def valida_maxmin_estud_programa(cant_matriculas) -> bool:
    while True:
        if cant_matriculas < reglas_de_negocio["min_estud_programa"]  or cant_matriculas > reglas_de_negocio["max_estud_programa"]:
            print(f'La duracion de la carrera no puede ser menor a {reglas_de_negocio["min_estud_programa"]}\
                    o mayor a {reglas_de_negocio["max_estud_programa"]} años')
            return False
        else:
            return  True


# 4 Si el programa de estudios es de cinco años se le aplica un 10% de descuento por 
#curso matriculado respecto al precio de lista, y si es de cuatro años se le aplica un 
#%5 (Importante mencionar que no existen programas de menor duración).
def valida_duracion_programa():
    while True:
        anios = int(input('Duracion de la Carrera : '))
        if anios < int(reglas_de_negocio["min_estud_curso"])  or anios > int(reglas_de_negocio["max_estud_curso"]):

            print(f'La duracion de la carrera no puede ser menor a {reglas_de_negocio["min_estud_curso"]} o mayor a {reglas_de_negocio["max_estud_curso"]} años')
        else:
            if anios == 5:
                anios = 5
            elif anios == 4:
                anios = 4

            return  anios

# 5 Si las calificaciones del estudiante por cada curso matriculado son mayores o 
# iguales a 90/100, se les otorga un descuento adicional del 10%, que se gestiona 
# como bono para las materias futuras a matricular

def descuentor_por_notas():
    while True:
        resul_notas = int(input('Agregar Notas : '))
        if resul_notas >= int(reglas_de_negocio["min_notas"]) and resul_notas <= int(reglas_de_negocio["max_notas"]):
             
          print("Descuento de 10 % adicional para su proximo curso")
        else: 
            print("Agregar sin descuentos")
            
        return  resul_notas
             
