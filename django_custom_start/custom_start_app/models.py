from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User (AbstractUser):
    new_field = models.TextField(blank=True)

#class image_test(models.Model):
#    nome = models.CharField(blank=True)