from modelo.Persona import Persona


class Estudiante(Persona):

    cont_estudiante = 0
    __lstEstudiantes = []

    def __init__(self, nombre, apellido, cedula, direccion, telefono,
                 fecha_nac, email, num_carnet, obj_matricula):
        Estudiante.cont_estudiante += 1
        super().__init__(nombre, apellido, cedula, direccion,
                         telefono, fecha_nac, email)
        self.num_carnet = num_carnet
        self.obj_matricula = obj_matricula
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
    def convert_to_dictionary(self):
        return {
            "num_carnet": self.num_carnet,
            "obj_matricula": self.obj_matricula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "cedula": self.cedula,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "fecha_nac": self.fecha_nac,
            "email": self.email
        }


    # region Metodos de Clase
    @classmethod
    def crear_persona(cls, objpersona):
        cls.__lstEstudiantes.append(objpersona)
        
    @classmethod
    def get_from_dictionary(cls, dictionary:dict):
        return Estudiante(
            num_carnet = dictionary["num_carnet"],
            obj_matricula = dictionary["obj_matricula"],
            nombre = dictionary["nombre"],
            apellido = dictionary["apellido"],
            cedula = dictionary["cedula"],
            direccion = dictionary["direccion"],
            telefono = dictionary["telefono"],
            fecha_nac = dictionary["fecha_nac"],
            email = dictionary["email"]
        )
        

        
    
    @classmethod
    def listar_estudiantes(cls, list_estudiantes):
        print("ID | Nombre | Apellido | Num Carnet")
        for estudiante in list_estudiantes:
            print(f"{estudiante._id_estudiante}".ljust(5), end="")
            print(f"{estudiante.nombre}".ljust(10), end="")
            print(f"{estudiante.apellido}".ljust(11), end="")
            print(estudiante.num_carnet)
            
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
        return estudiante
    
    @classmethod
    def editar_estudiantes(cls, estudiante):
        estudiante.nombre = input("Ingrese el nombre del estudiante: ")
        estudiante.apellido = input("Ingrese el apellido del estudiante: ")
        estudiante.cedula = input("Ingrese el cedula del estudiante: ")
        estudiante.direccion = input("Ingrese el direccion del estudiante: ")
        estudiante.telefono = input("Ingrese el telefono del estudiante: ")
        estudiante.fecha_nac = input("Ingrese la fecha de nacimiento del estudiante: ")
        estudiante.email = input("Ingrese el email del estudiante: ")
        estudiante.numero_carnet = input("Ingrese el numero de carnet del estudiante: ")
        
        return estudiante
    # endregion Metodos de Clase
