class Persona:
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_nac, email) -> None:
        __nombre = nombre
        __apellido = apellido
        __cedula = cedula
        __direccion = direccion
        __telefono = telefono
        __fecha_nac = fecha_nac
        __email = email
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, value):
        self.__apellido = value

    @apellido.deleter
    def apellido(self):
        del self.__apellido

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, value):
        self.__cedula = value

    @cedula.deleter
    def cedula(self):
        del self.__cedula

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @direccion.deleter
    def direccion(self):
        del self.__direccion

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        self.__telefono = value

    @telefono.deleter
    def telefono(self):
        del self.__telefono

    @property
    def fecha_nac(self):
        return self.__fecha_nac

    @fecha_nac.setter
    def fecha_nac(self, value):
        self.__fecha_nac = value

    @fecha_nac.deleter
    def fecha_nac(self):
        del self.__fecha_nac

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @email.deleter
    def email(self):
        del self.__email

    def crear_personal(self):
        pass