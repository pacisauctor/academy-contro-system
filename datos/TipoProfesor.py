from . import Turno
class TipoProfesor:

    def __init__(self, tipo, turno:Turno) -> None:
        self.__tipo = tipo
        self.__turno = turno
        
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, value):
        self.__tipo = value
        
    @tipo.deleter
    def tipo(self):
        del self.__tipo
    
    

    def definit_tipo(self):
        pass
