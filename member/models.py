from django.db import models
from user.models import User
from group.models import GroupModel
# Create your models here.
class Member(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='member')
    group=models.ForeignKey(GroupModel,on_delete=models.CASCADE,related_name='group_name')
    payout_order=models.CharField(max_length=10)
    joined_at=models.DateTimeField(auto_now_add=True)