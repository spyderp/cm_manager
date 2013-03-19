from django.db import models

# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=20)
    nivel = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('UserDetail')
        verbose_name_plural = _('UserDetails')
    def __unicode__(self):
    	return self.nickname

class Publicador(models.Model):
	nombre = models.CharField(max_length=45, unique=True)
	lema = models.CharField(max_length=80)
	logo = models.ImageField("Logo de su Fansub", upload_to="images/logo/", blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now=true)
    fecha_modificacion = models.DateTimeField()
    user = models.ManyToManyField(User)
	
    class Meta:
        verbose_name = _('Publicador')
        verbose_name_plural = _('Publicadores')

    def __unicode__(self):
        return self.nombre
    