from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255, default='title')
    cover = models.ImageField(upload_to='alboms/')

    def __str__(self):
        return self.title