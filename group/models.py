from django.db import models
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

STATUS =(
    ('Active','Active'),
    ('Completed','Completed')
)


class GroupModel(models.Model):
    name=models.CharField()
    group_creator=models.ForeignKey(User,on_delete=models.CASCADE)
    contribution_amount=models.PositiveIntegerField([MinValueValidator(1000)])
    number_of_memebers=models.SmallIntegerField(
        validators=[MinValueValidator(10)]
    )
    cycle_length=models.SmallIntegerField(
        validators=[MinValueValidator(1)]
    )
    start_date=models.DateField()
    status=models.CharField(choices=STATUS,default='Active')