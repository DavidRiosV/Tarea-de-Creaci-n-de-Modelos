from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    contraseña = models.CharField(max_length=100)
    fecha_de_registro = models.DateTimeField(default=timezone.now)
    
    proyectos_asignados = models.ManyToManyField('Proyecto',related_name='colaboradores',blank=True)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()

    creador = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='proyectos_creados')

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField(default=timezone.now)
    hora_vencimiento = models.TimeField(null=True, blank=True)
    
    creador = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='tareas_creadas')
    proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE,related_name='tareas')
    etiquetas = models.ManyToManyField(Etiqueta,related_name='tareas',blank=True)
    usuarios_asignados = models.ManyToManyField(Usuario,through='AsignacionTarea',related_name='tareas_asignadas')

    def __str__(self):
        return self.titulo

class AsignacionTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True)
    fecha_asignacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.usuario.nombre} → {self.tarea.titulo}"

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)

    autor = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='comentarios')
    tarea = models.ForeignKey(Tarea,on_delete=models.CASCADE,related_name='comentarios')

    def __str__(self):
        return f"Comentario de {self.autor.nombre} en {self.tarea.titulo}"
