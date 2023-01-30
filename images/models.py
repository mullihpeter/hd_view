from django.db import models


# Create your models here.
class Image(models.Model):
    file = models.FileField(upload_to='images')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
