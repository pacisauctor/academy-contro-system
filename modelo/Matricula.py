from datetime import date, datetime, time
class Matricula:
    
    __cont_matricula = 0
    def __init__(self, fecha_matricula, hora_matricula, obj_curso):
        Matricula.__cont_matricula += 1
        self.fecha_matricula = fecha_matricula
        self.hora_matricula = hora_matricula
        self.obj_curso = obj_curso
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

    # endregion metodos -> fecha_matricula

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
    
    def convert_to_dictionary(self)->dict:
        return {
            "fecha_matricula": self.fecha_matricula,
            "hora_matricula": self.hora_matricula,
            "obj_curso": self.obj_curso,
        }
        
    @classmethod
    def get_from_dictionary(cls, dictionary:dict):
        return Matricula(
            fecha_matricula= dictionary.get("fecha_matricula"),
            hora_matricula= dictionary.get("hora_matricula"),
            obj_curso= dictionary.get("obj_curso")
        )

    

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
        id_matricula = input("Ingrese el id de matricula: ")

        matricula = Matricula(fecha_matricula=fecha_matricula, hora_matricula=hora_matricula, id_matricula=id_matricula, obj_curso=None)
        return matricula


    @classmethod
    def editar_matricula(cls, matricula):
        matricula.fecha_matricula = input("Ingrese la fecha de matricula: ")
        matricula.hora_matricula = input("Ingrese la hora de matricula: ")
        matricula.id_matricula = input("Ingrese el id de matricula: ")
        return matricula