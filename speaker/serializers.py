from rest_framework import serializers
from .models import *
from deep_translator import GoogleTranslator
from django.core.cache import cache

class SpeakerSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)
    description = serializers.CharField(required=True)
    class Meta:
        model = Speaker
        fields = ['uid', 'name', 'image', 'role', 'description']


class SpeakerRussianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        translator = GoogleTranslator(source='auto', target='ru')


        for field in ['name', 'role', 'description']:
            cache_key = f"organiser_{field}_ru_{instance.uid}"
            cached_value = cache.get(cache_key)

            if cached_value:
                data[field] = cached_value
            else:
                try:
                    data[field] = translator.translate(getattr(instance, field))
                    cache.set(cache_key, data[field], timeout=86400)
                except Exception as e:
                    print(f"Translation error for {field}: {e}")
                    data[field] = getattr(instance, field)

        return data

class SpeakerEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        translator = GoogleTranslator(source='auto', target='en')

        # Use caching to avoid repeated API calls
        for field in ['name', 'role', 'description']:
            cache_key = f"organiser_{field}_en_{instance.uid}"
            cached_value = cache.get(cache_key)

            if cached_value:
                data[field] = cached_value
            else:
                try:
                    data[field] = translator.translate(getattr(instance, field))
                    cache.set(cache_key, data[field], timeout=86400)
                except Exception as e:
                    print(f"Translation error for {field}: {e}")
                    data[field] = getattr(instance, field)

        return data


class SpeakerUzbekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        translator = GoogleTranslator(source='auto', target='uz')

        # Use caching to avoid repeated API calls
        for field in ['name', 'role', 'description']:
            cache_key = f"organiser_{field}_uz_{instance.uid}"
            cached_value = cache.get(cache_key)

            if cached_value:
                data[field] = cached_value
            else:
                try:
                    data[field] = translator.translate(getattr(instance, field))
                    cache.set(cache_key, data[field], timeout=86400)
                except Exception as e:
                    print(f"Translation error for {field}: {e}")
                    data[field] = getattr(instance, field)

        return data
