from os import environ, urandom
import hashlib
import datetime
from bottle import response, request
import jwt
import binascii
from functools import wraps
import models.auth as mauth

import json

from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)

def add_a_quest(clave_pre=None, clave_usuario=None, pregunta=None, datetime=None, clave_tema=None):
    print("almacenado en add_a_quest")
    print(clave_pre, pregunta, clave_tema)
    datos_almacenados = {"clave_pre": clave_pre,"pregunta": pregunta, "datetime": datetime, "clave_tema":clave_tema }
    nombr_de_archivo = f"{clave_pre}-{pregunta}.json"
    datos = store_string(
        "quest_po/Carpeta1",
        nombr_de_archivo,
        json.dumps(datos_almacenados)
    )
    return "Exito"

def get_user_list(pregunta=None):
    query_result = query_storage(
        "pregunta/preguntas",
    )
    if preguntas is None:
        return query_result["content"]

def reg_respuesta(clave_pre=None, clave_usuario=None, datetime=None,respuesta=None, clave_tema=None):
    print("Guardar en reg_respuesta")
    print(respuesta)
    para_almacenar = {"clave_usuario": clave_usuario,"respuesta": respuesta, "datetime": datetime, "clave_tema":clave_tema }
    json_text = json.dumps(datos_almacenados)
    store_string('rescarpeta', respuesta, datos_almacenados)
    return "Exito"

def get_quest_list(clave_pre=None):
    query_result = query_storage(
        "quest_po/Carpeta",
    )
    if clave_pre is  None:
        return query_result["content"]
