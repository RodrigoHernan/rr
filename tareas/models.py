from django.db import models
from django.utils import timezone


# Create your models here.
class Grupo(models.Model):
    nombre = models.CharField(max_length=200)


    def __str__(self):
        return '{}'.format(self.nombre)


# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    hecho = models.BooleanField()
    time = models.DateTimeField(default=timezone.now)
    grupo = models.ForeignKey(Grupo, related_name='Grupo', on_delete=models.CASCADE,)
    descripcion = models.CharField(max_length=400,blank=True, null=True )

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.hecho)