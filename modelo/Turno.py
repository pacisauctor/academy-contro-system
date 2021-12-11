from modelo.TipoProfesor import TipoProfesor


class Turno:

    __cont_turno= 0
    dicTurnos = {'1':'07:00-08:45','2':'08:50-10:35'}

    def __init__(self, turno):
        Turno.__cont_turno += 1
        self.turno = turno
        self.tipoProfesores = [] 
        self.id_turno = (len(Turno.dicTurnos) + 1)

    def __str__(self):
        txt = f'''
        Id Turno: {self.id_turno}
        Turno: {self.turno}
        '''
        return txt
    
    def agregar_tipoProfesor(self, tipoProfesor:TipoProfesor):
        self.tipoProfesores.append(tipoProfesor)
    
    def eliminar_tipoProfesor(self, tipoProfesor:TipoProfesor)->bool:
        for tipoProfesorIt in self.tipoProfesores:
            if tipoProfesorIt.id_tipo_profesor == tipoProfesor.id_tipo_profesor:
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
        Turno.add_turno(self.id_turno, self.turno)

    def editar_turno(self):
        Turno.edit_turnos(self.id_turno, self.turno)

    # region Metodos de Clase
    @classmethod
    def listar_turno(cls):
        for key, val in cls.dicTurnos.items():
            print(key+') '+val)

    @classmethod
    def add_turno(cls, clave, turn):
        cls.dicTurnos[str(clave)] = turn

    @classmethod
    def edit_turnos(cls, clave, turn):
        cls.dicTurnos.update({clave: turn})

    @classmethod
    def delete_turnos(cls, clave):
        cls.dicTurnos.pop(clave)
