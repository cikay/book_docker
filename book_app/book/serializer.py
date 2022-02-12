from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('firstname', 'lastname')

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('name', 'author')

