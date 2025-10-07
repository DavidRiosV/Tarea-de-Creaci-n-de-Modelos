from django.contrib import admin
from .models import Usuario
from .models import Tarea
from .models import Proyecto
from .models import Etiqueta
from .models import AsignacionTarea
from .models import Comentario

admin.site.register(Usuario)
admin.site.register(Tarea)
admin.site.register(Proyecto)
admin.site.register(Etiqueta)
admin.site.register(AsignacionTarea)   
admin.site.register(Comentario)  