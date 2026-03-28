from rest_framework import serializers
from user.models import User
from .models import GroupModel
class GroupSerializer(serializers.ModelSerializer):
    group_creator=serializers.ReadOnlyField(source='group_creator.username')
    class Meta:
        model=GroupModel
        fields=['group_creator','name','contribution_amount','number_of_members','cycle_length','start_date','status']