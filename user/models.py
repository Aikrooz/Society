# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

class User(AbstractUser):
    account_number = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(validators=[MinValueValidator(10)])