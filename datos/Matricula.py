
class Matricula:
	def __init__(self, fecha_matricula, hora_matricula, obj_curso):
		self.fecha_matricula = fecha_matricula
		self.hora_matricula = hora_matricula
		self.obj_curso = obj_curso

# metodos de propiedad del argumeto -> fecha_matricula
                                
	@property
	def fecha_matricula(self):
		return self.__fecha_matricula
                                
	@fecha_matricula.setter
	def fecha_matricula(self, fecha_matricula):
		self.__fecha_matricula = fecha_matricula
                                
	@fecha_matricula.deleter
	def fecha_matricula(self):
		del self.__fecha_matricula
                                
# metodos de propiedad del argumeto -> hora_matricula
                                
	@property
	def hora_matricula(self):
		return self.__hora_matricula
                                
	@hora_matricula.setter
	def hora_matricula(self, hora_matricula):
		self.__hora_matricula = hora_matricula
                                
	@hora_matricula.deleter
	def hora_matricula(self):
		del self.__hora_matricula
