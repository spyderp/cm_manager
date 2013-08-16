try: 
    from django.conf.urls import patterns, url 
except ImportError: 
    # for Django version less then 1.4
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('administracion.views',
	url(r'^acceso/$', 'acceso', name='Acceder'),
    url(r'^contactos/$', 'contactos', name='Contactenos'),
    url(r'^fansub/$', 'fansub', name='Fansub'),
    url(r'^fansub/principal$', 'userIndex', name='Fansub'),
    url(r'^fansub/new-usuario$', 'userAdd', name='Fansub'),
    url(r'^fansub/edit-usuario/(\d{1,4})$', 'userEdit', name='Fansub'),
    url(r'^fansub/delete-usuario/(\d{1,4})$', 'userDelete', name='Fansub'),
    url(r'^fansub/usuarios$', 'usuarios', name='Fansub'),
    url(r'^fansub/(?P<fansub>[\w\-]+)$', 'detallesPublicador'),
    url(r'^registro/$', 'registro', name='registro'),
    url(r'^salir/$', 'salir', name='Salir'),
 )