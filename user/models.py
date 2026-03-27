from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class User(AbstractUser):
    account_number=models.CharField()
    age=models.IntegerField(
        validators=[MinValueValidator(10)]
    )


