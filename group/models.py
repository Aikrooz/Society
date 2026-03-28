from django.db import models
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

STATUS =(
    ('Active','Active'),
    ('Completed','Completed')
)


class GroupModel(models.Model):
    name=models.CharField(max_length=100)
    group_creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='group_creator')
    contribution_amount=models.PositiveIntegerField(validators=[MinValueValidator(1000)])
    number_of_members=models.SmallIntegerField(
        validators=[MinValueValidator(10)]
    )
    cycle_length=models.SmallIntegerField(
        validators=[MinValueValidator(1)]
    )
    start_date=models.DateField()
    status=models.CharField(choices=STATUS,default='Active', max_length=20)
    date_created=models.DateTimeField(auto_now_add=True)