# Descripcion del proyecto
Este proyecto registrara preguntas y respuestas de usuarios con temas relacionados a tecnologias o
materias de tronco comun.

## Entidades

Las entidades en mente para estre proyecto son las siguientes:
- Usuario (id_user,Nombre ,fecha_nac, email)
- preguntas (clave_pre, clave_usuario, datetime, clave_tema)
- respuesta(clave_res,clave_pre, respuesta)
- tema (clave_tema)


### Crear una respuesta
- Solicitar palabra clave de pregunta

### Operaciones de usurio
 - Registrar usuario
 - Realizar creacion de preguntas
 - Realizar creacion de respuestas

### Registro de usuarios
 - Se solicita un nombre de usurario y contraseña

## Estuctura de solicitud y respuesta
### Registro de un usuario

```
{
    "usuario": "userimio",
    "password": "tumundouser"
}
```
### Busqueda de preguntas por keyword
```
    {
      keyword: "keyword",
      question:[
          {
            id:2, question: "Esta es unapregunta"
          },
          {
            id:3, qustion: "Esta es otra pregunta"
          },
      ]

    }
```

### registos de  pregunta

```
{
  question:{
      question_id:<question_id>
      user_id
      question:"pregunta??"
      datetime: "xxxx-xx-xxTxx-xx"
      keyword:[
      "tegnologia","biologia","artes musicales"
      ]
  }
}
```         

### registros de respuestas            
```
{
  respuesta:{
      respuesta_id:<respuesta_id>
      respuesta: "respuesta"
      datetime: "xxxx-xx-xxTxx-xx"
      question_id:<keyword>

      ]
  }
}
```
### Solicitar lista de preguntas por keyword
| Path                  | Descripción |
| --------------------- | ----------- |
| /Quest-Po/list/<keyword>     |       Solicitar una lista de preguntas por keyword      |
| /Quest-Po/user/<user_id>|Solicitar informacion del usuario con id user_id, en el se incluyen sus preguntas realizadas|
| /Quest-Po/question/<question_id>|Solicitar pregunta con id question_id|
| /Quest_Po/addquestion |Agregar pregunta|


## Archivo principal y ruta de almacenamiento

- GET /quest_po/question
- GET /quest-po/user
- GET /quest_po/list
- POST /quest-po/addquestion
- POST /quest-po/addrespuesta


# Documento de plan de implementacion

## Aspecto general

Se a planteado este proyecto para la creacion de preguntas y respuestas entre usuarios, con un estilo foro en el cual se podran conocer los diferentes puntos de vista de los usuarios, asi de esta manera contando con una comunidad colaborativa en la que podramos consultar ideas nuevas en base a respuestas.

### Recursos
Principalmente la realizacion de este proyecto es necesario tener conocimientos en programacion web, conocer estructuras html, base de datos, codigo en lenguaje Json, etc.
Un equipo adecuado para la elaboracion y diseño.

### Al finalizar el proyecto

Una vez la idea implementada y con u optimo funcionamineto, es de alta relevancia el mantener un monitoreo adecuado a la plataforma , de esta manera contar con aportes legitimos y utiles a la plataforma.


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

Crear en su carpeta de modulos funciones que emulen las interacciones con el almacén de archivos o datos, es decir que si necesitas una función de consulta, crear una función que retorne una consulta simulada con datos codificados como constantes, y si necesitas crear objetos funciones que retornen simulando una creación exitosa.

- Entregable, señalar el commit-hash que contiene la codificacion de estas funciones asistentes.


| Descripcion               |Commit hash                          
|----------------|-------------------------------|
|  |  |
