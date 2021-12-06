from . import Persona

class Profesor(Persona):

    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nac, 
                 email, id_profesor, obj_programa, obj_curso) -> None:

        super().__init__(nombre, apellido, cedula, direccion, telefono, fecha_nac, email)  
        self.__id_profesor = id_profesor
        self.obj_programa = obj_programa
        self.obj_curso = obj_curso


    @property
    def id_profesor(self):
        return self.__id_profesor

    @id_profesor.setter
    def id_profesor(self, value):
        self.__id_profesor = value

    @id_profesor.deleter
    def id_profesor(self):
        del self.__id_profesor
    
    def crear_profesor(self):
        pass
