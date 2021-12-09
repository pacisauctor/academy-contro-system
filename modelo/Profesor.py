from datetime import date

from modelo.Aula import Aula
from modelo.Curso import Curso
from modelo.Persona import Persona
from modelo.Programa import Programa


class Profesor(Persona):
    contador_profesor = 0
    lstPersona = []

    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nac,
                 email, cod_profesor, obj_programa, obj_curso) -> None:
        Profesor.contador_profesor = + 1
        super().__init__(nombre, apellido, cedula, direccion, telefono, fecha_nac, email)
        self.__id_profesor = Profesor.contador_profesor
        self.cod_profesor = cod_profesor
        self.obj_programa = obj_programa
        self.obj_curso = obj_curso

    def __str__(self) -> str:
        txt = f"""\nProfesor: {self.cod_profesor}
        Nombre: {self.nombre} 
        Apellido: {self.apellido}
        Cedula: {self.cedula}
        Direccion: {self.direccion}
        Telefono: {self.telefono}
        Email: {self.email}
        Fecha de Nacimiento: {self.fecha_nac}
        \nPrograma: {self.obj_programa}
        \nCurso: {self.obj_curso}
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

    def crear_profesor(self):
        pass


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
        prg1,
        cur
    )


    Profesor.crear_persona(pro1)
    print(Profesor.detalles_personas())

# endregion Probar Clase Profesor
