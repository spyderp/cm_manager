# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from administracion.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import simplejson
from django.http import HttpResponse

def acceso(request):
	result = []
	if request.user.is_authenticated():
		messages.info(request, "Ya se encuentra autenticado")
		return redirect('/')
	if request.method == 'POST':
		formulario= AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				result.append({'result':1, 'msg':"Bienvenido su acceso ha sido exitoso"})
			else:           
				result.append({'result':0, 'msg':"Su cuenta se encuentra desactivada por favor contacte con la administracion de la web"})
		else:
			result.append({'result':0, 'msg':"Su usuario o contrasena son incorrecto, Por favor intente nuevamente"})
		return HttpResponse(simplejson.dumps(result), mimetype='application/json')	
	else:
		formulario = AuthenticationForm()		
	return render_to_response('acceder.html', {'formulario':formulario}, RequestContext(request))

def contactos(request):
	from django.conf import settings
	from django.core.mail import send_mail, BadHeaderError
	message ="Nombre: " + request.POST.get('nombre', '')+'\n'
	message =message + "Correo: "+request.POST.get('correo', '')+'\n'
	subject = request.POST.get('tema', '')
	message = message + "Mensaje: "+request.POST.get('msg', '')+'\n'
	if subject and message :
		try:
			send_mail(subject, message, settings.EMAIL_FROM, [settings.EMAIL_TO])
			messages.success(request, "Su correo ha sido enviado exitosamente, en caso que lo amerite nuestro personal se contactara con usted")
		except BadHeaderError:
			messages.error("Ocurrio un error y no se pudo enviar su correo. Intente nuevamente")
	return render_to_response('contactos.html', {'user':request.user}, RequestContext(request))



def detallesPublicador(request, fansub):
	publicador=Publicador.objects.all().filter(nombre__icontains=fansub.replace('-',' '))[0]
	return render_to_response('detalles.html', {'user':request.user,'publicador':publicador}, RequestContext(request))

@permission_required('administracion.edit_publicador')
def editarPublicador(request):
	return render_to_response('usuarios.html', {'user':request.user,  'publicador':publicador}, RequestContext(request))	

def fansub(request):
	fansub = Publicador.objects.all().filter(activo=1);
	return render_to_response('fansub.html', {'user':request.user , 'fansub':fansub }, RequestContext(request))

def registro(request):
	from administracion.forms import RegistrationForm
	from recaptcha.client import captcha
	if request.user.is_authenticated() and request.user.groups.all() and  (request.user.groups.all()[0].id == 2 or request.user.groups.all()[0].id == 3):
		messages.info(request, "Ya su cuenta de usuario esta asociada a un Fansub")
		return redirect('/')
	if request.method == 'POST':
		response = captcha.submit(  
            request.POST.get('recaptcha_challenge_field'),  
            request.POST.get('recaptcha_response_field'),  
            '6Le-l98SAAAAAF32m3a--C06tOrk5VXR1GHol0DS',  
            request.META['REMOTE_ADDR'],)  
		if response.is_valid:
			if request.user.is_authenticated():
				requestCopy = request.POST.copy()
				requestCopy['user']=request.user.id
				formulario=PublicadorForm(requestCopy, request.FILES)
				formulario2=''
				if formulario.is_valid():
					if formulario.save():
						messages.success(request, "Exito se ha creado el nuevo fansub, y tu eres el administrador")
						request.user.groups.add(2)
						request.user.save()
						return redirect('/')
					else:
						messages.error(request, "Ocurrio un error y no se pudo registrar el nuevo Fansub, Por favor Intenten nuevamente")
				else:
					messages.error(request, u'Error: Uno o más campos son incorrectos, corregir e intente nuevamente')
			else:
				formulario2=RegistrationForm(request.POST, prefix='usuarios')
				if(formulario2.is_valid()):
					usuario=formulario2.save()
					requestCopy = request.POST.copy()
					requestCopy['publicador-user']=usuario.id
					formulario=PublicadorForm(requestCopy, request.FILES, prefix="publicador")
					if formulario.is_valid():
						if formulario.save():
							messages.success(request, "Exito se ha creado el nuevo fansub, y tu eres el administrador")
							usuario.groups.add(2)
							usuario.save()
							user = authenticate(username=request.POST['usuarios-username'], password=request.POST['usuarios-password1'])
							login(request, user)
							return redirect('/')
						else:
							messages.error(request, "Ocurrio un error y no se pudo registrar el nuevo Fansub, Por favor Intenten nuevamente")
					else:
						messages.error(request, u'Error: Uno o más campos son incorrectos, corregir e intente nuevamente')
				else:
					formulario=PublicadorForm(request.POST, request.FILES, prefix="publicador")
					messages.error(request, u'Error: Uno o más campos son incorrectos, corregir e intente nuevamente')
		else:
			formulario=PublicadorForm(request.POST, request.FILES, prefix="publicador")
			formulario2=RegistrationForm(request.POST, prefix='usuarios')
			messages.error(request, u'La palabra de seguridad no es correcta por favor intente nuevamente')
	else:
		if request.user.is_authenticated():
			formulario=PublicadorForm( initial={'user':[str(request.user.id)]}) 
			formulario2=''
		else: 
			formulario=PublicadorForm(prefix="publicador");
			formulario2=RegistrationForm(prefix='usuarios')
	return render_to_response('registro.html', {'user':request.user, 'formulario':formulario, 'formulario2':formulario2}, RequestContext(request))

@login_required(login_url='/acceso')
def salir(request):
	logout(request)
	return redirect('/')

@permission_required('administracion.new_user')
def userAdd(request):
	from django.core.mail import send_mail, BadHeaderError
	from administracion.forms import RegistrationForm
	from django.conf import settings
	import random
	import string
	if request.method == 'POST':
		s=string.lowercase+string.digits
		password=random.sample(s,6)
		requestCopy = request.POST.copy()
		requestCopy['password1']=password
		requestCopy['password2']=password
		formulario=RegistrationForm(requestCopy)
		if(formulario.is_valid()):
			usuario=formulario.save()
			usuario.groups.add(3)
			usuario.save()
			publicador=Publicador.objects.get(user=request.user.id)
			publicador.user.add(usuario.id)
			publicador.save()
			message=u"""Te damos la bienvenida a mangaInk\n
			El Fansub: {0} \n
			Te ha asociado como parte de su equipo. \n 
			El cual esta administrado por {1} \n
			Los datos para acceder {2}  \n
			Contraseña: {3} \n
			Si tiene problemas con este correo puedes escribirle al correo del Administrador {4} \n		
			o en la sección de contacto en mangaInk.com \n\n
			Para acceder visita la siguiente web: http://www.mangaink.com/acceder/""".format(publicador,request.user.username,request.POST['username'],password,request.user.email)
			try:
				send_mail("Ahora formas parte de un Fansub de MangaInK", message, settings.EMAIL_FROM, [request.POST['email']])
				messages.success(request, "Nuevo usuario creado para tu fansub, se le envio un corrreo al usuario con sus datos")
			except BadHeaderError:
				messages.warning(u"Ocurrio un error y no se pudo enviar el correo. Contácte al nuevo usuario e informe de sus datos de acceso.")	
			return redirect('/fansub/usuarios')
		else:
			messages.error(request, u'Error: Uno o más campos son incorrectos, corregir e intente nuevamente')
	else:
		formulario=RegistrationForm()
	return render_to_response('addUser.html', {'user':request.user, 'formulario':formulario}, RequestContext(request))

@permission_required('administracion.edit_user')
def userEdit(request, usuarioId):
	from django.contrib.auth.models import User
	usuario=get_object_or_404(User, id=usuarioId)
	formulario=EditarForm(request.POST or None, instance=usuario)
	if request.method == 'POST':
		if formulario.is_valid():
			formulario.save()
			messages.success(request,u"Se actualizaron los datos")
			return redirect('/fansub/usuarios')
		else:
			messages.error(request,u"Uno o más campos son invalidos, corregir e intente nuevamente")
	return render_to_response('userEdit.html', {'user':request.user, 'formulario':formulario}, RequestContext(request))	

@permission_required('administracion.del_user')
def userDelete(request, usuarioId):
	from django.conf import settings
	usuario=get_object_or_404(User, id=usuarioId)
	if(usuario.id==user.id):
		messages.warning(request, "No puede borrar tu misma cuenta")
	else:
		publicador=Publicador.objects.get(user=request.user.id)
		correo=usuario.email
		publicador.user.remove(usuario)
		messages.success(request,u"Se borro el usuario del fansub")
		try:
			send_mail("Tu cuenta de usuario ha sido removida del fansub", "El usuario administrador ha removido tu cuenta de usuario", settings.EMAIL_FROM, [correo])
			messages.success(request, "Nuevo usuario creado para tu fansub, se le envio un corrreo al usuario con sus datos")
		except BadHeaderError:
			messages.warning(u"Ocurrio un error y no se pudo enviar el correo. Contácte al nuevo usuario e informe de sus datos de acceso.")	
		return redirect('/fansub/usuarios')

def userIndex(request):
	from django.template.defaultfilters import slugify
	publicador=Publicador.objects.get(user=request.user.id)
	nombre=slugify(publicador.nombre)
	return redirect('/fansub/'+nombre)

@permission_required('administracion.list_user')
def usuarios(request):
	publicador=Publicador.objects.get(user=request.user.id)
	return render_to_response('usuarios.html', {'user':request.user,  'publicador':publicador}, RequestContext(request))


