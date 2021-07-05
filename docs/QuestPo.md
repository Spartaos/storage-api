## Descripcion del proyecto
Este proyecto registrara preguntas y respuestas de usuarios con temas relacionados a tecnologias o
materias de tronco comun.

## Estructura deseada

- preguntas (clave_pre, clave_usuario, clave_tema , pregunta)
- respuesta(clave_res,clave_pre, respuesta)

## Operacione de almacenamiento

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
- OST /quest-po/addrespuesta
