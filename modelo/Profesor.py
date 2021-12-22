from datetime import date

from controlador.CReglasNegocio import valida_max_docente_asign
from modelo.Curso import Curso
from modelo.Persona import Persona


class bcolors:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


class Profesor(Persona):

    contador_profesor = 0
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
        txt = f"""\nProfesor Codigo: {self.cod_profesor}
        {super().__str__()}
        """
        return txt

    def agregar_programa(self, programa):
        self.programas.append(programa)
        
    def remover_programa(self, programa) -> bool:
        for programa_it in self.programas:
            if programa.id_programa == programa_it.id_programa:
                self.programas.remove(programa_it)
                return True
        return False
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def remover_curso(self, curso):
        self.cursos.remove(curso)

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
            id_ = cls.lstProfesores.index(profe)
            
            print(f"{bcolors.FAIL} {id_+1} {bcolors.RESET}".ljust(8), end="")
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
        cod_profesor = input("Digite el codigo del profesor: ")
        nombre = input("Digite el Nombre: ")
        apellido = input("Digite el Apellido: ")
        cedula = input("Digite la cedula: ")
        direccion = input("Digite la direccion: ")
        telefono = input("Digite el numero de telefono: ")
        print("Digite la fecha de nacimiento")
        anio = int(input('Digite el Año[1999]: '))
        mes = int(input('Digite el mes[1-12]: '))
        dia = int(input('Digite el dia: '))
        fecha_nac = date(anio, mes, dia)
        email = input("Digite el email: ")

        profe = Profesor(nombre, apellido, cedula, direccion, telefono, fecha_nac, email, cod_profesor)
        dec = input(f'[?] Desea agregar un curso al profesor {profe.nombre} y/n: ').lower()
        if dec == 'y':
            profe.agregar_curso(Curso.obtener_curso(True))

        cls.lstProfesores.append(profe)

    @classmethod
    def editar_profesor(cls):
        op = int(input('[?] Digita el id del profesor: '))
        print('Proporciona los siguientes datos...')
        
        cls.lstProfesores[op-1].cod_profesor = input("Digite el codigo del profesor: ")
        cls.lstProfesores[op-1].nombre = input("Digite el nombrer: ")
        cls.lstProfesores[op-1].apellido = input("Digite el apellido: ")
        cls.lstProfesores[op-1].cedula = input("Digite la cedula: ")
        cls.lstProfesores[op-1].direccion = input("Digite la direccion: ")
        cls.lstProfesores[op-1].telefono = input("Digite el telefono: ")
        print("Digite la fecha de nacimiento")
        anio = int(input('Digite el Año: '))
        mes = int(input('Digite el mes[1-12]: '))
        dia = int(input('Digite el dia: '))
        cls.lstProfesores[op-1].fecha_nac = date(anio, mes, dia)
        cls.lstProfesores[op-1].email = input("Digite el email: ")

        if len(cls.lstProfesores[op-1].cursos) > 0:
            opc = input(f'[?] Desea eliminar un curso de los que imparte '
                        f'{cls.lstProfesores[op-1].nombre} (y/n): ').lower()
            if opc == 'y':
                print('Cursos...')
                for curso in cls.lstProfesores[op-1].cursos:
                    print(curso.__str__())
                    opt = input('[?] Desea eliminar este Curso (y/n): ').lower()
                    if opt == 'y':
                        cls.lstProfesores[op-1].remover_curso(curso)

        dec = input(f'[?] Desea agregar un curso al profesor {cls.lstProfesores[op-1].nombre} y/n: ').lower()
        if dec == 'y':
            cant_curso = len(cls.lstProfesores[op - 1].cursos)
            if valida_max_docente_asign(cant_curso):
                cls.lstProfesores[op - 1].agregar_curso(Curso.obtener_curso(True))

    @classmethod
    def obtener_profesor(cls):
        """Retorna un objeto de tipo profesor"""
        cls.mostrar_profesores()
        op = int(input('Digita el id del Profesor a obtener: '))
        obj_profesor = cls.lstProfesores[(op - 1)]
        return obj_profesor

    @classmethod
    def obtener_cant_registros_profesores(cls):
        return len(cls.lstProfesores)

    @classmethod
    def mostrar_reg_detallados(cls):
        for prof in cls.lstProfesores:
            print(prof.__str__())
            for cur in prof.cursos:
                print('Cursos que imparte...')
                print(cur.__str__())