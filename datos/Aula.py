
class Aula:
	
	def __init__(self, nombre_aula, numero_piso, numero_edificio, capacidad_asientos):
		self.nombre_aula = nombre_aula
		self.numero_piso = numero_piso
		self.numero_edificio = numero_edificio
		self.capacidad_asientos = capacidad_asientos

	def __str__(self):
		txt = f'''
		Aula: {self.nombre_aula}
		Piso: {self.numero_piso}
		Edificio: {self.numero_edificio}
		Capacidad de Asientos: {self.capacidad_asientos}
		'''
		return txt
# metodos de propiedad del argumeto -> nombre_aula
	
	@property
	def nombre_aula(self):
		return self.__nombre_aula
	
	@nombre_aula.setter
	def nombre_aula(self, nombre_aula):
		self.__nombre_aula = nombre_aula
	
	@nombre_aula.deleter
	def nombre_aula(self):
		del self.__nombre_aula
	
# metodos de propiedad del argumeto -> numero_piso
	
	@property
	def numero_piso(self):
		return self.__numero_piso
	
	@numero_piso.setter
	def numero_piso(self, numero_piso):
		self.__numero_piso = numero_piso
	
	@numero_piso.deleter
	def numero_piso(self):
		del self.__numero_piso
	
# metodos de propiedad del argumeto -> numero_edificio
	
	@property
	def numero_edificio(self):
		return self.__numero_edificio
	
	@numero_edificio.setter
	def numero_edificio(self, numero_edificio):
		self.__numero_edificio = numero_edificio
	
	@numero_edificio.deleter
	def numero_edificio(self):
		del self.__numero_edificio
	
# metodos de propiedad del argumeto -> canpacidad_asientos
	
	@property
	def capacidad_asientos(self):
		return self.__capacidad_asientos
	
	@capacidad_asientos.setter
	def capacidad_asientos(self, capacidad_asientos):
		self.__capacidad_asientos = capacidad_asientos
	
	@capacidad_asientos.deleter
	def capacidad_asientos(self):
		del self.__capacidad_asientos
