try: 
    from django.conf.urls import patterns, url 
except ImportError: 
    # for Django version less then 1.4
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('publicaciones.views',
    url(r'^categorias/$', 'categorias', name='Categorias'),
    url(r'^categorias/(?P<categoria>[\w\-]+)$', 'categoria', name='Categoria seleccionada'),
    url(r'^generos/$', 'generos', name='Generos'),
    url(r'^generos/(?P<genero>[\w\-]+)$', 'genero', name='Genero selecionado'),
    url(r'^$', 'inicio', name='inicio'),
 )