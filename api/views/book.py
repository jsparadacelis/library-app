from django.core import exceptions
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Book
from api.serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    """ Books list view, for list and create many books """
    queryset = Book.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        book = {
            'title': request.data.get('title'),
            'subject': request.data.get('subject'),
            'author': request.data.get('author'),
        }
        serializer = self.get_serializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save(book)
            if book_saved == {}:
                return Response(book_saved, status=status.HTTP_400_BAD_REQUEST)
            return Response(book_saved, status=status.HTTP_201_CREATED)
        return Response(None, status=status.HTTP_412_PRECONDITION_FAILED)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Book Detail view, for create, update, get and delete an unique book """

    # permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def get_object(self, id):
        return Book.objects.get(pk=id)

    def get(self, request, id, *args, **kwargs):
        try:
            current_book = self.get_object(id)
            serializer = self.get_serializer(current_book)
            return Response(serializer.data)
        except exceptions.ObjectDoesNotExist as err:
            print(err)
            return Response('NOT FOUND', status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, *args, **kwargs):

        # creates a new dict in order to django will allowed to decide
        # run an updating or a creation
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
        try:
            return self.destroy(request, id, *args, **kwargs)
        except exceptions.ObjectDoesNotExist as err:
            print(err)
            return Response('NOT FOUND', status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, id, *args, **kwargs):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
