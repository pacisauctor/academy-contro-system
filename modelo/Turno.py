from modelo.TipoProfesor import TipoProfesor


class Turno:

    __cont_turno= 0
    __lst_registros = []

    def __init__(self, turno):
        self.turno = turno
        self.tipoProfesores = [] 
        self.id_turno = Turno.__cont_turno
        self.agrega_turno()
        Turno.__cont_turno += 1

    def __str__(self):
        txt = f'''
        Id Turno: {self.id_turno}
        Turno: {self.turno}
        '''
        return txt
    
    def agregar_tipoProfesor(self, tipoProfesor:TipoProfesor, is_recursive:bool=True):
        if is_recursive:
            tipoProfesor.agregar_turno(self, False)
        self.tipoProfesores.append(tipoProfesor)
    
    def eliminar_tipoProfesor(self, tipoProfesor:TipoProfesor, is_recursive:bool=True)->bool:
        for tipoProfesorIt in self.tipoProfesores:
            if tipoProfesorIt.id_tipo_profesor == tipoProfesor.id_tipo_profesor:
                if is_recursive:
                    tipoProfesor.eliminar_turno(self, False)
                self.tipoProfesores.remove(tipoProfesor)
                return True
        return False
    # metodos de propiedad del argumeto -> turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @turno.deleter
    def turno(self):
        del self.__turno

    def agrega_turno(self):
        """Invocado en el constructor para que cuando se cree el objeto se añade al registro.
        """
        Turno.agregar_registro(self)

    # region Metodos de Clase
    @classmethod
    def mostrar_registros(cls):
        for turno in cls.__lst_registros :
            print(turno.__str__())

    @classmethod
    def agregar_registro(cls, turno):
        cls.__lst_registros.append(turno)
        
    @classmethod
    def ver_detalle(cls):
        cls.mostrar_registros()
        option = int(input("Digite el id del Turno: "))
        turno = cls.__lst_registros[option]
        print(turno.__str__())
        print("Tipos de profesores en este turno: ")
        for tipos_profe in turno.tipoProfesores:
            print(tipos_profe.__str__())
        

    @classmethod
    def edit_turnos(cls):
        cls.mostrar_registros()
        option = int(input("Digite el id del Turno: "))
        for registro in cls.__lst_registros:
            if registro.id_turno == option:
                turno = registro
        nombre = input(f"Nuevo valor de turno (actualmente '{turno.turno}'): ")
        if nombre == "":
            print("Edición cancelada")
        else:
            cls.__lst_registros[option].turno = nombre
            option = input("¿Desea eliminar tipos de profesores en el turno?(Y/N)")
            if option.lower() == "y":
                print("Tipos de profesores en este turno: ")
                for tipos_profe in turno.tipoProfesores:
                    print(tipos_profe.__str__())
                    option = input("¿Desea eliminarlo?(Y/N)")
                    if option.lower() == "y":
                        turno.eliminar_tipoProfesor(tipos_profe)
            option = input("¿Desea agregar un tipo de profesor en el turno?(Y/N)")
            if option.lower() == "y":
                TipoProfesor.listar_registros()
                id_tipo =  int("ID del tipo de profesor: ")
                turno.agregar_tipoProfesor(TipoProfesor.obtener_registro(id_tipo))
                
        
        

    @classmethod
    def delete_turno(cls):
        cls.mostrar_registros()
        option = int(input("Digite el id del Turno: "))
        for registro in cls.__lst_registros:
            if registro.id_turno == option:
                cls.__lst_registros.remove(registro)