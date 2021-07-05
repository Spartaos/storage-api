## Descripcion del proyecto
Este proyecto registrara preguntas y respuestas de usuarios con temas relacionados a tecnologias o
materias de tronco comun.

## Estructura deseada

- preguntas (clave_pre, clave_usuario, clave_tema , pregunta)
- respuesta(clave_res,clave_pre, respuesta)

## Operacione de almacenamiento
###Solicitar lista de preguntas por keyword
| Path                  | Descripción |
| --------------------- | ----------- |
| /Quest-Po/list/<keyword>     |       Solicitar una lista de preguntas por keyword      |
| /Quest-Po/user/<user_id>|Solicitar informacion del usuario con id user_id, en el se incluyen sus preguntas realizadas|
| /Quest-PO/question/<question_id>|Solicitar pregunta con id question_id|


> Crear una respuesta
- Solicitar clave de pregunta
- Solicitar respuesta

### Operaciones de usurio
 - Registrar usuario
 - Realizar busqueda de temas de interes
 - Realizar creacion de preguntas
 - Realizar creacion de respuestas
 ### Registro de usuarios
 - Se solicita un nombre de usurario y contraseña


                           
