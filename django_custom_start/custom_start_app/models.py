from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User (AbstractUser):
    new_field = models.TextField(blank=True)

class image_test(models.Model):
    name = models.CharField(blank=True, max_length=100)
    image = models.ImageField(upload_to='images_test_folder/',blank=True)

    class Meta:
        verbose_name_plural = 'image_tests'
    #resolvendo o object no admim nome melhor
    def __str__(self):
        return self.name