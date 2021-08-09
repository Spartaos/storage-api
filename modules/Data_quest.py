import json
from datetime import datetime
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)

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


def add_quest(clave_pre=None, clave_usuario=None, pregunta=None, datetime=None, clave_tema=None):
    print("Datos de Pregunta")
    print(clave_pre, clave_usuario pregunta, clave_tema)
    print("Exito")

    datos_almacenados = {"clave_pre": clave_pre,"pregunta": pregunta, "datetime": datetime, "clave_tema":clave_tema }
    nombre_de_archivo = f"{pregunta}-{clave_pre}-{clave_usuario}.json"
    datos = store_string(
        "pregunta/preguntas",
        nombre_de_archivo,
        json.dumps(datos_almacenados)
    )
    return datos

def get_preguntas( clave_pre= None, pregunta = None):
    query_result = query_storage(
        "pregunta/preguntas",
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
        print("Respuesta")
    if encuesta is not None:
        return [
           r
           for r in query_result["content"]
           if encuesta in r
        ]
        print("respuesta")


def add_answer(clave_pre=None, clave_usuario=None, datetime=None,respuesta=None, clave_tema=None):
    print("Respuesta guardada")
    print(respuesta)
    print("Exito")

    datos_almacenados = {"clave_usuario": clave_usuario,"respuesta": respuesta, "datetime": datetime, "clave_tema":clave_tema }
    nombre_de_archivo = f"{respuesta}-{clave_usuario}.json"
    datos = store_string(
        "pregunta/respuestas",
        nombre_de_archivo,
        json.dumps(datos_almacenados)
    )
    return datos

def get_answers(clave_pre=None, clave_usuario=None, datetime=None,respuesta=None, clave_tema=None):
    query_result = query_storage(
        "pregunta/respuestas",
    )
    if id is not None:
        return [
           r
           for r in query_result["content"]
           if id in r
        ]
    print("Exito")
