from django.contrib import admin
from publicaciones.models import *

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'activo')
class TipoAdmin (admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'tipo_adulto', 'activo')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tipo,TipoAdmin)
admin.site.register(Publicacion)
admin.site.register(Capitulo)