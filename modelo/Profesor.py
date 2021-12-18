from datetime import date

from modelo.Aula import Aula
#from modelo.Curso import Curso
from modelo.Persona import Persona
from modelo.Programa import Programa

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    
class Profesor(Persona):
    contador_profesor = 0
    #lstPersona = []
    lstProfesores = []

    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nac,
                 email, cod_profesor) -> None:
        Profesor.contador_profesor = + 1
        super().__init__(nombre, apellido, cedula, direccion, telefono, fecha_nac, email)
        self.id_profesor = Profesor.contador_profesor
        self.cod_profesor = cod_profesor
        self.programas = []
        self.cursos = []

    def __str__(self) -> str:
        txt = f"""\nProfesor: {self.cod_profesor}
        {super.__str__(self)}
        """
        return txt

    def agregar_programa(self, programa:Programa):
        self.programas.append(programa)
        
    def remover_programa(self, programa:Programa)->bool:
        for programa_it in self.programas:
            if programa.id_programa == programa_it.id_programa:
                self.programas.remove(programa_it)
                return True
        return False
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)
        
    def remover_curso(self, curso)->bool:
        for curso_it in self.cursos:
            if curso.id_curso == curso_it.id_curso:
                self.cursos.remove(curso_it)
                return True
        return False
    # region Metodos attr -> cod_profesor
    @property
    def cod_profesor(self):
        return self.__cod_profesor

    @cod_profesor.setter
    def cod_profesor(self, value):
        self.__cod_profesor = value

    @cod_profesor.deleter
    def cod_profesor(self):
        del self.__cod_profesor

    # endregion Metodos attr -> cod_profesor

    @classmethod
    def mostrar_profesores(cls):
        for profe in cls.lstProfesores:
            print(profe.__str__())
            
    @classmethod
    def profesores_editar_mostar(cls):
        print(f"ID|".ljust(6), end="")
        print(f"C_P|".ljust(7), end="")
        print(f"Nombre|".ljust(8), end="")
        print(f"Apellido|".ljust(12), end="")
        print(f"Cedula|".ljust(14), end="")
        print(f"Direccion|".ljust(15), end="")
        print(f"Telefono|".ljust(17), end="")
        print(f"Fecha_nac|".ljust(19), end="")
        print(f"Email|".ljust(20), end="")
        print("\n")

        for profe in cls.lstProfesores[:]:
            id = cls.lstProfesores.index(profe)
            
            print(f"{bcolors.FAIL} {id+1} {bcolors.RESET}".ljust(8), end="")
            print(f"{profe.cod_profesor}".ljust(7), end="")
            print(f"{profe.nombre}".ljust(8), end="")
            print(f"{profe.apellido}".ljust(12), end="")
            print(f"{profe.cedula}".ljust(14), end="")
            print(f"{profe.direccion}".ljust(15), end="")
            print(f"{profe.telefono}".ljust(17), end="")
            print(f"{profe.fecha_nac}".ljust(19), end="")
            print(f"{profe.email}".ljust(20), end="")
            print("\n")
 
 
    @classmethod
    def crear_profesor(cls):
        cod_profesor = input("Digite el cod_profesor del profesor: ")
        nombre = input("Digite el nombre del profesor: ")
        apellido = input("Digite el apellido del profesor: ")
        cedula = input("Digite el cedula del profesor: ")
        direccion = input("Digite el direccion del profesor: ")
        telefono = input("Digite el telefono del profesor: ")
        fecha_nac = input("Digite el fecha_nac del profesor: ")
        email = input("Digite el email del profesor: ")
        
        cls.lstProfesores.append(
            Profesor(
                cod_profesor=cod_profesor,
                nombre=nombre,
                apellido=apellido,
                cedula=cedula,
                direccion=direccion,
                telefono=telefono,
                fecha_nac=fecha_nac,
                email=email
        ))

    @classmethod
    def editar_profesor(cls):
        op = int(input('[?] Digita el id del profesor: '))
        print('Proporciona los siguientes datos...')
        
        cls.lstProfesores[op-1].cod_profesor = input("Digite el cod_profesor del profesor: ")
        cls.lstProfesores[op-1].nombre = input("Digite el nombre del profesor: ")
        cls.lstProfesores[op-1].apellido = input("Digite el apellido del profesor: ")
        cls.lstProfesores[op-1].cedula = input("Digite el cedula del profesor: ")
        cls.lstProfesores[op-1].direccion = input("Digite el direccion del profesor: ")
        cls.lstProfesores[op-1].telefono = input("Digite el telefono del profesor: ")
        cls.lstProfesores[op-1].fecha_nac = input("Digite el fecha_nac del profesor: ")
        cls.lstProfesores[op-1].email = input("Digite el email del profesor: ")
        



    @classmethod
    def obtener_profesor(cls):
        """Retorna un objeto de tipo profesor"""
        cls.mostrar_profesores()
        op = int(input('Digita el id del Profesor a obtener: '))
        obt_profesor = cls.lstPersona[(op - 1)]
        return obt_profesor

