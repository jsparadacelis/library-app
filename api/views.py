from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# rest framework
from rest_framework import generics, status
from rest_framework.response import Response
# local
from api.models import Author, Book
from api.serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            book_created = serializer.create(request.data)
            if book_created == {}:
                return Response(book_created, status=status.HTTP_400_BAD_REQUEST)
            return Response(book_created, status=status.HTTP_201_CREATED)
        return Response(None, status=status.HTTP_412_PRECONDITION_FAILED)

class BookDetail(generics.RetrieveAPIView):

    serializer_class = BookSerializer
    def retrieve(self, request, id, *args, **kwargs):
        current_book = Book.objects.get(pk=id)
        serializer = self.get_serializer(current_book)
        return Response(serializer.data)
