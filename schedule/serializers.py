from rest_framework import serializers
from .models import *
from deep_translator import GoogleTranslator



class ScheduleSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)
    class Meta:
        model = Schedule
        fields = ['uid', 'title', 'time', 'speakers']




class ScheduleRussianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        translator = GoogleTranslator(source='auto', target='ru')
        data['title'] = translator.translate(instance.title)

        return data


class ScheduleEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        translator = GoogleTranslator(source='auto', target='en')
        data['title'] = translator.translate(instance.title)

        return data