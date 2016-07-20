from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre=models.CharField(max_length = 50 , null=True)
	correo=models.CharField(max_length = 50 , null=True)
	clave=models.CharField(max_length = 50 , null=True)



	def __str__(self):
		#retornar cadena no tupla
		return (self.nombre.encode('utf8'))
		#class meta sirve para poner algunas funciones entre ellas ordenar
	class Meta:
		ordering=['nombre']

class imgportada(models.Model):
	image=models.ImageField(upload_to='photos',blank=True, null=True)


class articulo(models.Model):
	creador=models.ForeignKey(Usuario)
	imageportada=models.ForeignKey(imgportada,default=1)
	
	#ManyToManyField(Autor) relacion muchos a muchos
	titulo=models.CharField(max_length = 200 , null=True)
	descripcion=models.CharField(max_length = 200 , null=True)
	cuerpo=models.TextField(null=True)

	def __str__(self):
		cadena=self.titulo.encode('utf8')
		return cadena

class comentario(models.Model):
	articulo=models.ForeignKey(articulo)
	user=models.ForeignKey(Usuario)
	comentario=models.TextField(null=True)
	

