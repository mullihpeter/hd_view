import random

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)


class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4)
    username = models.CharField(max_length=350, unique=True)
    email = models.EmailField(blank=False, max_length=255, verbose_name="email address")
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    nickname = models.TextField(max_length=200)
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=15)
    profile_pic = models.ImageField(upload_to='profile_pic', default='default.png')
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.nickname
