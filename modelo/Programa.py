from datetime import date

from controlador import CReglasNegocio
from controlador.CReglasNegocio import valida_duracion_programa, valida_maxmin_curso_program
from modelo.Profesor import Profesor


class Programa:
    """Clase programa"""
    cont_prgrama = 0
    __lstprogramas = []

    def __init__(self, nombre_programa=None, fecha_programa=None,
                 duracion_anios=None, status_programa='Cerrado', director=None):
        """Constructor de la clase programa"""
        Programa.cont_prgrama += 1
        self.nombre_programa = nombre_programa
        self.fecha_programa = fecha_programa
        self.status_programa = status_programa
        self.duracion_anios = duracion_anios
        self.director = director
        self.id_programa = Programa.cont_prgrama
        self.cant_curso = 0
        self.cant_matriculados = 0

    def __str__(self) -> str:
        txt = f'''
        ID del Programa: {self.id_programa}
        Nombre del Programa: {self.nombre_programa}
        Fecha de Inicio: {self.fecha_programa}
        Estado: {self.status_programa}
        Duracion (años): {self.duracion_anios}
        Cantidad de cursos en el programa: {self.cant_curso}
        Director: {self.director}\n'''
        return txt

    # region metodos de propiedad del argumeto -> cant_curso
    @property
    def cant_curso(self) -> int:
        return self.__cant_curso

    @cant_curso.setter
    def cant_curso(self, cant_curso):
        self.__cant_curso = cant_curso

    @cant_curso.deleter
    def cant_curso(self):
        del self.__cant_curso

    # endregion metodos de propiedad del argumeto -> cant_curso

    # region metodos de propiedad del argumeto -> cant_matriculados
    @property
    def cant_matriculados(self) -> int:
        return self.__cant_matriculados

    @cant_matriculados.setter
    def cant_matriculados(self, cant_matriculados):
        self.__cant_matriculados = cant_matriculados

    @cant_matriculados.deleter
    def cant_matriculados(self):
        del self.__cant_matriculados

    # endregion metodos de propiedad del argumeto -> cant_matriculados

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
    # endregion metodos -> directos

    # region metodos -> duracion anios
    @property
    def duracion_anios(self):
        return self.__duracion_anios

    @duracion_anios.setter
    def duracion_anios(self, duracion_anios):
        self.__duracion_anios = duracion_anios

    @duracion_anios.deleter
    def duracion_anios(self):
        del self.__duracion_anios
    # endregion metodos -> duracion anios

    # region Metodos de clase

    @classmethod
    def ingresar_registro(cls, obj_programa):
        cls.__lstprogramas.append(obj_programa)

    @classmethod
    def listar_programas(cls):
        for program in cls.__lstprogramas:
            print(program.__str__())

    @classmethod
    def editar_programa(cls):
        cls.listar_programas()
        op = int(input('[?] Digita el id del programa: '))
        print('Proporciona los siguientes datos...')
        cls.__lstprogramas[(op - 1)].nombre_programa = input('Nombre del Programa: ')
        cls.__lstprogramas[(op - 1)].fecha_programa = date.today()
        cls.__lstprogramas[(op - 1)].duracion_anios = valida_duracion_programa()
        cls.__lstprogramas[(op - 1)].director = Profesor.obtener_profesor()

    @classmethod
    def modificar_status_programa(cls):
        cls.listar_programas()
        op = int(input('[?] Digita el id del programa: '))
        matriculados = cls.__lstprogramas[(op - 1)].cant_matriculados
        desicion = input('Desea establecer el estado del programa, como abierto? y/n: ').lower()
        if desicion == 'y':
            if not(CReglasNegocio.valida_maxmin_estud_programa(matriculados)):
                print('Error. No se pudo cambiar el status del programa...\
                        no se Cumple con la cantidad de matriculas suficientes.')
            else:
                cls.__lstprogramas[(op - 1)].status_programa = 'Abierto'
                print('El status del programa se cambio a -> "Abierto"')

    @classmethod
    def eliminar_programa(cls):
        cls.listar_programas()
        op = int(input('[?] Digita el id del programa: '))
        cls.__lstprogramas.pop((op - 1))

    @classmethod
    def obtener_programa(cls):
        cls.listar_programas()
        op = int(input('[?] Digita el id del programa: '))
        program_elegido = cls.__lstprogramas[(op-1)]
        return program_elegido
    # endregion Metodos de clase

    #  FALTA --> Se bebe sobreescribir el metodo destructor __del__

# region Pruebas de la clase programa
# if __name__ == '__main__':
#     prg1 = Programa(
#         'Matematicas',
#         date(2021, 5, 12),
#         'Abierto',
#         'Ronald Reyes'
#     )
#
#     # print(prg1)
#     Programa.agregar_programa(prg1)
#     print(Programa.mostrar_detalle())
# endregion Pruebas de la clase programa
