from rest_framework import serializers
from .models import Book
from django.forms import ValidationError

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()
#
#     def create(self, data):
#         return Book.objects.create(**data)
#
#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.number_of_pages = data.get('title', instance.number_of_pages)
#         instance.publish_date = data.get('title', instance.publish_date)
#         instance.quantity = data.get('title', instance.quantity)
#         instance.save()
#         return instance


class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

        def get_description(self, data):
            return f"This book is called {data.title} and it is {data.number_of_pages} long."