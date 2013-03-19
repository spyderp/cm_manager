from django.db import models

# Create your models here.
class Archivo(models.Model):
    alto = models.IntegerField(null=False)
    ancho = models.IntegerField(null=False)
    extension = models.CharField(max_length=5)
    path = models.FileField(upload_to="archivos/", null=False)
    tipo = models.CharField(max_length=11)
    fecha_creacion = models.DateTimeField(auto_now=False)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('Archivo')
        verbose_name_plural = _('Archivos')

    def __unicode__(self):
        pass

class Categoria(models.Model):
    nombre = models.CharField("Minimo 5 maximo 15 caracteres",max_length=15, min_length=5, unique=True)
    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')
    
    def __unicode__(self):
        return self.nombre

class Capitulo(models.Model):
    numero_capitulo = models.IntegerField()
    visitas = models.IntegerField(default=0)
    votos = models.IntegerField(default=0)
    publicacion = models.ManyToManyField(publicacion)
    publicador = models.ForeignKey(Publicador)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = _('Capitulo')
        verbose_name_plural = _('Capitulos')

    def __unicode__(self):
        pass
    
class Publicacion(models.Model):
    nombre = models.CharField("Maximo 35 caracteres, No se puede duplicar un manga ya creado", max_length=35, unique=True)
    descripcion = models.CharField("Descripcion corta de lo que se trata el manga", max_length=150, min_length=30)
    imagen = models.ImageField("Imagen de la publicacion", upload_to="images/publicacion/", null=False)
    fecha_creacion = models.DateTimeField()
    categoria = models.ForeignKey(Categoria)
    tipo = models.ManyToManyField(Tipo)
    class Meta:
        verbose_name = _('Publicacion')
        verbose_name_plural = _('Publicaciones')
 
    def __unicode__(self):
        return self.nombre

class Sprite(models.Model):
	orden = models.IntegerField()
    class Meta:
        verbose_name = _('Sprite')
        verbose_name_plural = _('Sprites')

    def __unicode__(self):
        pass
    

class Tipo(models.Model):
     nombre = models.CharField("Minimo 5 maximo 15 caracteres",max_length=15, min_length=5, unique=True)
    class Meta:
        verbose_name = _('Tipo')
        verbose_name_plural = _('Tipos')

    def __unicode__(self):
        return self.nombre
    
                      