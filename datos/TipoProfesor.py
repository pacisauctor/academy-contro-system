class TipoProfesor:
    def __init__(self, tipo, obj_profesor):
        self.tipo = tipo
        self.obj_profesor = obj_profesor

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
