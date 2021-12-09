class Turno:
    __cont_turno= 0
    def __init__(self, turno, obj_tipo_profesor):
        Turno.__cont_turno += 1
        self.turno = turno
        self.obj_tipo_profesor = obj_tipo_profesor
        self.id_turno = Turno.__cont_turno

    # metodos de propiedad del argumeto -> turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @turno.deleter
    def turno(self):
        del self.__turno
