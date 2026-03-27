from django.db import models
from user.models import User
from group.models import GroupModel
# Create your models here.


class Contribution(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('pending_verification', 'Pending Verification'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)
    cycle_number = models.SmallIntegerField(help_text='Number of times a member in the group will repeat the same cycle')
    amount = models.SmallIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    paid_at = models.DateTimeField(null=True, blank=True)
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='verified_contributions')


