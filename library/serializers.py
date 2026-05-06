from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """A class to represent a book serializer"""
    class Meta:
        model = Book
        fields = '__all__'