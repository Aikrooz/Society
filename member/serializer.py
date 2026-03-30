from rest_framework import serializers


class MembersSerializer(serializers.models):
    class Meta:
        fields=['id','user','payout_order','joined']