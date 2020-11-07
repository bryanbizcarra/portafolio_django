from django.db import models

# Create your models here.
class informacion_personal(models.Model):
    nombre = models.CharField(max_length=150)
    nacimiento = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    cuidad = models.CharField(max_length=50)
    edad = models.IntegerField()
    cargo_actual = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class conocimientos(models.Model):
    nombre_conocimiento = models.CharField(max_length=100)
    porcentaje_conocimiento = models.IntegerField()

class trayectoria_academica(models.Model):
    tipo_trayectoria = models.CharField(max_length=100)
    ano_inicio = models.CharField(max_length=20)
    ano_termino= models.CharField(max_length=20)
    nombre_institucion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, null = True, blank = True)

class trayectoria_laboral(models.Model):
    tipo_trayectoria = models.CharField(max_length=100)
    ano_inicio = models.CharField(max_length=20)
    ano_termino= models.CharField(max_length=20)
    nombre_empresa = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, null = True, blank = True)



