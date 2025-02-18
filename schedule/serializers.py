from rest_framework import serializers
from .models import *




class ScheduleSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)
    class Meta:
        model = Schedule
        fields = ['uid', 'title', 'time', 'speakers']
