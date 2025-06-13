from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# confirm_password


User = get_user_model()

class UserLoginModel(models.Model):
    login = models.OneToOneField(User, related_name= 'login', on_delete=models.CASCADE)