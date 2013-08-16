from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.contrib import messages
from publicaciones.models import *

def categorias(request):
	return render_to_response('categorias.html', {'user':request.user}, RequestContext(request))

def categoria(request, categoria):
	resultado=Categoria.objects.get(nombre=categoria)
	return render_to_response('categoria.html', {'user':request.user, 'title':categoria, 'resultado':resultado}, RequestContext(request))

def generos(request):
	return render_to_response('generos.html', {'user':request.user}, RequestContext(request))

def genero(request, genero):
	resultado=Tipo.objects.get(nombre=genero)
	return render_to_response('genero.html', {'user':request.user, 'title': genero, 'resultado':resultado}, RequestContext(request))

def inicio(request):
	return render_to_response('inicio.html', {'user':request.user}, RequestContext(request));