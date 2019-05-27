from django.db import models
from django.contrib.auth.models import AbstractUser


class ParkUser(AbstractUser):
    avatar = models.ImageField\
        (verbose_name='аватарка', blank=True, upload_to='users')
    age = models.SmallIntegerField(verbose_name='возраст')

# Create your models here.
