from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)


class CustomUser(AbstractUser):
    profiles = models.OneToOneField('Profile', blank=True)
    username = models.CharField(max_length=350)
    email = models.EmailField(blank=False,max_length=254, verbose_name="email address")
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"


class Profile(models.Model):
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=15)
    profile_pic = models.ImageField(upload_to='profile_pic', default='default.png')
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.username
