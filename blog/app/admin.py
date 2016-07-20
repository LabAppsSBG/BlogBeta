from django.contrib import admin

# Register your models here.

from .models import Usuario,articulo,comentario,imgportada


class UsuarioAdmin(admin.ModelAdmin):
	list_display=('nombre','correo')
	search_fields=('nombre','correo')
#poner clase primera en mayuscula
class ArticuloAdmin(admin.ModelAdmin):
	list_display=('titulo','descripcion')
	search_fields=('titulo','descripcion')
	# fields=('titulo','creador')  





admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(articulo,ArticuloAdmin)
admin.site.register(comentario)
admin.site.register(imgportada)