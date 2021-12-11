from modelo.Profesor import Profesor


class TipoProfesor:

    __cont_tipo_profesor= 0
    __dicTipoProfesor = {}
    __tipos = ['Ciencias Basicas', 'Ingenierias']

    def __init__(self, tipo):
        TipoProfesor.__cont_tipo_profesor += 1
        self.tipo = tipo
        self.profesores = []
        self.id_tipo_profesor = TipoProfesor.__cont_tipo_profesor

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
    def listar_tipos_profesores(cls):
        profesores_str = ""
        for tip, prof in cls.__dicTipoProfesor:
            profesores_str += (tip + prof.__str__())
        return profesores_str

    @classmethod
    def agregar_tipo_profesor(cls, obj_tipo, obj_profesor):
        idTipo = obj_tipo.id_tipo_profesor
        profesor = obj_profesor
        cls.__dicTipoProfesor[idTipo] = profesor

    @classmethod
    def listar_tipos(cls):
        cont = 1
        for tipo in cls.__tipos:
            print(f'{cont}) {tipo}')
            cont += 1

    @classmethod
    def agregar_tipo(cls, tipo):
        cls.__tipos.append(tipo)

    @classmethod
    def edit_tipo(cls):
        TipoProfesor.listar_tipos()
        op = int(input('[?] Digita tu opcion: '))
        del cls.__tipos[(op-1)]
        newTipo = input('Digita el nuevo tipo: ')
        cls.__tipos.insert((op-1), newTipo)

    @classmethod
    def delete_tipo(cls):
        TipoProfesor.listar_tipos()
        op = int(input('[?] Digita tu opcion: '))
        del cls.__tipos[(op-1)]
    # endregion Metodos de Clase

    def define_tipo(self, obj_profesor):
        print('Establece el tipo de profesor')
        print(
            'Codigo: '+obj_profesor.cod_profesor+'\n'
            +'Profesor: '+obj_profesor.nombre+' '+obj_profesor.apellido
        )
        TipoProfesor.listar_tipos()
        op = int(input('[?] Digita tu opcion: '))
        self.tipo = TipoProfesor.__tipos[(op-1)]

        TipoProfesor.agregar_tipo_profesor(self, obj_profesor)
