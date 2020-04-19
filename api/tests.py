from django.test import Client, TestCase


class BookListTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.data_to_test = {
            'title': 'Cien años',
            'subject': 'Drama',
            'author': 'Gabriel Garcia'
        }

    def test_create_success(self):
        response = self.client.post(
            '/book/',
            self.data_to_test
        )
        self.assertEqual(response.status_code, 201)

    def test_create_fail(self):
        data_to_test = self.data_to_test
        data_to_test['author'] = 'fake'*10
        response = self.client.post(
            '/book/',
            data_to_test
        )
        self.assertEqual(response.status_code, 400)
