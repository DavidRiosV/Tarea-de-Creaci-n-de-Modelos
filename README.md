# Tarea de Creacion de Modelos
Tarea de Creación de Modelos

# Mi tarea debe cumplir
Tarea de Creación de Modelos

## Introducción

A continuación se detalla un escenario de una aplicación Web, dónde los alumnos tendrán que implementar los modelos correspondiente en la aplicación de Django para poder gestionar dicha aplicación y crear las tablas correspondientes en la base de datos.

## Escenario

Este escenario representa una aplicación de gestión de tareas en la que los usuarios pueden crear tareas, asignar tareas a otros usuarios, colaborar en proyectos y agregar etiquetas a las tareas. 

## Modelos
### Usuario:

Nombre: Texto 
Correo Electrónico: Texto y  único
Contraseña: Texto 
Fecha de Registro: Fecha y Hora 

### Tarea:

Título: Texto 
Descripción: Texto Largo
Prioridad: Entero 
Estado : Debe seleccionar las opciones(‘Pendiente’,’Progreso’,’Completada’)
Completada: Booleano 
Fecha de Creación: Fecha 
Hora de Vencimiento: Hora 

### Proyecto:

Nombre: Texto
Descripción: Texto Largo 
Duración Estimada: Float
Fecha de Inicio: Fecha 
Fecha de Finalización: Fecha 

### Etiqueta:

Nombre: Texto y único

### Asignación de Tarea:

Observaciones: Texto largo
Fecha de Asignación : Fecha y Hora

### Comentario:

Contenido: Texto Largo
Fecha de Comentario: Fecha y Hora

## Relaciones

### Usuario:

Relación con Proyecto (Proyectos Asignados): Un usuario puede estar asignado a varios proyectos como colaborador. Y un proyecto puede tener varios usuarios.

### Proyecto:

Relación con Usuario (Creador): Un proyecto tiene un usuario que lo crea o administra. 

### Tarea:

Relación con Usuario (Creador): Muchas tareas pueden ser creadas por un usuario. 

Relación con usuarios(usuarios asignados): Una tarea puede tener asignado uno o más usuarios y un usuario puede estar en varias tareas, por lo tanto vamos a relacionarlos a través de una tabla intermedia Asignación de Tarea.

Relación con Etiqueta (Etiquetas Asociadas): Una tarea puede tener varias etiquetas. Y una etiqueta puede estar asignada a varias tareas.

Relación con Proyecto (proyecto): Un proyecto tiene varias tareas creadas, para desarrollar el proyecto.

### Comentario:

Relación con Usuario (Autor): Cada comentario tiene un autor (usuario). 

Relación con Tarea: Cada comentario está asociado a una tarea. 

## Crear Datos
Debe incluir datos de ejemplo en la base de datos por parte de la administración para comprobar que todo es correcto.

Deben incluirse 30 datos en cada tabla, por lo tanto estaría bien usar el Seeder para generar estos datos.

## Fixtures
Debe realizarse una copia de seguridad de los datos con el fixture.
