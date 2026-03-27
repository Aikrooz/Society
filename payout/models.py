from django.db import models
from group.models import GroupModel
from user.models import User
# Create your models here.
class Payout(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
    ]

    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payouts')
    cycle_number = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    paid_at = models.DateTimeField(null=True, blank=True)