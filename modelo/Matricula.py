from datetime import date, datetime, time
from modelo.Estudiante import Estudiante
from modelo.Curso import Curso

class Matricula:
    
    __cont_matricula = 0
    def __init__(self, fecha_matricula, hora_matricula):
        Matricula.__cont_matricula += 1
        self.fecha_matricula = fecha_matricula
        self.hora_matricula = hora_matricula
        self.curso = None
        self.total_pagar = 0
        # nota = 0
        self.id_matricula = Matricula.__cont_matricula

    def __str__(self):
        txt = f'''
        Fecha de Matricula: {self.fecha_matricula}
        Hora: {self.hora_matricula}
        \nCurso: {self.obj_curso}
        '''
        return txt
    # region metodos de propiedad del argumeto -> fecha_matricula

    @property
    def fecha_matricula(self):
        return self.__fecha_matricula

    @fecha_matricula.setter
    def fecha_matricula(self, fecha_matricula):
        self.__fecha_matricula = fecha_matricula

    @fecha_matricula.deleter
    def fecha_matricula(self):
        del self.__fecha_matricula
        
    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso:Curso):
        self.__curso = curso

    @curso.deleter
    def curso(self):
        del self.__curso
        

    # endregion metodos -> fecha_matricula
    @property
    def total_pagar(self):
        return self.__total_pagar

    @total_pagar.setter
    def total_pagar(self, total_pagar):
        self.__total_pagar = total_pagar

    @total_pagar.deleter
    def total_pagar(self):
        del self.__total_pagar
    
    
  
    # region metodos de propiedad del argumeto -> hora_matricula

    @property
    def hora_matricula(self):
        return self.__hora_matricula

    @hora_matricula.setter
    def hora_matricula(self, hora_matricula):
        self.__hora_matricula = hora_matricula

    @hora_matricula.deleter
    def hora_matricula(self):
        del self.__hora_matricula
    # endregion metodos -> hora_matricula
    
   

    @classmethod
    def listar_matricula(cls, list_matricula):
        for i in range(len(list_matricula)):
            print(list_matricula[i])

    @classmethod
    def agregar_matricula(cls):
        fecha_matricula = date.today()
        print(time.strftime("EL dia es: %d / %m / %y"))
        hora_matricula = datetime.now()
        print(time.strftime(" La hora es: %H:%M:%S"))
        Estudiante.listar_estudiantes()

        matricula = Matricula(fecha_matricula=fecha_matricula, hora_matricula=hora_matricula)
        # listar estudiantes, y seleccionar el id del estudiante
        # est.agregar_matricula(matricula)
        # listar cursos, y selecciono el id del curso
        # matricula.obj_curso = curso_seleccionado
        # total_apagar = curso_seleccionado.precio <-- conforme a: años del programa y las notas del estudiante
        return matricula


    @classmethod
    def editar_matricula(cls, matricula):
        matricula.fecha_matricula = input("Ingrese la fecha de matricula: ")
        matricula.hora_matricula = input("Ingrese la hora de matricula: ")
        matricula.id_matricula = input("Ingrese el id de matricula: ")
        return matricula