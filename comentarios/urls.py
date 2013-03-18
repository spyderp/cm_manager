from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^ajax/post/$', 'comentarios.views.post_comment'),
)