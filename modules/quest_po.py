import json
from datetime import datetime
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)

##agregar un usuario
def add_user(id = None, username = None, genero = None, edad = None,  fecha = None, correo = None):

    print("Datos de usario")
    print(id, username, genero, edad, fecha, correo)
    print("Capturdo")


    almacenable = {"id": id, "username": username, "genero": genero, "edad": edad, "fecha": fecha, "correo": correo,}
    nombre_de_archivo = f"{username}-{id}-{genero}-{edad}-{fecha}-{correo}.json"
    datos = store_string(
        "user/users",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_user_list(users=None):
    query_result = query_storage(
        "user/users",
    )
    if users is None:
        return query_result["content"]

def get_id_details(id=None):
    query_result = query_storage(
        "user/users",
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
    print("done")

##agregar Pregunta


def Addpre(pre_id=None, user_name=None, tema=None, pregunta=None):
    print("Desde modulo addpre")
    print(pre_id,user_name, tema, pregunta)
    para_almacenar = {"pre_id": pre_id,"user_name": user_name, "tema": tema, "pregunta":pregunta }
    nombre_de_archivo = f"{pre_id}-{pregunta}.json"
    datos = store_string(
        "quest_po/Preguntas",
        nombre_de_archivo,
        json.dumps(para_almacenar)
    )
    return datos

## obtener Pregunta
def get_quest(pregunta=None):
    query_result = query_storage(
        "quest_po/Preguntas",
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
    print("Exito")
##sdsda
