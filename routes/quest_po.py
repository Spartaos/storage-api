import json
from time import time
import bottle
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord
from modules.quest_po import add_a_quest
from modules.quest_po import reg_respuesta


app = BottleJson()


@app.post("/")
@app.get("/")
## agregar pregunta
##$ curl http://localhost:8080/quest_po/addquest -X POST -H 'content-Type: application/json' -d '{"clave_pre":"212","clave_Usuario": "unis","pregunta": "Que son las TICS?", "clave_tema" : "TICS"}'


@app.post("/addquest")
def addquest(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        clave_pre = str(payload['clave_pre'])
        clave_usuario = str(payload['clave_usuario'])
        pregunta = str(payload['pregunta'])
        datetime = str(payload['datetime'])
        clave_tema = str(payload['clave_tema'])
        if len(clave_usuario) == 0:
            raise Exception()
        # Validacion de fecha
        year, month, date = [int(x) for x in
        datetime.split("-")]
        print("Datos validos")
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(501)

##ver preguntas
#curl http://localhost:8080/vg_info/list -X GET
@app.get("/list")
def get_quest(*args, **kwargs):
    try:
       respuesta = add_a_quest()
    except:
        raise bottle.HTTPError(500, "Error interno")
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
