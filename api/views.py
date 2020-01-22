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
            book_saved = serializer.save(request.data)
            if book_saved == {}:
                return Response(book_saved, status=status.HTTP_400_BAD_REQUEST)
            return Response(book_saved, status=status.HTTP_201_CREATED)
        return Response(None, status=status.HTTP_412_PRECONDITION_FAILED)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = BookSerializer

    def get_object(self, id):
        return Book.objects.get(pk=id)

    def get(self, request, id, *args, **kwargs):
        current_book = self.get_object(id)
        serializer = self.get_serializer(current_book)
        return Response(serializer.data)

    def put(self, request, id, *args, **kwargs):
        book_data = {
            'id': id
        }
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            book_data = {**book_data, **request.data}
            book_saved = serializer.save(book_data)
            if book_saved == {}:
                return Response(book_saved, status=status.HTTP_400_BAD_REQUEST)
            return Response(book_saved, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_412_PRECONDITION_FAILED)
    
    def delete(self, request, id, *args, **kwargs):
        return self.destroy(request, id, *args, **kwargs)
    
    def destroy(self, request, id, *args, **kwargs):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
