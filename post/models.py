from django.db import models

# Create your models here.

class Post(models.Model):
    person = models.CharField(max_length=120, verbose_name='ID')
    content = models.TextField(verbose_name='Message')
    publishDate = models.DateTimeField(verbose_name='Tarih')
    #post kayıtlarının ayırt edilmesi için..
    def __str__(self):
        return self.person