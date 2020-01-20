from rest_framework import serializers
from api.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'subject', 'author']

    def save(self, validated_data):
        author_id = validated_data.pop('author')
        author = Author.objects.get(id=author_id)
        author_data = {'author': author}
        validated_data = {**validated_data, **author_data}
        try:
            book_object = Book(**validated_data)
            book_object.save()
            book_serialized = BookSerializer(validated_data)
            return book_serialized.data
        except Exception as err:
            print(err)
            return {}
