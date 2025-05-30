from rest_framework import serializers
from .models import Schedule
from deep_translator import GoogleTranslator


class ScheduleSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)

    class Meta:
        model = Schedule
        fields = ['uid', 'title', 'time', 'speakers', 'file']


class ScheduleRussianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['uid', 'title', 'time', 'speakers', 'file']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        translator = GoogleTranslator(source='auto', target='ru')
        data['title'] = translator.translate(instance.title)
        return data


class ScheduleEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['uid', 'title', 'time', 'speakers', 'file']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        translator = GoogleTranslator(source='auto', target='en')
        data['title'] = translator.translate(instance.title)
        return data
