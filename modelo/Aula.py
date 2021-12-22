from modelo.Edificio import Edificio


class Aula:

    __cont_aula = 0
    __list = []

    def __init__(self, nombre_aula, numero_piso, numero_edificio, capacidad_asientos):
        Aula.__cont_aula += 1
        self.nombre_aula = nombre_aula
        self.numero_piso = numero_piso
        self.numero_edificio = numero_edificio
        self.capacidad_asientos = capacidad_asientos
        self.id_aula = Aula.__cont_aula

    def __str__(self):
        txt = f'''Id del Aula: {self.id_aula}
        Aula: {self.nombre_aula}
        Piso: {self.numero_piso}
        Capacidad de Asientos: {self.capacidad_asientos}
        Edificio: {self.numero_edificio}
        '''
        return txt

    # region metodos de propiedad del argumeto -> nombre_aula

    @property
    def nombre_aula(self):
        return self.__nombre_aula

    @nombre_aula.setter
    def nombre_aula(self, nombre_aula):
        self.__nombre_aula = nombre_aula

    @nombre_aula.deleter
    def nombre_aula(self):
        del self.__nombre_aula

    # endregion metodos de propiedad del argumeto -> nombre_aula

    # region metodos de propiedad del argumeto -> numero_piso
    @property
    def numero_piso(self):
        return self.__numero_piso

    @numero_piso.setter
    def numero_piso(self, numero_piso):
        self.__numero_piso = numero_piso

    @numero_piso.deleter
    def numero_piso(self):
        del self.__numero_piso

    # endregion metodos de propiedad del argumeto -> numero_piso

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

    # endregion metodos de propiedad del argumeto -> numero_edificio

    # region metodos de propiedad del argumeto -> canpacidad_asientos

    @property
    def capacidad_asientos(self):
        return self.__capacidad_asientos

    @capacidad_asientos.setter
    def capacidad_asientos(self, capacidad_asientos):
        self.__capacidad_asientos = capacidad_asientos

    @capacidad_asientos.deleter
    def capacidad_asientos(self):
        del self.__capacidad_asientos

    # endregion metodos de propiedad del argumeto -> canpacidad_asientos

    # region Metodos de Clase
    @classmethod
    def listar_aulas(cls):
        for aula in cls.__list:
            print(aula.id_aula, end=" ")
            print(aula.nombre_aula, end=" ")
            print(aula.numero_edificio, end=" ")
            print(aula.capacidad_asientos, end=" ")

    @classmethod
    def agregar_aula(cls):
        nombre = input("Nombre del aula: ")
        num_pisos = int(input("Numero de piso: "))
        edficio_eleccion = Edificio.obtener_edificio()
        capacidad = int(input("Capacidad Asientos: "))
        aula = Aula(nombre, num_pisos, edficio_eleccion, capacidad)

        cls.__list.append(aula)

    @classmethod
    def editar_aula(cls):
        cls.listar_aulas()
        eleccion = int(input("Digite el Id del aula"))
        cls.__list[eleccion - 1].nombre_aula = input("Nombre del aula: ")
        cls.__list[eleccion - 1].numero_piso = int(input("Numero de piso: "))
        cls.__list[eleccion - 1].capacidad_asientos = int(input("Capacidad Asientos: "))

    @classmethod
    def eliminar_aula(cls):
        cls.listar_aulas()
        eleccion = int(input("Digite el Id del aula"))
        cls.__list.pop(eleccion - 1)

    @classmethod
    def obtener_aula(cls):
        """Metodo que retorna un objeto de aula para agregar a un curso"""
        cls.listar_aulas()
        op = int(input('Digite el id del aula a obtener: '))
        aula_elegida = cls.__list[(op - 1)]
        return aula_elegida

    @classmethod
    def obtener_cant_registro_aulas(cls):
        return len(cls.__list)
    # endregion Metodos de Clase
