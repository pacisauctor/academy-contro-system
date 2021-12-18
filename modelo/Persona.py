from datetime import date


class Persona:

    contador_personas = 0
    lstPersona = []

    def __init__(self, nombre, apellido, cedula, direccion,
                 telefono, fecha_nac, email) -> None:
        Persona.contador_personas += 1
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_nac = fecha_nac
        self.email = email
        self.id_persona = Persona.contador_personas
        Persona.crear_persona(self)

    def __str__(self) -> str:
        txt = f"""\nPersona:{self.id_persona}
        Nombre: {self.nombre} 
        Apellido: {self.apellido}
        Cedula: {self.cedula}
        Direccion: {self.direccion}
        Telefono: {self.telefono}
        Email: {self.email}
        Fecha de Nacimiento: {self.fecha_nac}
        """
        return txt

    # region metodos -> nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    # endregion metodos -> nombre

    # region metodos -> apellidos
    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, value):
        self.__apellido = value

    @apellido.deleter
    def apellido(self):
        del self.__apellido

    # endregion metodos -> apellidos

    # region metodos -> cedula
    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, value):
        self.__cedula = value

    @cedula.deleter
    def cedula(self):
        del self.__cedula

    # endregion metodos -> cedula

    # region metodos -> direccion
    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @direccion.deleter
    def direccion(self):
        del self.__direccion

    # endregion metodos -> direccion

    # region metodos -> telefono
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        self.__telefono = value

    @telefono.deleter
    def telefono(self):
        del self.__telefono
    # endregion metodos -> telefono

    # region metodos -> fecha_nac
    @property
    def fecha_nac(self):
        return self.__fecha_nac

    @fecha_nac.setter
    def fecha_nac(self, value):
        self.__fecha_nac = value

    @fecha_nac.deleter
    def fecha_nac(self):
        del self.__fecha_nac
    # endregion metodos -> fecha_nac

    # region metodos -> email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @email.deleter
    def email(self):
        del self.__email
    # endregion metodos -> email

    # region Otros Metodos
    def birthday(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nac.year

        if self.fecha_nac.month >= hoy.month:
            if self.fecha_nac.day > hoy.day:
                edad -= 1

        return edad
    # endregion Otros Metodos

    # region Metod de Clase
    @classmethod
    def crear_persona(cls, objpersona):
        cls.lstPersona.append(objpersona)

    @classmethod
    def detalles_personas(cls):
        personas_str = ""
        for persona in cls.lstPersona:
            personas_str += persona.__str__()
        return personas_str

    @classmethod
    def tamaniolst(cls):
        return len(cls.lstPersona)
    # endregion Metod de Clase


