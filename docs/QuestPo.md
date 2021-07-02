## Descripcion del proyecto
Este proyecto registrara preguntas y respuestas de usuarios con temas relacionados a tecnologias o
materias de tronco comun.

## Estructura deseada

- Usuario (clave_user,user_name,password)
- tema (clave_tema)
- preguntas (clave_pre, clave_usuario, clave_tema , pregunta)
- respuesta(clave_res,clave_pre, respuesta)

## API's

### Registro de usuarios
- Se solicita un nombre de usurario y contraseña


| Path                  | Descripción |
| --------------------- | ----------- |
| /Quest-Po/login       |             |
| /Quest-Po/Buscar      | Se podran consultar las preguntas almacenadas con una palabra clave                     |
| /Quest-Po/consult/    | Se mostraran las preguntas de un creador en espesifico                            |
| /Quest-Po/creator/    | Se mostraran los creadores de las preguntas                             |

## Operaciones de Almacenamiento de datos
### Realizacion de creacion  
> Crear una pregunta
- Solicitar Tema relacionado
- Solicitar creacion de preguntas
- El identificador clave de la pregunta sera autoasignada

> Crear una respuesta
- Solicitar clave de pregunta
- Solicitar respuesta

### Operaciones de usurio
 - Registrar usuario
 - Realizar busqueda de temas de interes
 - Realizar creacion de preguntas
 - Realizar creacion de respuestas
 
