from datetime import date


class Programa:
    """Clase programa"""
    cont_prgrama = 0

    def __init__(self, nombre_programa, fecha_programa, duracion_anios, status_programa, director):
        """Constructor de la clase programa"""
        Programa.cont_prgrama += 1
        self.nombre_programa = nombre_programa
        self.fecha_programa = fecha_programa
        self.status_programa = status_programa
        self.duracion_anios = duracion_anios
        self.director = director
        self.id_programa = Programa.cont_prgrama

    def __str__(self) -> str:
        txt = f'''
        Detalles del Programa: {self.id_programa}
        Nombre del Programa: {self.nombre_programa}
        Fecha de Inicio: {self.fecha_programa}
        Estado: {self.status_programa}
        Duracion (años): {self.duracion_anios}
        Director: {self.director}\n'''
        return txt

    # region metodos de propiedad del argumeto -> nombre_programa

    @property
    def nombre_programa(self):
        return self.__nombre_programa

    @nombre_programa.setter
    def nombre_programa(self, nombre_programa):
        self.__nombre_programa = nombre_programa

    @nombre_programa.deleter
    def nombre_programa(self):
        del self.__nombre_programa

    # endregion metodos -> nombre_programa

    # region metodos de propiedad del argumeto -> fecha_programa

    @property
    def fecha_programa(self):
        return self.__fecha_programa

    @fecha_programa.setter
    def fecha_programa(self, fecha_programa):
        self.__fecha_programa = fecha_programa

    @fecha_programa.deleter
    def fecha_programa(self):
        del self.__fecha_programa

    # endregion metodos -> fec ha_programa

    # region metodos de propiedad del argumeto -> status_programa

    @property
    def status_programa(self):
        return self.__status_programa

    @status_programa.setter
    def status_programa(self, status_programa):
        self.__status_programa = status_programa

    @status_programa.deleter
    def status_programa(self):
        del self.__status_programa

    # endregion metodos -> status_programa

    # region metodos de propiedad del argumeto -> director

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        self.__director = director

    @director.deleter
    def director(self):
        del self.__director


    @property
    def duracion_anios(self):
        return self.__duracion_anios

    @duracion_anios.setter
    def duracion_anios(self, duracion_anios):
        self.__duracion_anios = duracion_anios

    @duracion_anios.deleter
    def duracion_anios(self):
        del self.__duracion_anios
    # endregion metodos -> directos

    # region Metodos de clase
    @classmethod
    def agregar_programa(cls):
        nombre_programa = input("Ingrese el nombre_programa: ")
        fecha_programa = input("Ingrese el fecha_programa: ")
        status_programa = input("Ingrese el status_programa: ")
        indice = int(input("Ingrese el id del profesor:"))
        
        
        return Programa(
            nombre_programa = nombre_programa,
            fecha_programa = fecha_programa,
            status_programa = status_programa,
            director = indice
        )
    
    
    @classmethod
    def editar_programa(cls, programa):
        programa.nombre_programa = input("Ingrese el nombre_programa: ")
        programa.fecha_programa = input("Ingrese el fecha_programa: ")
        programa.status_programa = input("Ingrese el status_programa: ")
        programa.director =  int(input("Ingrese el id del profesor:"))
        return programa

    @classmethod
    def mostrar_programas(cls, programas:list):
        for programa in programas:
            print(programa)
    
    
    
    # endregion Metodos de clase


# region Pruebas de la clase programa
if __name__ == '__main__':
    prg1 = Programa(
        'Matematicas',
        date(2021, 5, 12),
        'Abierto',
        'Ronald Reyes'
    )

    # print(prg1)
    Programa.agregar_programa(prg1)
    print(Programa.mostrar_detalle())
# endregion Pruebas de la clase programa
