from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# rest framework
from rest_framework import generics
from rest_framework.response import Response
# local
from api.models import Book
from api.serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):

    serializer_class = BookSerializer
    def retrieve(self, request, id, *args, **kwargs):
        current_book = Book.objects.get(pk=id)
        serializer = self.get_serializer(current_book)
        return Response(serializer.data)
