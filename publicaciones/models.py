from django.db import models
from django.contrib.auth.models import User
from administracion.models import Publicador
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=15,  unique=True)
    descripcion = models.CharField( max_length=50, null=True)
    activo = models.BooleanField(default=True)
    class Meta:
        ordering = ['id']
    def __unicode__(self):
        return self.nombre

class Tipo(models.Model):
    nombre = models.CharField(max_length=15,  unique=True)
    descripcion = models.CharField(max_length=200, null=True)
    tipo_adulto = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    class Meta:
        ordering = ['nombre']
    def __unicode__(self):
        return self.nombre     

class Publicacion(models.Model):
    nombre = models.CharField( max_length=35, unique=True)
    descripcion = models.CharField(max_length=150)
    imagen = models.ImageField("Imagen de la publicacion", upload_to="images/publicacion/", null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=False)
    aprobar = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria)
    tipo = models.ManyToManyField(Tipo)

    class meta:
        verbose_name_plural = ('Publicaciones')
    def __unicode__(self):
        return '%s - creado: %s' % (self.nombre, self.fecha_creacion)

class Capitulo(models.Model):
    numero_capitulo = models.IntegerField()
    visitas = models.IntegerField(default=0)
    votos = models.IntegerField(default=0)
    publicacion = models.ForeignKey(Publicacion)
    publicador = models.ForeignKey(Publicador)
    activo = models.BooleanField(default=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'Numero %i,  Total visistas: %i, Total votos: %i' % (self.numero_capitulo, self.visitas, self.votos)

class Sprite(models.Model):
    def content_file_name(instance, filename):
        ext = filename[-3:]
        new = hashlib.md5(filename+str(time.time()))
        return "archivo/%s.%s" % (new.hexdigest(),ext)
	orden = models.IntegerField()
    path = models.ImageField("Solo puede insertar imagenes", upload_to=content_file_name, null=False)
    size = models.IntegerField() 
    alto = models.IntegerField(null=False)
    ancho = models.IntegerField(null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    capitulo = models.ForeignKey(Capitulo)

    def __unicode__(self):
        return u'Archivo: %s, Orden: %i, Tamano: %i, Ancho: %i, Alto: %i' % (self.path, self.orden, self.size, self.width, self.height)

    def save(self, *args, **kwargs):
        self.size=self.path.size
        self.alto = self.path.height
        self.ancho = self.path.width
        super(Archivo, self).save(*args, **kwargs)
    
class suscripcion(models.Model):
    user = models.ForeignKey(User)
    publicacion = models.ForeignKey(Publicacion)
    class Meta:
        verbose_name = ('suscripcion')
        verbose_name_plural = ('suscripciones')

    def __unicode__(self):
        pass
    
class configSuscripcion(models.Model):
    correo = models.BooleanField(default=True)
    facebook = models.BooleanField(default=False)
    twitter = models.BooleanField(default=False)
    #google = models.BooleanField("Google+", default=False)
    user = models.ForeignKey(User)
    class Meta:
        verbose_name = ('configSuscripcion')
        verbose_name_plural = ('configSuscripciones')

    def __unicode__(self):
        pass
    


                      