from rest_framework import serializers
from deep_translator import GoogleTranslator
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    pdf = serializers.FileField(required=False)
    cover_image = serializers.ImageField(required=False)

    class Meta:
        model = Book
        fields = '__all__'

class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'pdf', 'cover_image']





class BookRussianSerializer(serializers.ModelSerializer):
    title = serializers.CharField()

    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Translate the title to Russian
        translator = GoogleTranslator(source='auto', target='ru')
        data['title'] = translator.translate(instance.title)

        return data


class BookEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Translate the title to English
        translator = GoogleTranslator(source='auto', target='en')
        data['title'] = translator.translate(instance.title)

        return data

