from rest_framework import serializers, generics
from translatepy import Translator
from django.core.cache import cache
from .models import Organiser

class OrganiserSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)
    description = serializers.CharField(required=True)
    class Meta:
        model = Organiser
        fields = ['uid', 'name', 'image', 'role', 'description']





class BaseOrganiserSerializer(serializers.ModelSerializer):
    language = None

    class Meta:
        model = Organiser
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        translator = Translator()


        for field in ['role', 'description']:
            cache_key = f"organiser_{field}_{self.language}_{instance.uid}"
            cached_value = cache.get(cache_key)

            if cached_value:
                data[field] = cached_value
            else:
                try:
                    translated_text = translator.translate(getattr(instance, field), self.language).result
                    data[field] = translated_text
                    cache.set(cache_key, translated_text, timeout=86400)
                except Exception as e:
                    print(f"Translation error for {field} ({self.language}): {e}")
                    data[field] = getattr(instance, field)

        return data


class OrganiserRussianSerializer(BaseOrganiserSerializer):
    language = "ru"

class OrganiserEnglishSerializer(BaseOrganiserSerializer):
    language = "en"

class OrganiserUzbekSerializer(BaseOrganiserSerializer):
    language = "uz"

