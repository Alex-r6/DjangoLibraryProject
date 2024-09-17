from rest_framework import serializers
from .models import *


class BookSerializer2(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['title', 'genres']


class AuthorSerializer1(serializers.ModelSerializer):
    # books = serializers.StringRelatedField(many=True)
    books = BookSerializer2(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', '__str__', 'info', 'portrait', 'books']


class AuthorSerializer2(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['__str__', 'books']


class BookSerializer1(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', ]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class GenreSerializer2(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Genre
        fields = ['name', 'books']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer2(serializers.ModelSerializer):
    book = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['username', 'text', 'book']
