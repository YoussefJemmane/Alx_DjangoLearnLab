from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model that converts Book instances to JSON format
    and handles validation for API requests.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
