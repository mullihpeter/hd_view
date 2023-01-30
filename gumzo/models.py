from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from accounts.models import Profile, CustomUser
from videos.models import Video
from images.models import Image

# Create your models here.
VIDEO_CATEGORIES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)


class Media(models.Model):
    title = models.CharField(max_length=600)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=VIDEO_CATEGORIES, max_length=25)
    age_limit = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.ManyToManyField(Video)
    image = models.ManyToManyField(Image)

    def __str__(self):
        return self.title


class Gumzo(models.Model):
    title = models.CharField(max_length=200)
    uuid = models.UUIDField(default=uuid.uuid4)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='gumzo_images')

    class Meta:
        pass

    def __str__(self):
        return self.title
