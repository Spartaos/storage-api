## Descripcion del proyecto
Este proyecto registrara preguntas y respuestas de usuarios con temas relacionados a tecnologias actuales.

## Estructura deseada

- Usuario (clave_user,user_name,password)
- preguntas (clave_pre, clave_usuario, pregunta)
- respuesta(clave_res,clave_pre, respuesta)

## APIz

| Path                  | Descripción |
| --------------------- | ----------- |
| /Quest-Po/consult           | Se podran consultar las preguntas almacenadas con su numero            |
| /Quest-Po/consult/<clave_pre>           | Se podran consultar las preguntas almacenadas con una palabra clave            |
| /Quest-Po/consult/<clave_usuario>       | Se mostraran las preguntas de un creador en espesifico           |
| /Quest-Po/creator/       | Se mostraran los creadores de las preguntas           |

## Operaciones de Almacenamiento de datos

### Operaciones de Usuario
#### Registrar un usuarios
> Solicitamos Usuario y contraseña
