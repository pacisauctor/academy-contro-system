from datetime import date, datetime, time
from modelo.Estudiante import Estudiante
from modelo.Curso import Curso


class Matricula:

    __cont_matricula = 0
    __list_matricula = []

    def __init__(self, fecha_matricula, hora_matricula):
        Matricula.__cont_matricula += 1
        self.fecha_matricula = fecha_matricula
        self.hora_matricula = hora_matricula
        self.curso = None
        self.total_pagar = 0
        self.nota = 0
        self.id_matricula = Matricula.__cont_matricula

    def __str__(self):
        txt = f'''
        Id Matricula: {self.id_matricula}
        Fecha de Matricula: {self.fecha_matricula}
        Hora: {self.hora_matricula}
        Curso: {self.curso}
        Nota Obtenida: {self.nota}
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

    # endregion metodos de propiedad del argumeto -> fecha_matricula

    # region Metodos curso
    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso: Curso):
        self.__curso = curso

    @curso.deleter
    def curso(self):
        del self.__curso

    # endregion Metodos curso

    # region Metodos nota
    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota

    @nota.deleter
    def nota(self):
        del self.__nota

    # endregion Metodos nota

    # region metodos -> toal_pagar
    @property
    def total_pagar(self):
        return self.__total_pagar

    @total_pagar.setter
    def total_pagar(self, total_pagar):
        self.__total_pagar = total_pagar

    @total_pagar.deleter
    def total_pagar(self):
        del self.__total_pagar

    # endregion metodos -> toal_pagar

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

    # region Metodos de Clase
    @classmethod
    def listar_matricula(cls):
        for matricula in cls.__list_matricula:
            print(matricula.id_matricula, end="")
            print(matricula.fecha_matricula, end="")
            estudiante = Estudiante.obtener_estudiante_byMatricula(matricula)
            print(estudiante.num_carnet, end="")
            print(estudiante.nombre, end="")
            print(estudiante.apellido, end="")

    @classmethod
    def agregar_matricula(cls):
        fecha_matricula = date.today()
        print(time.strftime("EL dia es: %d / %m / %y"))
        hora_matricula = datetime.now()
        print(time.strftime(" La hora es: %H:%M:%S"))
        matricula = Matricula(fecha_matricula=fecha_matricula, hora_matricula=hora_matricula)
        Estudiante.addMatriculaToEstudiante(matricula)
        matricula.curso = Curso.obtener_curso()

        for programa in matricula.curso.lstprogramas:
            print(programa.nombre_programa, end="")
            print(programa.id_programa, end="")

        eleccion = int(input("Seleccione un id de programa"))

        if matricula.curso.lstprogramas[eleccion].duracion_anios == 5:
            matricula.total_pagar = (matricula.curso.precio * 0.9)
        else:
            matricula.total_pagar = (matricula.curso.precio * 0.95)

        cls.__list_matricula.append(matricula)

    @classmethod
    def editar_matricula(cls):
        cls.listar_matricula()
        eleccion = int(input("Elija el Id de la matricula"))
        cls.__list_matricula[eleccion - 1].fecha_matricula = input("Ingrese la fecha de matricula: ")
        cls.__list_matricula[eleccion - 1].hora_matricula = input("Ingrese la hora de matricula: ")

    @classmethod
    def eliminar_matricula(cls):
        cls.listar_matricula()
        eleccion = int(input("Elija el Id de la matricula"))
        cls.__list_matricula.pop(eleccion - 1)
    # endregion Metodos de Clase
