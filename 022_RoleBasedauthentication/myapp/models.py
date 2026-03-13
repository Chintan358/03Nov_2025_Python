from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.manager import CustomeUserManager

class Role(models.Model):
    name = models.CharField(max_length=20)


class CustomeUser(AbstractUser):
    username=None
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=15,unique=True)
    bio = models.TextField()

    USERNAME_FIELD="phone"

    objects=CustomeUserManager()