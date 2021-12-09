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
