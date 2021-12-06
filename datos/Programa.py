
class Programa:
	def __init__(self, nombre_programa, fecha_programa, status_programa, director):
		self.nombre_programa = nombre_programa
		self.fecha_programa = fecha_programa
		self.status_programa = status_programa
		self.director = director

# metodos de propiedad del argumeto -> nombre_programa
                                
	@property
	def nombre_programa(self):
		return self.__nombre_programa
                                
	@nombre_programa.setter
	def nombre_programa(self, nombre_programa):
		self.__nombre_programa = nombre_programa
                                
	@nombre_programa.deleter
	def nombre_programa(self):
		del self.__nombre_programa
                                
# metodos de propiedad del argumeto -> fecha_programa
                                
	@property
	def fecha_programa(self):
		return self.__fecha_programa
                                
	@fecha_programa.setter
	def fecha_programa(self, fecha_programa):
		self.__fecha_programa = fecha_programa
                                
	@fecha_programa.deleter
	def fecha_programa(self):
		del self.__fecha_programa
                                
# metodos de propiedad del argumeto -> status_programa
                                
	@property
	def status_programa(self):
		return self.__status_programa
                                
	@status_programa.setter
	def status_programa(self, status_programa):
		self.__status_programa = status_programa
                                
	@status_programa.deleter
	def status_programa(self):
		del self.__status_programa
                                
# metodos de propiedad del argumeto -> director
                                
	@property
	def director(self):
		return self.__director
                                
	@director.setter
	def director(self, director):
		self.__director = director
                                
	@director.deleter
	def director(self):
		del self.__director
