from datetime import date

from controlador.CReglasNegocio import valida_maxmin_estudiante_asign
from modelo.Curso import Curso
from modelo.Persona import Persona
from modelo.Programa import Programa


class Estudiante(Persona):

    cont_estudiante = 0
    __lstEstudiantes = []

    def __init__(self, nombre, apellido, cedula, direccion, telefono,
                 fecha_nac, email, num_carnet):
        Estudiante.cont_estudiante += 1
        super().__init__(nombre, apellido, cedula, direccion,
                         telefono, fecha_nac, email)
        self.num_carnet = num_carnet
        self.matriculas = []
        self._id_estudiante = Estudiante.cont_estudiante

    def __str__(self):
        txt = f"""
        Id del Estudiante: {self._id_estudiante}
        Carnet: {self.num_carnet}
        {super.__str__(self)}
        """
        return txt

    # region metodos de propiedad del argumeto -> id_estudiante

    @property
    def num_carnet(self):
        return self.__num_carnet

    @num_carnet.setter
    def num_carnet(self, num_carnet):
        self.__num_carnet = num_carnet

    @num_carnet.deleter
    def num_carnet(self):
        del self.__num_carnet
    # endregion Metodos -> id_estudiantes

    # region Metodo de matriculas
    def agregar_matricula(self, matricula):
        self.matriculas.append(matricula)
        
    def remover_matricula(self, matricula) -> bool:
        for matricula_it in self.matriculas:
            if matricula.id_matricula == matricula_it.id_matricula:
                self.matriculas.remove(matricula_it)
                return True
        return False

    # endregion Metodo de matriculas

    # region Metodos de Clase

    @classmethod
    def listar_estudiantes(cls):
        print("ID | Nombre | Apellido | Num Carnet")
        for estudiante in cls.__lstEstudiantes:
            print(f"{estudiante._id_estudiante}".ljust(5), end="")
            print(f"{estudiante.num_carnet}".ljust(5), end="")
            print(f"{estudiante.nombre}".ljust(10), end="")
            print(f"{estudiante.apellido}".ljust(11), end="")
            
    @classmethod
    def agregar_estudiantes(cls):
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        cedula = input("Ingrese el cedula del estudiante: ")
        direccion = input("Ingrese el direccion del estudiante: ")
        telefono = input("Ingrese el telefono del estudiante: ")
        print("Digite el fecha_nac del profesor ")
        anio = int(input('Digite el Año: '))
        mes = int(input('Digite el mes[1-12]: '))
        dia = int(input('Digite el dia: '))
        fecha_nac = date(anio, mes, dia)
        email = input("Ingrese el email del estudiante: ")
        numero_carnet = input("Ingrese el numero de carnet del estudiante: ")
        estudiante = Estudiante(nombre, apellido, cedula, direccion,
                                telefono, fecha_nac, email, numero_carnet)
        cls.__lstEstudiantes.append(estudiante)
    
    @classmethod
    def editar_estudiantes(cls):
        cls.listar_estudiantes()
        elc = int(input("Ingrese el ID del estudiante: "))
        cls.__lstEstudiantes[elc - 1].numero_carnet = input("Ingrese el numero de carnet del estudiante: ")
        cls.__lstEstudiantes[elc - 1].nombre = input("Ingrese el nombre del estudiante: ")
        cls.__lstEstudiantes[elc - 1].apellido = input("Ingrese el apellido del estudiante: ")
        cls.__lstEstudiantes[elc - 1].cedula = input("Ingrese el cedula del estudiante: ")
        cls.__lstEstudiantes[elc - 1].direccion = input("Ingrese el direccion del estudiante: ")
        cls.__lstEstudiantes[elc - 1].telefono = input("Ingrese el telefono del estudiante: ")
        print("Digite el fecha_nac del profesor ")
        anio = int(input('Digite el Año: '))
        mes = int(input('Digite el mes[1-12]: '))
        dia = int(input('Digite el dia: '))
        cls.__lstEstudiantes[elc - 1].fecha_nac = date(anio, mes, dia)
        cls.__lstEstudiantes[elc - 1].email = input("Ingrese el email del estudiante: ")

    @classmethod
    def eliminar_estudiante(cls):
        cls.listar_estudiantes()
        eleccion = int(input("Ingrese el ID del estudiante: "))
        cls.__lstEstudiantes.pop(eleccion - 1)

    @classmethod
    def obtener_estudiante(cls):
        cls.listar_estudiantes()
        eleccion = int(input("Ingrese el ID del estudiante: "))
        return cls.__lstEstudiantes[eleccion - 1]

    @classmethod
    def obtener_estudiante_byMatricula(cls, matricula):
        for estudiante in cls.__lstEstudiantes:
            if matricula in estudiante.matriculas:
                return estudiante

    @classmethod
    def addMatriculaToEstudiante(cls, matricula):
        cls.listar_estudiantes()
        eleccion = int(input("Ingrese el ID del estudiante a agregar matricula: "))
        cls.__lstEstudiantes[eleccion - 1].matricula(matricula)

    @classmethod
    def matricular(cls):
        if len(cls.__lstEstudiantes) > 0:
            carnet = input('Digita tu numero de carnet: ')
            for estudiante in cls.__lstEstudiantes:
                if estudiante.num_carnet == carnet:
                    est = estudiante
                    can_matricula = len(est.matriculas)
                    if valida_maxmin_estudiante_asign(can_matricula):
                        prog = Programa.obtener_programa()
                        Curso.listar_curso_en_programa(prog)
                        cur = Curso.obtener_curso()
                        est.matriculas.append(cur)
                    break
                else:
                    print('No se encontro el estudiante')
        else:
            print('No existen registros de estudiantes matriculados')

    @classmethod
    def obtener_cant_registro_estudiantes(cls):
        return len(cls.__lstEstudiantes)

    # endregion Metodos de Clase
