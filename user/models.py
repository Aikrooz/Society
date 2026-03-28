# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    account_number = models.CharField(max_length=20)
    age = models.IntegerField()