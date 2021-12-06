
class Aula:
	
	def __init__(self, nombre_aula, numero_piso, numero_edificio, canpacidad_asientos):
		self.nombre_aula = nombre_aula
		self.numero_piso = numero_piso
		self.numero_edificio = numero_edificio
		self.canpacidad_asientos = canpacidad_asientos

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
	def canpacidad_asientos(self):
		return self.__canpacidad_asientos
	
	@canpacidad_asientos.setter
	def canpacidad_asientos(self, canpacidad_asientos):
		self.__canpacidad_asientos = canpacidad_asientos
	
	@canpacidad_asientos.deleter
	def canpacidad_asientos(self):
		del self.__canpacidad_asientos
