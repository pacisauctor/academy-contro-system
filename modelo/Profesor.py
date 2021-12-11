from datetime import date

from modelo.Aula import Aula
from modelo.Curso import Curso
from modelo.Persona import Persona
from modelo.Programa import Programa


class Profesor(Persona):
    contador_profesor = 0
    lstPersona = []

    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nac,
                 email, cod_profesor, tipo_profesor) -> None:
        Profesor.contador_profesor = + 1
        super().__init__(nombre, apellido, cedula, direccion, telefono, fecha_nac, email)
        self.__id_profesor = Profesor.contador_profesor
        self.cod_profesor = cod_profesor
        self.tipo_profesor = tipo_profesor

    def __str__(self) -> str:
        txt = f"""\nProfesor: {self.cod_profesor}
        {super.__str__(self)}
        """
        return txt

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
    def mostrar_profesores(cls, list_profesores:list):
        for profe in list_profesores:
            print(profe)
            
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
        
        return Profesor(
            cod_profesor=cod_profesor,
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            direccion=direccion,
            telefono=telefono,
            fecha_nac=fecha_nac,
            email=email
        )

    @classmethod
    def editar_profesor(cls, profesor):
        profesor.cod_profesor = input("Digite el cod_profesor del profesor: ")
        profesor.nombre = input("Digite el nombre del profesor: ")
        profesor.apellido = input("Digite el apellido del profesor: ")
        profesor.cedula = input("Digite el cedula del profesor: ")
        profesor.direccion = input("Digite el direccion del profesor: ")
        profesor.telefono = input("Digite el telefono del profesor: ")
        profesor.fecha_nac = input("Digite el fecha_nac del profesor: ")
        profesor.email = input("Digite el email del profesor: ")
        
        return profesor
# region Probar Clase Profesor
if __name__ == '__main__':
    aul = Aula(
        'auala ciencias',
        5,
        1,
        24
    )

    cur = Curso(
        'Ciencias Naturales',
        4,
        5,
        'ciencias',
        aul
    )

    prg1 = Programa(
        'Matematicas',
        date(2021, 5, 12),
        'Abierto',
        'Ronald Reyes'
    )

    pro1 = Profesor(
        'Alex',
        'carballo',
        '001-123549-1002G',
        'rrsdf',
        '8795-1251',
        '2021-12-15',
        'alex@gmail.com',
        '0215',
        prg1
    )


    Profesor.crear_persona(pro1)
    print(Profesor.detalles_personas())

# endregion Probar Clase Profesor
