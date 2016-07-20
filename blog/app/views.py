
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from app.models import Usuario,articulo,comentario
from django.template import RequestContext

# Create your views here.

def crear2(request):
	creado=""
	crear='crear.html'
	if request.method == "POST": 
		nombre=request.POST['nombre']
		#me retorna un objeto
		contra=request.POST['contra']
		email=request.POST['email']

		p1=Usuario(nombre=nombre,correo=email,clave=contra,)
		p1.save()
		creado="registro exitoso"
	else:
		creado=""	
	return render(request,crear ,{'error':creado})

def mostrartarticulo(request):
	pagina="viewprueba.html"

	return render(request,pagina)

def index(request):
	pagina="index2.html"
	articulos=articulo.objects.all()


	return render(request,pagina,{"articulos":articulos})

def viewpost(request,offset):
	pagina="viewpost.html"
	articulos=articulo.objects.get(id=offset)
	comentarios=comentario.objects.all().filter(articulo_id=articulos.id)

	return render(request,pagina,{"articulo":articulos, "comentarios":comentarios})


