def gestionar():
    pass

def valida_duracion_programa():
    while True:
        anios = int(input('Duracion de la Carrera[años]: '))
        if anios < 4 or anios > 5:
            print('La duracion de la carrera no puede ser menor a 4 o mayor a 5 años')
        else:
            return  anios
