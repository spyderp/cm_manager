# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, HiddenInput, TextInput
# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(User)
    nivel = models.IntegerField(default=0)
    def __unicode__(self):
    	return self.nickname

class Publicador(models.Model):
    nombre = models.CharField(max_length=45, unique=True, )
    lema = models.CharField(max_length=80)
    logo = models.ImageField("Logo de su Fansub", upload_to="logosFansub/")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    user = models.ManyToManyField(User)
    def __unicode__(self):
        return self.nombre
    class Meta:
        permissions = (
                        ("new_user", "Agregar usuarios al fansub"),
                        ("edit_user", "Editar usuario del fansub"),
                        ("del_user", "borrar un usuario del fansub"),
                        ("list_user", "lista de usuarios"),

                       )

class PublicadorForm(ModelForm):
    class Meta:
        model = Publicador
        fields = ('nombre', 'lema', 'logo', 'user' )
        widgets = {
            'lema':TextInput(attrs={'style':'width:50%'})
        }

class EditarForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active' )            