from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    correo = models.CharField(max_length=50, null=True)
    clave = models.CharField(max_length=50, null=True)

    def __str__(self):
        # retornar cadena no tupla
        return (self.nombre.encode('utf8'))

    # class meta sirve para poner algunas funciones entre ellas ordenar
    class Meta:
        ordering = ['nombre']