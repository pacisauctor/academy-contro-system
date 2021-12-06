
class Curso:
    
	def __init__(self, nombre_curso, creditos, cant_hrs_semanales, 
				 programa, obj_aula):
		self.nombre_curso = nombre_curso
		self.creditos = creditos
		self.cant_hrs_semanales = cant_hrs_semanales
		self.programa = programa
		self.obj_aula = obj_aula

# metodos de propiedad del argumeto -> nombre_curso
                                
	@property
	def nombre_curso(self):
		return self.__nombre_curso
                                
	@nombre_curso.setter
	def nombre_curso(self, nombre_curso):
		self.__nombre_curso = nombre_curso
                                
	@nombre_curso.deleter
	def nombre_curso(self):
		del self.__nombre_curso
                                
# metodos de propiedad del argumeto -> creditos
                                
	@property
	def creditos(self):
		return self.__creditos
                                
	@creditos.setter
	def creditos(self, creditos):
		self.__creditos = creditos
                                
	@creditos.deleter
	def creditos(self):
		del self.__creditos
                                
# metodos de propiedad del argumeto -> cant_hrs_semanales
                                
	@property
	def cant_hrs_semanales(self):
		return self.__cant_hrs_semanales
                                
	@cant_hrs_semanales.setter
	def cant_hrs_semanales(self, cant_hrs_semanales):
		self.__cant_hrs_semanales = cant_hrs_semanales
                                
	@cant_hrs_semanales.deleter
	def cant_hrs_semanales(self):
		del self.__cant_hrs_semanales
                                
# metodos de propiedad del argumeto -> programa
                                
	@property
	def programa(self):
		return self.__programa
                                
	@programa.setter
	def programa(self, programa):
		self.__programa = programa
                                
	@programa.deleter
	def programa(self):
		del self.__programa
