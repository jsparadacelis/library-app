from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# local
from api.models import Book

class BookView(View):
    def get(self, request):
        book_list = Book.objects.all()
        book_data = [{'id': book.id, 'title': book.title} for book in book_list]
        return JsonResponse(book_data, safe=False)
