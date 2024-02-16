
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='users/', blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)