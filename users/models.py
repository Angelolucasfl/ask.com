from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nome_usuario = models.CharField(max_length=150, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    REQUIRED_FIELDS = [] 
    
