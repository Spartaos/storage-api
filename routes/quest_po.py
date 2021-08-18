import json
import datetime as dt
from time import time
import bottle
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord
from modules.quest_po import add_user
from modules.quest_po import get_user_list
from modules.quest_po import Addpre
from modules.quest_po import get_quest
from modules.quest_po import get_pre
from modules.quest_po import add_res
from modules.quest_po import get_ress



app = BottleJson()



## agregar un Usuario curl http://localhost:8080/quest_po/add_user  -X POST -H 'Content-Type: application/json'  -d '{"id" : "12" , "username" : "Oscar" , "genero" : "hombre" , "edad" : "23" , "fecha":"2021-10-10" , "correo" : "test@hotmail.com"}'
@app.post("/add_user")
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
        print("Datos incorrectos")
        raise bottle.HTTPError(405, "Datos invalidos")
    raise bottle.HTTPError(201, "Usuario agregado")

##Lista de usuarios
# curl http://localhost:8080/quest_po/list -X GET
@app.get("/listuser")
def get_all_info(*args, **kwargs):
    try:
       respuesta = get_user_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

##Agregar Pregunta
##curl http://localhost:8080/quest_po/newq -X POST -H 'content-Type: application/json' -d  '{"pre_id":"Q012","user_name": "useer1","tema": "Tics", "pregunta" : "pregunta2", "fecha":"2021-10-10"}'


@app.post("/newq")
def newq(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        pre_id = str(payload['pre_id'])
        user_name = str(payload['user_name'])
        tema = str(payload['tema'])
        pregunta = str(payload['pregunta'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        print("Datos validos")
        respuesta = Addpre(**payload)

    except:
        print("Datos invalidos")
        raise bottle.HTTPError(405, "Datos invalidos")
    raise bottle.HTTPError(201, "Pregunta agregada")
##ver preguntas
# curl http://localhost:8080/quest_po/listq -X GET
@app.get("/listq")
def get_all_quest(*args, **kwargs):
    try:
       respuesta = get_quest()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

##Ver pregunta por ID
#curl http://localhost:8080/quest_po/Q003/getidq -X GET


@app.get("/<pre_id>/getidq")
def get_pre_id(*args, pre_id=None, **kwargs):
    try:
        respuesta = get_pre(pre_id = pre_id)
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

    ##Agregar respuestas
##curl http://localhost:8080/quest_po/Q003/addres -X POST -H 'Content-Type: application/json' -d '{"pre_id":"Q003","res_id":"R001","respuesta": "respuesta1","fecha": "2021-08-12"}'

@app.post("/<pre_id>/addres")
def addres(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        pre_id = str(payload['pre_id'])
        res_id = str(payload['res_id'])
        respuesta = str(payload['respuesta'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        print("Datos validos")
        respuesta = add_res(**payload)

    except:
        print("Datos invalidos")
        raise bottle.HTTPError(405, "Datos invalidos")
    raise bottle.HTTPError(201, "Respuesta agregada correctamente")

    ##Ver Respuestas
    ##curl http://localhost:8080/quest_po/listres -X GET

@app.get("/listres")
def get_all_res(*args, **kwargs):
    try:
       respuesta = get_ress()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)


    ##Ver pregunta por ID
    #curl http://localhost:8080/quest_po/R001/getidq -X GET


    @app.get("/<res_id>/getass")
    def get_res_id(*args, res_id=None, **kwargs):
        try:
            respuesta = get_res(res_id = res_id)
        except:
            raise bottle.HTTPError(500, "Error interno")
        raise bottle.HTTPError(200, respuesta)
