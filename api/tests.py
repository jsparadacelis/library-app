from django.forms.models import model_to_dict
from django.test import Client, TestCase

from api.models import Book


class BookListTest(TestCase):

    def setUp(self):
        self.book_path = '/book'
        self.client = Client()
        self.data_to_test = {
            'title': 'Cien años',
            'subject': 'Drama',
            'author': 'Gabriel Garcia'
        }

    def test_create_success(self):
        response = self.client.post(
            f'{self.book_path}/',
            self.data_to_test
        )
        self.assertEqual(response.status_code, 201)

    def test_create_fail(self):
        data_to_test = self.data_to_test
        data_to_test['author'] = 'fake'*10
        response = self.client.post(
            f'{self.book_path}/',
            data_to_test
        )
        self.assertEqual(response.status_code, 400)


class BookDetailTest(TestCase):

    fixtures = ['book.json']

    def setUp(self):
        self.client = Client()
        self.book_path = '/book'

    def test_get_success(self):
        book_response = self.client.get(
            f'{self.book_path}/1'
        )
        first_book = Book.objects.get(pk=1)
        first_book_as_dict = model_to_dict(
            first_book,
            fields=['author', 'subject', 'title']
        )
        self.assertEqual(book_response.status_code, 200)
        self.assertEqual(book_response.json(), first_book_as_dict)

    def test_delete_success(self):
        book_response = self.client.delete(
            f'{self.book_path}/1'
        )
        self.assertEqual(book_response.status_code, 204)
        self.assertEqual(book_response.content, b'')
