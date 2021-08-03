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

## Add a user
@app.post("/questpo/addUser")
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

## agregar pregunta
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
