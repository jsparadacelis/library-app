from django.core.management import call_command
from django.test import Client, TestCase

from api import models


class BookListTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.data_to_test = {
            'title': 'Cien años',
            'subject': 'Drama',
            'author': 'Gabriel Garcia'
        }
        self.book_path = '/book/'

    def test_create_success(self):
        response = self.client.post(
            f'{self.book_path}',
            self.data_to_test
        )
        self.assertEqual(response.status_code, 201)

    def test_create_fail(self):
        data_to_test = self.data_to_test
        data_to_test['author'] = 'fake'*10
        response = self.client.post(
            f'{self.book_path}',
            data_to_test
        )
        self.assertEqual(response.status_code, 400)

class BookDetailTest(TestCase):

    def setUp(self):
        call_command('loaddata', 'fixtures/book_fixtures.yaml', verbosity=0)
        self.client = Client()
        self.book_path = '/book/'

    def test_get_success(self):
        response = self.client.get(
            f'{self.book_path}'
        )
        self.assertEqual(response.status_code, 200)
