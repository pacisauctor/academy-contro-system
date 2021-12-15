from modelo.Aula import Aula


class Edificio:
    __cont_edificio= 0
    __lstEdificio = []

    def __init__(self, nombre, direccion, numero_edificio, cantidad_pisos,
                 cantidad_aulas):
        Edificio.__cont_edificio += 1
        self.nombre = nombre
        self.direccion = direccion
        self.numero_edificio = numero_edificio
        self.cantidad_pisos = cantidad_pisos
        self.cantidad_aulas = cantidad_aulas
        self.aulas = []
        self.id_edificio = Edificio.__cont_edificio

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
    def agregar_aula(self, aula:Aula):
        self.aulas.append(aula)
        
    def remover_aula(self, aula:Aula)->bool:
        for aula_it in self.aulas:
            if aula.id_aula == aula_it.id_aula:
                self.aulas.remove(aula_it)
                return True
        return False
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
        
        

    @classmethod
    def listar_edificio(cls):
        for edificio in cls.__lstEdificio:
            print(edificio.numero_edificio,end=" ")
            print(edificio.nombre, end = " ")
            print(edificio.direccion, end = " ")

    @classmethod
    def agregar_edificio(cls):
        nombre = input("Ingrese el nombre del edificio: ")
        direccion = input("Ingrese la direccion del edificio: ")
        numero_edificio = input("Ingrese el numero de edificio: ")
        cantidad_pisos = input("Ingrese la cantidad de pisos del edificio: ")
        cantidad_aulas = input("Ingrese cantidad de aulas: ")

        edificio = Edificio(nombre, direccion, numero_edificio,cantidad_pisos, cantidad_aulas, None)
        cls.__lstEdificio.append(edificio)

    @classmethod
    def editar_edificio(cls):
        cls.listar_edificio()
        eleccion = int(input("Ingrese el ID del edificio: "))

        cls.__lstEdificio[eleccion].nombre = input("Ingrese el nombre del edificio: ")
        cls.__lstEdificio[eleccion].direccion = input("Ingrese la dirrecion del edificio: ")
        cls.__lstEdificio[eleccion].numero_edificio = input("Ingrese el numero del edificio: ")
        cls.__lstEdificio[eleccion].cantidad_pisos = input("Ingrese la cantidad de pisos: ")
        cls.__lstEdificio[eleccion].cantidad_aulas = input("Ingrese la cantidad de aulas: ")


    @classmethod
    def eliminar_edificio(cls):
        cls.listar_edificio()
        eleccion = int(input("Ingrese el ID del edificio: "))
        cls.__lstEdificio.pop(eleccion)


    