from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cm_manager.views.home', name='home'),
    # url(r'^cm_manager/', include('cm_manager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'', include('administracion.urls')),
     #url(r'^comment/', include('comentarios.urls')),
     url(r'', include('publicaciones.urls')),
     url(r'', include('social_auth.urls')),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
)
