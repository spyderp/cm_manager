from django.db import models

# Create your models here.
class CommentDetail(models.Model):
    comment = models.OneToOneField(Comment)
    votos = models.IntegerField(default=0)

    class Meta:
        verbose_name = _( 'CommentDetail')
        verbose_name_plural = _( 'CommentDetails')

    def __unicode__(self):
        pass
    