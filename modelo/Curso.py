from controlador import CReglasNegocio
from controlador.CReglasNegocio import valida_maxmin_estud_curso
from modelo.Aula import Aula
from modelo.Programa import Programa


class Curso:

    __cont_curso = 0
    __lst_cursos = list()

    def __init__(self, nombre_curso=None, creditos=None,
                 cant_hrs_semanales=None, precio=None, estado='Cerrado'):
        Curso.__cont_curso += 1
        self.nombre_curso = nombre_curso
        self.creditos = creditos
        self.cant_hrs_semanales = cant_hrs_semanales
        self.precio = precio
        self.estado = estado
        self.cant_matricula = 0
        self.lstaulas = []
        self.lstprogramas = []
        self.id_curso = Curso.__cont_curso

    def __str__(self):
        txt = f'''
        Id del Curso: {self.id_curso}
        Nombre del Curso: {self.nombre_curso}
        Creditos: {self.creditos}
        Horas Semanales: {self.cant_hrs_semanales}
        '''
        return txt

    # region metodos de propiedad del argumeto -> nombre_curso

    @property
    def nombre_curso(self):
        return self.__nombre_curso

    @nombre_curso.setter
    def nombre_curso(self, nombre_curso):
        self.__nombre_curso = nombre_curso

    @nombre_curso.deleter
    def nombre_curso(self):
        del self.__nombre_curso

    # endregion metodos -> nombre_curso

    # region metodos de propiedad del argumeto -> creditos

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, creditos):
        self.__creditos = creditos

    @creditos.deleter
    def creditos(self):
        del self.__creditos

    # endregion metodos -> creditos

    # region metodos de propiedad del argumeto -> cant_hrs_semanales

    @property
    def cant_hrs_semanales(self):
        return self.__cant_hrs_semanales

    @cant_hrs_semanales.setter
    def cant_hrs_semanales(self, cant_hrs_semanales):
        self.__cant_hrs_semanales = cant_hrs_semanales

    @cant_hrs_semanales.deleter
    def cant_hrs_semanales(self):
        del self.__cant_hrs_semanales

    # endregion metodos -> cant_hrs_semanales

    # region metodos de propiedad del argumeto -> precio

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @precio.deleter
    def precio(self):
        del self.__precio
    # endregion metodos -> precio

    # region metodos de propiedad del argumeto -> estado

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @estado.deleter
    def estado(self):
        del self.__estado
    # endregion metodos -> precio

    # region metodos de propiedad del argumeto -> cant_matricula
    @property
    def cant_matricula(self):
        return self.__cant_matricula

    @cant_matricula.setter
    def cant_matricula(self, cant_matricula):
        self.__cant_matricula = cant_matricula

    @cant_matricula.deleter
    def cant_matricula(self):
        del self.__cant_matricula

    # endregion metodos de propiedad del argumeto -> cant_matricula

    # region Metodos de Instancia

    def add_aula(self, obj_aula: Aula):
        self.lstprogramas.append(obj_aula)

    def delete_aula(self, obj_aula: Aula):
        self.lstprogramas.remove(obj_aula)

    def add_programa(self, obj_programa: Programa):
        obj_programa.cant_curso += 1
        self.lstprogramas.append(obj_programa)

    def delete_progama(self, obj_programa: Programa):
        obj_programa.cant_curso -= 1
        self.lstprogramas.remove(obj_programa)

    # endregion Metodos de Instancia

    # region Metodos de clase

    @classmethod
    def add_registro_curso(cls, obj_curso):
        cls.__lst_cursos.append(obj_curso)

    @classmethod
    def listar_registros_cursos(cls):
        for curso in cls.__lst_cursos:
            print(curso.__str__())

    @classmethod
    def editar_registro_curso(cls):
        curso_elegido = None
        Curso.listar_registros_cursos()
        op = int(input('Digita el id del curso a editar: '))
        for registro in cls.__lst_cursos:
            if registro.id_curso == op:
                curso_elegido = registro

        print('Proporciona los siguientes Datos...')
        curso_elegido.nombre = input('Digita el nombre del curso: ')
        curso_elegido.creditos = int(input('Digita la cantidad de creditos del curso: '))
        curso_elegido.horas = float(input('Digita la cantidad de horas del curso: '))
        curso_elegido.precio = float(input('Digita el precio: '))

        if len(curso_elegido.lstaulas) > 0:
            op = input('[?] Desea eliminar aulas (y/n): ').lower()
            if op == 'y':
                print('Aulas en las que se imparte el curso...')
                for aula in curso_elegido.lstaulas:
                    print(aula.__str__())
                    opt = input('[?] Desea elinar el aula (y/n): ').lower()
                    if opt == 'y':
                        curso_elegido.delete_aula(aula)

        op = input('[?] Desea agregar un aula (y/n): ').lower()
        if op == 'y':
            aulaAgregar = Aula.obtener_aula()
            curso_elegido.add_aula(aulaAgregar)

        if len(curso_elegido.lstprogramas) > 0:
            op = input('[?] Desea eliminar Programas a los que pertenece el curso (y/n): ').lower()
            if op == 'y':
                print('Programas a los que pertenece el Curso...')
                for programa in curso_elegido.lstprogramas:
                    print(programa.__str__())
                    opt = input('[?] Desea eliminar este Programa (y/n): ').lower()
                    if opt == 'y':
                        curso_elegido.delete_progama(programa)
                    else:
                        break

        op = input('[?] Desea agregar un programa (y/n): ').lower()
        if op == 'y':
            proAgregar = Programa.obtener_programa()
            can_curso = proAgregar.cant_curso
            if not (CReglasNegocio.valida_maxmin_curso_program(can_curso)):
                print('Error. No se pueden agregar mas cursos al programa...')
            else:
                curso_elegido.add_programa(proAgregar)

    @classmethod
    def eliminar_registro_curso(cls):
        Curso.listar_registros_cursos()
        op = int(input('Digita el id del curso a eliminar: '))
        for curso in cls.__lst_cursos:
            if curso.id_curso == op:
                cls.__lst_cursos.remove(curso)

    @classmethod
    def obtener_curso(cls, listar=False):
        cursoObtenido = None
        if listar:
            Curso.listar_registros_cursos()
        op = int(input('Digita el id del curso: '))
        for curso in cls.__lst_cursos:
            if curso.id_curso == op:
                cursoObtenido = curso
                break
        if cursoObtenido is None:
            print('Error: No se encontro el curso seleccionado.')
        return cursoObtenido

    @classmethod
    def modificar_estado_curso(cls, obj_programa: Programa):
        for curso in cls.__lst_cursos:
            if valida_maxmin_estud_curso(curso.cant_matricula):
                for prog in curso.lstprogramas:
                    if obj_programa.id_programa == prog.id_programa:
                        curso.estado = 'Abierto'
                        break
            else:
                print(f'El curso {curso.nombre_curso}, no se pudo aperturar.')

    @classmethod
    def listar_curso_en_programa(cls, obj_programa: Programa):
        print('Cursos que pertenecen a este programa')
        for curso in cls.__lst_cursos:
            for prog in curso.lstprogramas:
                if obj_programa.id_programa == prog.id_programa:
                    print(curso)
                    break

    # endregion Metodos de clase
