from rest_framework import serializers, generics
from translatepy import Translator
from django.core.cache import cache
from .models import Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    uid = serializers.UUIDField(read_only=True)
    description = serializers.CharField(required=True)
    class Meta:
        model = Speaker
        fields = ['uid', 'name', 'image', 'role', 'description']






class BaseOrganiserSerializer(serializers.ModelSerializer):
    language = None

    class Meta:
        model = Speaker
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        translator = Translator()


        for field in ['name', 'role', 'description']:
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



class SpeakerRussianSerializer(BaseOrganiserSerializer):
    language = "ru"

class SpeakerEnglishSerializer(BaseOrganiserSerializer):
    language = "en"

class SpeakerUzbekSerializer(BaseOrganiserSerializer):
    language = "uz"







class OrganiserListRussianView(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerRussianSerializer

class SpeakerRetrieveRussianView(generics.RetrieveAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerRussianSerializer
    lookup_field = 'uid'

class OrganiserListEnglishView(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerEnglishSerializer

class OrganiserRetrieveEnglishView(generics.RetrieveAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerEnglishSerializer
    lookup_field = 'uid'

class OrganiserListUzbekView(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerUzbekSerializer

class OrganiserRetrieveUzbekView(generics.RetrieveAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerUzbekSerializer
    lookup_field = 'uid'
















# class SpeakerRussianSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Speaker
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#
#         translator = GoogleTranslator(source='auto', target='ru')
#
#
#         for field in ['name', 'role', 'description']:
#             cache_key = f"organiser_{field}_ru_{instance.uid}"
#             cached_value = cache.get(cache_key)
#
#             if cached_value:
#                 data[field] = cached_value
#             else:
#                 try:
#                     data[field] = translator.translate(getattr(instance, field))
#                     cache.set(cache_key, data[field], timeout=86400)
#                 except Exception as e:
#                     print(f"Translation error for {field}: {e}")
#                     data[field] = getattr(instance, field)
#
#         return data
#
# class SpeakerEnglishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Speaker
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#
#         translator = GoogleTranslator(source='auto', target='en')
#
#         # Use caching to avoid repeated API calls
#         for field in ['name', 'role', 'description']:
#             cache_key = f"organiser_{field}_en_{instance.uid}"
#             cached_value = cache.get(cache_key)
#
#             if cached_value:
#                 data[field] = cached_value
#             else:
#                 try:
#                     data[field] = translator.translate(getattr(instance, field))
#                     cache.set(cache_key, data[field], timeout=86400)
#                 except Exception as e:
#                     print(f"Translation error for {field}: {e}")
#                     data[field] = getattr(instance, field)
#
#         return data
#
#
# class SpeakerUzbekSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Speaker
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#
#         translator = GoogleTranslator(source='auto', target='uz')
#
#         # Use caching to avoid repeated API calls
#         for field in ['name', 'role', 'description']:
#             cache_key = f"organiser_{field}_uz_{instance.uid}"
#             cached_value = cache.get(cache_key)
#
#             if cached_value:
#                 data[field] = cached_value
#             else:
#                 try:
#                     data[field] = translator.translate(getattr(instance, field))
#                     cache.set(cache_key, data[field], timeout=86400)
#                 except Exception as e:
#                     print(f"Translation error for {field}: {e}")
#                     data[field] = getattr(instance, field)
#
#         return data
