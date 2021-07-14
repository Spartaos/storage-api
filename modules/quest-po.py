from os import environ, urandom
import hashlib
import datetime
from bottle import response, request
import jwt
import binascii
from functools import wraps
import models.auth as mauth

questions = []
def add_a_quest(clave_pre, clave_usuario, datetime, clave_tema):
    Questions = {
        "clave_pre": clave_pre,
        "Usuario": clave_usuario,
        "Datetime": datetime,
        "Tema": tema,

    }
    questions.append(questions)
    return json.dumps(questions)

respuesta = []
def add_a_respuesta(clave_pre, clave_usuario, datetime, clave_tema):
    Respuesta = {
        "clave_pre": clave_pre,
        "Usuario": clave_usuario,
        "Datetime": datetime,
        "Tema": tema,

    }
    respuesta.append(respuesta)
    return json.dumps(respuesta)
