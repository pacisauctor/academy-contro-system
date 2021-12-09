class TipoProfesor:
    __cont_tipo_profesor= 0
    def __init__(self, tipo, obj_profesor):
        TipoProfesor.__cont_tipo_profesor += 1
        self.tipo = tipo
        self.obj_profesor = obj_profesor
        self.id_tipo_profesor = TipoProfesor.__cont_tipo_profesor

# metodos de propiedad del argumeto -> tipo
                                
    @property
    def tipo(self):
        return self.__tipo
                                
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
                                
    @tipo.deleter
    def tipo(self):
        del self.__tipo	
        
    def define_tipo(self):
        pass
