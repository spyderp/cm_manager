from django.db import models
from django.contrib.comments.models import Comment
# Create your models here.
class CommentDetail(models.Model):
    comment = models.OneToOneField(Comment)
    votos = models.IntegerField(default=0)
    def __unicode__(self):
        return 'Total de votos %i, Comentario: %s'% (self.votos, self.comment)
    