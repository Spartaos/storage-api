import json
from time import time
import bottle
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord
from modules.quest_po import add_user
from modules.quest_po import get_user_list
from modules.quest_po import get_id_details
from modules.quest_po import add_quest
from modules.quest_po import get_preguntas
from modules.quest_po import add_answer
from modules.quest_po import get_answers


app = BottleJson()


@app.post("/store")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id = str(payload['id'])
        username = str(payload['username'])
        genero = str(payload['genero'])
        edad = str(payload['edad'])
        correo = str(payload['correo'])
        print("Datos Aceptados")
        respuesta = add_user(**payload)
        print(respuesta)
        print("Almost done")
    except:
        print("Datos incorrecros")
        raise bottle.HTTPError(405, "datos invalidos")
    raise bottle.HTTPError(201, "Usuario agregado")
## agregar pregunta

# curl http://localhost:8080/quest_po/list -X GET
@app.get("/list")
def get_all_info(*args, **kwargs):
    try:
       respuesta = get_user_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

##$ curl http://localhost:8080/quest_po/1/addpregunta -X POST -H 'content-Type: application/json' -d '{"clave_pre":"212","clave_Usuario": "unis","pregunta": "Que son las TICS?", "clave_tema" : "TICS"}'

@app.post("/addsquest")
def add_quest(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        clave_pre = str(payload['clave_pre'])
        clave_usuario = str(payload['clave_usuario'])
        pregunta = str(payload['pregunta'])
        print("Datos Aceptados")
        respuesta = add_quest(**payload)
        print(respuesta)
        print("Almost done")
    except:
        print("Datos incorrecros")
        raise bottle.HTTPError(405, "datos invalidos")
    raise bottle.HTTPError(201, "Usuario agregado")

@app.post("/addpregunta")
def bar(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        clave_pre = str(payload['clave_pre'])
        clave_usuario = str(payload['clave_usuario'])
        pregunta = str(payload['pregunta'])
        clave_tema = str(payload['clave_tema'])
        print("Datos validos")
        pregunta = add_quest(**payload)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400, "Datos invalidos")
    raise bottle.HTTPError(201, "Creaste una nueva pregunta")

##ver preguntas
# curl http://localhost:8080/quest_po/list -X GET
@app.get("/list")
def get_all_info(*args, **kwargs):
    try:
       respuesta = get_user_list()
    except:
        raise bottle.HTTPError(501, "Error interno")
    raise bottle.HTTPError(200, respuesta)

## Add a user
@app.post("/addUser")
def add_a_user(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    print("holamundo")
    return dict(code=501, message="Not implemented")

## Get user info
@app.get("/questpo/addUser/<name_id>")
def get_user(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")


@app.post("POST /quest-po/addquestion")
def add_a_quest(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get question  List
@app.get("/questpo/list")
def get_quest_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get muestra la informacion de la respuesta
@app.get("/quest-po/<respuesta_id>")
def get_a_videogame(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")
