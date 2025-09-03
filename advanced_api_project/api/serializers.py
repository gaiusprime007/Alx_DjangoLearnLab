from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

#Book serializer 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # with custom validation to check publication date is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            return serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
#Since BookSerializer is defined after AuthorSerializer, we use a string reference here
    books = BookSerializer(many=True, read_only=True, source='author')

    class Meta:
        model = Author
        fields = ['name', 'books']
