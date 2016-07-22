from django.contrib import admin
from .models import articulo, comentario, imgportada

#poner clase primera en mayuscula
class ArticuloAdmin(admin.ModelAdmin):
	list_display=('titulo','descripcion')
	search_fields=('titulo','descripcion')
	# fields=('titulo','creador')

admin.site.register(articulo,ArticuloAdmin)
admin.site.register(comentario)
admin.site.register(imgportada)