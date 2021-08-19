# Descripcion del proyecto
Este proyecto plantea la idea de un tipo bloc de preguntas y respuestas de diferentes temas relevantes, para asi poder contar con una libreria de preguntas comunes en las que se puedan apoyar y asi comparar respuestas entre los usuarios y formular sus propias respuestas en base a las respuestas de otros usuarios sin alejarse le la respuesta correcta.

## Entidades

Las entidades en mente para este proyecto son las siguientes:

- Usuario (id_user,Nombre ,password,fecha_nac)
- preguntas (clave_pre, pregunta, clave_usuario, datetime, clave_tema)
- respuesta(clave_res,clave_pre, respuesta)


### API

| | Path                  | Descripción |
|---------| --------------------- | ----------- |
|POST| /quest-po/add_user| Registro de un usuario |
|GET| /quest-po/listuser| Solicitar usuarios existentes |
|POST| /quest_po/newq | Agregar pregunta |
|GET| /quest_po/listq| Ver preguntas |
|GET| /quest_po/<pre_id>/getidq/ | Ver preguntas por id |
|POST| /quest_po/pre_id/addres | Agregado de Respuestas |
|GET| /quest_po/listres | Ver respuestas |




## Operaciones de usurio
 - Registrar usuario
 - Realizar creacion de preguntas
 - Realizar creacion de respuestas

## Registro de usuarios
 - Se solicita un nombre de usurario y contraseña

## Realizar una preguntas
- realizar una pregunta
- la clave de la pregunta se realizara automaticamente

### Estructuras de Solicitud y Respuestas


## Registro de una pregunta de manera exitosa
```
    {
      "pre_id":"Q012",
      "user_name": "useer1",
      "tema": "Tics",
      "pregunta" : "pregunta2",
      "fecha":"2021-10-10"
    }
```

## Mensaje de fallo

```
{
          "Code": "500",
          "mesagge": "Error al capturar la pregunta"
    }
```         

## Registro  de respuestas            
```
{
          pre_id":"Q003",
          "res_id":"R001",
          "respuesta": "respuesta1",
          "fecha": "2021-08-12""


}
```

## Mensaje de fallo            
```
{
          "Code": "500",
          "mesagge": "Error al capturar de respuesta"

}
```

## Interaccion con el servidor


`GET  /quest_po/listuser`

- 200 regresa la informacion de un usuario
- 500, regresa mensaje de fallo

`POST /quest_po/newq`

- Recibe la pregunta    
- 201, Registra los datos de la pregunta
- 500, regresa estructura de mensaje de fallo     

`GET  /quest_po/listq`

- 200 Regresa una lista de preguntas de los usurios
- 500, regresa mensaje de fallo   

`GET  /quest_po/<pre_id>`

- 201, Muestra preguntas por Id
- 500, regresa mensaje de fallo  


`POST /quest_po/<pre_id>/addres`
- 201, Registra las respuestas a las preguntas
- 500, regresa mensaje de fallo  

`GET  /quest_po/listres`

- 201, Muestra las respuestas a las preguntas
- 500, regresa mensaje de fallo  

## Casos de uso

### Agregado de Usuario

El usuario puede agregar un  perfil tomando en cuenta el username, genero, correo, edad y el Id
```
curl http://localhost:8080/quest_po/add_user  -X POST -H 'Content-Type: application/json'  -d '{"id" : "20" , "username" : "Oscar" , "genero" : "hombre" , "edad" : "23" , "fecha":"2021-10-10" , "correo" : "test@hotmail.com"}'

```
### Agregado de Preguntas

Si un usuario desea agregar una pregunta es necesario contar con el Id

```
curl http://localhost:8080/quest_po/newq -X POST -H 'content-Type: application/json' -d  '{"pre_id":"Q020","user_name": "useer1","tema": "Tics", "pregunta" : "pregunta2", "fecha":"2021-10-10"}'
```
### Consulta de las preguntas
El Usuario puede consultar las preguntas realizadas de todos los demas usuarios

```
curl http://localhost:8080/quest_po/listq -X GET
```
### Consultas de las preguntas por Id
El usuario puede consultar las preguntas por Id
```
curl http://localhost:8080/quest_po/Q003/getidq -X GET
```
### Agregado de Respuestas
El usuario puee agregar Respuestas considerando el Id de la pregunta a la que desea contestar
```
curl http://localhost:8080/quest_po/Q003/addres -X POST -H 'Content-Type: application/json' -d '{"pre_id":"Q020","res_id":"R020","respuesta": "respuesta1","fecha": "2021-08-12"}'

```
### Mostrar Respuestas
El usuario puede mostrar respuestas de las preguntas realizadas
```
curl http://localhost:8080/quest_po/listres -X GET

```


## Documentacion para continuacion del proyecto
Al finalizar el codigo, se puede llegar que el proyecto pude ofrecer mas areas de oportunidad para desarrollo del mismo de manera que se puedan agregar mas funciones tales como:

- Funcion para editar las preguntas de los usuarios.
- Funcion para eliminar preguntas de los usuarios
- Funcion para la busqueda de preguntas con sus respuestas por medio de Id
- Funcion para la edicion de respuestas de los usuarios
- Funciones para que los usuarios puedan editar las respuestas de los usuarios
- Funcion para busqueda por temas de las Preguntas
- Funcion para la busqueda de preguntas por tema

Otro de los objetivos del proyecto fue la falta de mas desarrollo del Front-end para una mejor vision de como se quiere realizar el proyecto visualmente

-----------------------------------------------------------------------


## Computo en la nube

### Creacion de fork en storage-api

* Entregable : Señalar cual es el commit-has, a partir del que se realizo el fork

| Descripcion | Commit hash |                    
|----------------|-------------------------------|
|  Creacion de Fork  | 611e82fc76fa90423ddde10f12ebe3028d1e3cbd         |

Crear los archivos correspondientes a su proyecto, y someterlos a control de versiones
- Entregable, señalar el commit-hash que contiene la creación de dichos archivos.–Archivos en./docs,./routes,./modules,./models, nombrados con el slug de su proyecto.
- NOTA: dentro de docs son archivos tipo markdown (.md), y dentro de las demás son archivos tipo python(.py)

|Descripcion                |Commit hash                          
|----------------|-------------------------------|
| Creacion de /Quest-Po  | 611e82fc76fa90423ddde10f12ebe3028d1e3cbd|   


Crear todas las rutas especificadas en su archivo de documentación dentro de su archivo en la carpeta routes, y todas deben de responder 501, con Content-Type: application/json, y un cuerpo de respuesta en formato json con 2 llaves,code y message, el message debe contener el mensaje, Not Implemented.
- Entregable, señalar el commit-hash que contiene la codificacion de las rutas.

|Descripcion                |Commit hash                          
|----------------|-------------------------------|
| Creacion de questpo.py | |    959284a3fbb618af04b39fbc8f8d129aea1b3ffc
