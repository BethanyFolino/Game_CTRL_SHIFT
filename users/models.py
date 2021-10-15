from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length=30)
    profile_img = models.ImageField(upload_to='images/', null=True, blank=True )

