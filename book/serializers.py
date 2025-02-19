from rest_framework import serializers
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
