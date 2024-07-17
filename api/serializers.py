from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(write_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if not data.get('author_name'):
            raise serializers.ValidationError("Author name is required.")
        return data

    def create(self, validated_data):
        author_name = validated_data.pop('author_name')
        author, created = Author.objects.get_or_create(name=author_name)
        book = Book.objects.create(author=author, **validated_data)
        return book
