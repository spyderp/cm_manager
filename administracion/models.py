from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=20)
    nivel = models.IntegerField(default=0)
    def __unicode__(self):
    	return self.nickname

class Publicador(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    lema = models.CharField(max_length=80)
    logo = models.ImageField("Logo de su Fansub", upload_to="images/logo/", blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_modificacion = models.DateTimeField()
    activo = models.BooleanField(default=False)
    aprobar = models.BooleanField(default=False)
    user = models.ManyToManyField(User)
    def __unicode__(self):
        return self.nombre
    