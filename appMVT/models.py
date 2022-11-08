from django.db import models

class Familiar(models.Model):

    pariente = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nac = models.DateField()
    