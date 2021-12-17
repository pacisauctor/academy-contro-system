from modelo.Matricula import Matricula
from modelo.Persona import Persona


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

    def agregar_matricula(self, matricula:Matricula):
        self.matriculas.append(matricula)
        
    def remover_matricula(self, matricula:Matricula)->bool:
        for matricula_it in self.matriculas:
            if matricula.id_matricula == matricula_it.id_matricula:
                self.matriculas.remove(matricula_it)
                return True
        return False
    # region Metodos de Clase
    @classmethod
    def crear_persona(cls, objpersona):
        cls.__lstEstudiantes.append(objpersona)
        
        
    
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
        fecha_nac = input("Ingrese la fecha de nacimiento del estudiante: ")
        email = input("Ingrese el email del estudiante: ")
        numero_carnet = input("Ingrese el numero de carnet del estudiante: ")
        estudiante = Estudiante(nombre=nombre, apellido=apellido, cedula=cedula, direccion=direccion, telefono=telefono, fecha_nac=fecha_nac, email=email, num_carnet=numero_carnet, obj_matricula=None)
        cls.__lstEstudiantes.append(estudiante)
    
    @classmethod
    def editar_estudiantes(cls):
        cls.listar_estudiantes()
        eleccion = int(input("Ingrese el ID del estudiante: "))
        cls.__lstEstudiantes[eleccion - 1].numero_carnet = input("Ingrese el numero de carnet del estudiante: ")
        cls.__lstEstudiantes[eleccion - 1].nombre = input("Ingrese el nombre del estudiante: ")
        cls.__lstEstudiantes[eleccion - 1].apellido = input("Ingrese el apellido del estudiante: ")
        cls.__lstEstudiantes[eleccion - 1].cedula = input("Ingrese el cedula del estudiante: ")
        cls.__lstEstudiantes[eleccion - 1].direccion = input("Ingrese el direccion del estudiante: ")
        cls.__lstEstudiantes[eleccion - 1].telefono = input("Ingrese el telefono del estudiante: ")
        cls.__lstEstudiantes[eleccion - 1].fecha_nac = input("Ingrese la fecha de nacimiento del estudiante: ")
        cls.__lstEstudiantes[eleccion - 1].email = input("Ingrese el email del estudiante: ")


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
    def obtener_estudiante_byMatricula(cls,matricula):
        for estudiante in cls.__lstEstudiantes:
            if matricula in estudiante.matriculas:
                return estudiante
                break

    @classmethod
    def addMatriculaToEstudiante(cls,matricula):
        cls.listar_estudiantes()
        eleccion = int(input("Ingrese el ID del estudiante a agregar matricula: "))
        cls.__lstEstudiantes[eleccion - 1].matricula(matricula)

    # endregion Metodos de Clase
