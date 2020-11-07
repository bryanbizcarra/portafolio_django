from django.contrib import admin

# Register your models here.
from .models import informacion_personal, conocimientos, trayectoria_academica, trayectoria_laboral

admin.site.register(informacion_personal)
admin.site.register(conocimientos)
admin.site.register(trayectoria_academica)
admin.site.register(trayectoria_laboral)