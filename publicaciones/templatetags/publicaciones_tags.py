from django import template
from publicaciones.models import *
from django.template.loader import render_to_string

register = template.Library()
@register.filter
def get_menus(user): 
    categoria = Categoria.objects.all();
    tipo=Tipo.objects.all();
    return render_to_string('menu.html', {'categoria':categoria, 'tipo':tipo, 'user':user})
