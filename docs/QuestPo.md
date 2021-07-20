<<<<<<< HEAD
# Descripcion del proyecto
Este proyecto plantea la idea de un tipo bloc de preguntas y respuestas de diferentes temas relevantes, para asi poder contar con una libreria de preguntas comunes en las que se puedan apoyar y asi comparar respuestas entre los usuarios y formular sus propias respuestas en base a las respuestas de otros usuarios sin alejarse le la respuesta correcta.

## Entidades

Las entidades en mente para este proyecto son las siguientes:

- Usuario (id_user,Nombre ,password,fecha_nac)
- preguntas (clave_pre, pregunta, clave_usuario, datetime, clave_tema)
- respuesta(clave_res,clave_pre, respuesta)
- tema (clave_tema, tema)

### API

| Path                  | Descripción |
| --------------------- | ----------- |
| /Quest-Po/user/<user_id>|Solicitar informacion del usuario con id user_id, en el se incluyen sus preguntas realizadas|
| /Quest-Po/question/<question_id>|Solicitar pregunta con id question_id|
| /Quest_Po/add_a_quest |Agregar pregunta|
| /Quest_Po/addrespuesta/<clave_res>|Agregar una respuesta|
|/Quest_Po/userinfo/|Ver la informacion de los usuarios|

###  Operaciones de Almacenamiento de datos


## Operaciones de usurio
 - Registrar usuario
 - Realizar creacion de preguntas
 - Realizar creacion de respuestas

## Registro de usuarios
 - Se solicita un nombre de usurario y contraseña

## Realizar una preguntas
- realizar una pregunta
- la clave de la pregunta se realizara automaticamente

### Estuctura de solicitud y respuesta

## Registro de un usuario

```
{
    "usuario": "clarkken99",
    "password": "tumundouser"
}
```
## Registro de una pregunta de manera exitosa
```
    {
      "clave_pre" : "Que es la paravirtualizacion?"
      "datetime" : "XX-XX-XXXXHXX:XX:XX"
      "Tema" : "Servidores"
    }
```

## Mensaje de fallo

```
{
          "Code": "500",
          "mesagge": "Error al capturar la pregunta"
    }
```         

## Mensaje de respuestas            
```
{
          "Respuesta": "El uso de varias capas de virtualizacion"
          "Tema": "Servidores"


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


`GET  /quest_po/User/<name_id>`

- 200 regresa la informacion de un usuario
- D.O.M, regresa mensaje de fallo

`POST /quest_po/add_a_quest`

- Recibe la pregunta    
- 201, Registra los datos de la pregunta
- D.O.M, regresa estructura de mensaje de fallo     

`GET  /quest_po/<keywords>`

- 200 Regresa una lista de preguntas de los usurios
- D.O.M, regresa mensaje de fallo   

`GET  /quest_po/<question_id>`

- 201, muetra la informacion de las preguntas echas
- D.O.M, regresa mensaje de fallo  


`POST /quest_po/addrespuesta`
- 201, Registra las respuestas a las preguntas
- D.O.M, regresa mensaje de fallo  

`GET  /quest_po/<respuesta_id>`

- 201, Muestra las respuestas a las preguntas
- D.O.M, regresa mensaje de fallo  




### Computo en la nube

## Creacion de fork en storage-api

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
=======
<h1>Descripcion del proyecto</h1>
<<<<<<< HEAD
>>>>>>> 445c008 (actualzacion)
=======
Este proyecto registrara preguntas y respuestas de usuarios con temas relacionados a tecnologias actuales.

## API

| Path                  | Descripción |
| --------------------- | ----------- |
| /Quest-Po/consult           | Se podran consultar las notas almacenadas con su nombre            |
| /Quest-Po/consult/<key>           | Se podran consultar las notas almacenadas con una palabra clave            |
| /Quest-Po/consult/<creator>       | Se mostraran las notas de un creador en espesifico           |
| /Quest-Po/creator/       | Se mostraran los creadores de notas           |
>>>>>>> e6aec3e (Actualizacion de documento de proyecto)
