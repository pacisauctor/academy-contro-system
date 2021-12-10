from collections import namedtuple
import csv
from modelo.Aula import Aula
from modelo.Curso import Curso
from modelo.Edificio import Edificio
from modelo.Matricula import Matricula
from modelo.Profesor import Profesor
from modelo.Programa import Programa
from modelo.TipoProfesor import TipoProfesor
from modelo.Turno import Turno
from modelo.Estudiante import Estudiante


def save_data(filename:str, list_objects:list, clase:str):
    """Guarda datos en un csv en la carpeta database

    Args:
        filename (str): Nombre del archivo a guardar
        list_objects (list): lista de objetos a guardar
        clase (str): Tipo de objeto a guardar
    """
    list_dicctionary = []
    for object in list_objects:
        if clase == "aula":
            list_dicctionary.append(convert_aula_to_dictionary(object=object))
        elif clase == "edificio":
            list_dicctionary.append(convert_aula_to_dictionary(object=object))
        elif clase == "estudiante":
            list_dicctionary.append(convert_aula_to_dictionary(object=object))
        elif clase == "matricula":
            list_dicctionary.append(convert_aula_to_dictionary(object=object))
        elif clase == "profesor":
            list_dicctionary.append(convert_aula_to_dictionary(object=object))
        elif clase == "programa":
            list_dicctionary.append(convert_aula_to_dictionary(object=object))
        elif clase == "tipoprofesor":
            list_dicctionary.append(convert_aula_to_dictionary(object=object))
        elif clase == "curso":
            list_dicctionary.append(convert_aula_to_dictionary(object=object))
        
    keys = list_dicctionary[0].keys()
    
    file_csv= open(filename, "w")
    dict_writer = csv.DictWriter(file_csv, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list_dicctionary)
    file_csv.close()
    
def load_data(filename:str, clase:str) -> list:
    
    file_csv = open(filename, "r")
    dict_reader = csv.DictReader(file_csv)
    list_objects = []
    for row in dict_reader:
        if clase == "aula":
            list_objects.append(convert_dictionary_to_aula(row))
        elif clase == "edificio":
            list_objects.append(convert_dictionary_to_aula(row))
        elif clase == "estudiante":
            list_objects.append(convert_dictionary_to_aula(row))
        elif clase == "matricula":
            list_objects.append(convert_dictionary_to_aula(row))
        elif clase == "profesor":
            list_objects.append(convert_dictionary_to_aula(row))
        elif clase == "programa":
            list_objects.append(convert_dictionary_to_aula(row))
        elif clase == "tipoprofesor":
            list_objects.append(convert_dictionary_to_aula(row))
        elif clase == "curso":
            list_objects.append(convert_dictionary_to_aula(row))
        
    return list_objects
    
    
    
def convert_aula_to_dictionary(object:Aula)->dict:
    return {
        "nombre_aula": object.nombre_aula,
        "numero_piso": object.numero_piso,
        "numero_edificio": object.numero_edificio,
        "capacidad_asientos": object.capacidad_asientos,
        "id_aula": object.id_aula
    }
def convert_dictionary_to_aula(dictionary:dict)->Aula:
    return Aula(
        nombre_aula=dictionary["nombre_aula"],
        numero_piso=dictionary["numero_piso"],
        numero_edificio=dictionary["numero_edificio"],
        capacidad_asientos=dictionary["capacidad_asientos"],
        id_aula=dictionary["id_aula"]
    )