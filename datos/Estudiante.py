from . import Persona
class Estudiante(Persona):

	def __init__(self, nombre, apellido, cedula, direccion, telefono, 
                 fecha_nac, email, id_estudiante, obj_matricula):

		super().__init__(nombre, apellido, cedula, direccion, 
                         telefono, fecha_nac, email)
		self.id_estudiante = id_estudiante
		self.obj_matricula = obj_matricula

# metodos de propiedad del argumeto -> id_estudiante
                                
	@property
	def id_estudiante(self):
		return self.__id_estudiante
                                
	@id_estudiante.setter
	def id_estudiante(self, id_estudiante):
		self.__id_estudiante = id_estudiante
                                
	@id_estudiante.deleter
	def id_estudiante(self):
		del self.__id_estudiante
