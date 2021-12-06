
class Turno:
	def __init__(self, turno, obj_tipo_profesor):
		self.turno = turno
		self.obj_tipo_profesor = obj_tipo_profesor

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
		

# **************************************************
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
