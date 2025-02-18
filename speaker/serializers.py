from rest_framework import serializers
from .models import *



class SpeakerSerializer(serializers.ModelSerializer):

    description = serializers.CharField(required=True)

    class Meta:
        model = Speaker
        fields = ['uid', 'name', 'image', 'role', 'description']


