from django.db import models

# Create your models here.
class Video(models.Model):
    file = models.FileField(upload_to='videos')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
