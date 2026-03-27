from django.db import models
from user.models import User
from group.models import GroupModel
# Create your models here.
class Member(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(GroupModel,on_delete=models.CASCADE)
    payout_order=models.CharField()
    joined_at=models.DateTimeField(auto_now=True)