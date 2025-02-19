from rest_framework import serializers
from .models import *



class OrganiserSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)
    description = serializers.CharField(required=True)
    class Meta:
        model = Organiser
        fields = ['uid', 'name', 'image', 'role', 'description']
