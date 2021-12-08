class Edificio:
    def __init__(self, nombre, direccion, numero_edificio, cantidad_pisos,
                 cantidad_aulas, obj_aula):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_edificio = numero_edificio
        self.cantidad_pisos = cantidad_pisos
        self.cantidad_aulas = cantidad_aulas
        self.obj_aula = obj_aula

    # region metodos de propiedad del argumeto -> nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    # endregion metodos -> nombre

    # region metodos de propiedad del argumeto -> direccion

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @direccion.deleter
    def direccion(self):
        del self.__direccion

    # endregion metodos -> direccion

    # region metodos de propiedad del argumeto -> numero_edificio

    @property
    def numero_edificio(self):
        return self.__numero_edificio

    @numero_edificio.setter
    def numero_edificio(self, numero_edificio):
        self.__numero_edificio = numero_edificio

    @numero_edificio.deleter
    def numero_edificio(self):
        del self.__numero_edificio

    # endregion metodos -> numero_edificio

    # region metodos de propiedad del argumeto -> cantidad_pisos

    @property
    def cantidad_pisos(self):
        return self.__cantidad_pisos

    @cantidad_pisos.setter
    def cantidad_pisos(self, cantidad_pisos):
        self.__cantidad_pisos = cantidad_pisos

    @cantidad_pisos.deleter
    def cantidad_pisos(self):
        del self.__cantidad_pisos

    # endregion metodos -> cantidad_pisos

    # region metodos de propiedad del argumeto -> cantidad_aulas

    @property
    def cantidad_aulas(self):
        return self.__cantidad_aulas

    @cantidad_aulas.setter
    def cantidad_aulas(self, cantidad_aulas):
        self.__cantidad_aulas = cantidad_aulas

    @cantidad_aulas.deleter
    def cantidad_aulas(self):
        del self.__cantidad_aulas
    # endregion metodos -> cantidad_aulas
