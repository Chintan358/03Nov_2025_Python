from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.manager import CustomeUserManager
# Create your models here.
class CustomeUser(AbstractUser):
    phone = models.CharField(max_length=15,unique=True)
    bio = models.TextField()

    USERNAME_FIELD="phone"

    objects=CustomeUserManager()