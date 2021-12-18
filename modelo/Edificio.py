
class Edificio:

    __cont_edificio = 0
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

    def __str__(self):
        txt = f"""
        Id del Edificio: {self.id_edificio}
        Nombre: {self.nombre}
        Direccion: {self.direccion}
        Numero del Edificio: {self.numero_edificio}
        Cantidad de pisos: {self.cantidad_pisos}
        Cantidad de aulas: {self.cantidad_aulas}
        """
        return txt

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

    # region metodos lista aulas
    def agregar_aula(self, aula):
        self.aulas.append(aula)
        
    def remover_aula(self, aula) -> bool:
        for aula_it in self.aulas:
            if aula.id_aula == aula_it.id_aula:
                self.aulas.remove(aula_it)
                return True
        return False

    # endregion metodos lista aulas

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

    # endregion metodos de propiedad del argumeto -> cantidad_aulas

    # region Metodos de Clase
    @classmethod
    def listar_edificio(cls):
        for edificio in cls.__lstEdificio:
            print(edificio.__str__())

    @classmethod
    def agregar_edificio(cls):
        nombre = input("Ingrese el nombre del edificio: ")
        direccion = input("Ingrese la direccion del edificio: ")
        numero_edificio = input("Ingrese el numero de edificio: ")
        cantidad_pisos = input("Ingrese la cantidad de pisos del edificio: ")
        cantidad_aulas = input("Ingrese cantidad de aulas: ")

        edificio = Edificio(nombre, direccion, numero_edificio,
                            cantidad_pisos, cantidad_aulas)
        cls.__lstEdificio.append(edificio)

    @classmethod
    def editar_edificio(cls):
        edificio = None
        cls.listar_edificio()
        op = int(input('Digita el id del edificio: '))
        for edif in cls.__lstEdificio:
            if edif.id_edificio == op:
                edificio = edif
                break

        edificio.nombre = input("Ingrese el nombre del edificio: ")
        edificio.direccion = input("Ingrese la dirrecion del edificio: ")
        edificio.numero_edificio = input("Ingrese el numero del edificio: ")
        edificio.cantidad_pisos = input("Ingrese la cantidad de pisos: ")
        edificio.cantidad_aulas = input("Ingrese la cantidad de aulas: ")

    @classmethod
    def eliminar_edificio(cls):
        cls.listar_edificio()
        op = int(input('[?] Digita el id del Edificio: '))
        cls.__lstEdificio.pop((op - 1))

    @classmethod
    def obtener_edificio(cls):
        cls.listar_edificio()
        op = int(input('[?] Digita el id del Edificio: '))
        edifico_elegido = cls.__lstEdificio[(op-1)]
        return edifico_elegido
    # endregion Metodos de Clase
