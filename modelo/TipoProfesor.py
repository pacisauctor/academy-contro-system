from modelo.Profesor import Profesor


class TipoProfesor:

    __cont_tipo_profesor= 0
    __ls_registros = []

    def __init__(self, tipo):
        self.tipo = tipo
        self.profesores = []
        self.turnos = []
        self.id_tipo_profesor = TipoProfesor.__cont_tipo_profesor
        TipoProfesor.__cont_tipo_profesor += 1

    def __str__(self):
        txt = f'''
        Id Tipo Profesor: {self.id_tipo_profesor}
        Tipo de Profesor: {self.tipo}
        '''
        return txt
# metodos de propiedad del argumeto -> tipo
               
    def agregar_profesor(self, profesor:Profesor):
        self.profesores.append(profesor)
    
    def eliminar_profesor(self, profesor:Profesor) -> bool:
        for profesor_it in self.profesores:
            if profesor_it.id_profesor == profesor.id_profesor:
                self.profesores.remove(profesor_it)
                return True
        return 
    
    def agregar_turno(self, turno, is_recursive:bool=True):
        if is_recursive:
            turno.agregar_tipoProfesor(self, False)
        self.turnos.append(turno)
    
    def eliminar_turno(self, turno, is_recursive:bool = True) -> bool:
        """Elimina el turno relacionado al tipo de profesor

        Args:
            turno
            is_recursive (bool): Si queremos que se elimine la otra relación, ponemos True

        Returns:
            bool: Si todo ta bien, ta bien
        """
        for turno_it in self.turnoes:
            if turno_it.id_turno == turno.id_turno:
                if is_recursive:
                    turno_it.eliminar_tipoProfesor(self, False)
                self.turnos.remove(turno_it)
                return True
        return False
        
    @property
    def tipo(self):
        return self.__tipo
                                
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
                                
    @tipo.deleter
    def tipo(self):
        del self.__tipo

    # region Metodos de Clase
    @classmethod
    def listar_registros(cls):
        
        for registro in cls.__ls_registros:
            print(registro.__str__())


    @classmethod
    def agregar_registro(cls):
        tipo = input("Escriba el tipo de profesor:")
        tipo_obj = TipoProfesor(tipo)
        cls.__ls_registros.append(tipo_obj)

    @classmethod
    def listar_registros(cls):
        for tipo in cls.__ls_registros:
            print(tipo.__str__())
            
    @classmethod
    def detalle_registro(cls):
        TipoProfesor.listar_registros()
        op = int(input('[?] Digita tu opcion: '))
        tipo_profesor = cls.__ls_registros[op]
        print(tipo_profesor.__str__())
        print("Turnos: ")
        for turno in tipo_profesor.turnos:
            print(turno.__str__())
        print("Profesor: ")
        for profesor in tipo_profesor.profesores:
            print(profesor.__str__())
            
    @classmethod
    def agregar_tipoProfesor(cls,  id_tipo_profesor:int):
        for registro in cls.__ls_registros:
            if registro.id_tipo_profesor == id_tipo_profesor:
                return registro
        return None

    @classmethod
    def editar_registro(cls):
        TipoProfesor.listar_registros()
        op = int(input('[?] Digita tu opcion: '))
        newTipo = input('Digita el nuevo tipo: ')
        for registro in TipoProfesor.__ls_registros:
            if registro.id_tipo_profesor == op:
                registro.tipo=newTipo

    @classmethod
    def eliminar_registro(cls):
        TipoProfesor.listar_registros()
        op = int(input('[?] Digita tu opcion: '))
        for registro in TipoProfesor.__ls_registros:
            if registro.id_tipo_profesor == op:
                cls.__ls_registros.remove(registro)
                
    @classmethod
    def obtener_registro(cls, id_tipo):
        for registro in TipoProfesor.__ls_registros:
            if registro.id_tipo_profesor == id_tipo:
                return registro
            
        return None        
    # endregion Metodos de Clase


