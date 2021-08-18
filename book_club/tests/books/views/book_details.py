from django.test import TestCase, Client
from django.urls import reverse

from book_club.account.admin import UserModel
from book_club.book.models import Book


class BookDetails(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')

    def test_add_book_post_view_WhenUserLoggedIn_expect_to_add(self):
        self.client.force_login(self.user)
        self.client.post(
            reverse('add book'),
            data={
                'title': 'test',
                'author': 'test_auth',
                'genre': 'fiction',
                'length': '888 pages',
                'emotional_value': 'neutral',
                'review': 'test',
                'mark': 'neutral',
                'favorite': False,
                'user': self.user,
            },
            follow=True
        )

        self.assertEqual(Book.objects.first().title, 'test')
        self.assertEqual(Book.objects.first().author, 'test_auth')
        self.assertEqual(Book.objects.first().genre, 'fiction')
        self.assertEqual(Book.objects.first().length, '888 pages')
        self.assertEqual(Book.objects.first().emotional_value, 'neutral')
        self.assertEqual(Book.objects.first().review, 'test')
        self.assertEqual(Book.objects.first().mark, 'neutral')
        self.assertEqual(Book.objects.first().favorite, False)
        self.assertEqual(Book.objects.first().user, self.user)

    def test_add_book_ifUserLoggedIn_method_get_should_return_(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('add book'))

        self.assertEqual(200, response.status_code)

    def test_add_book_ifUserLoggedOut_method_get_should_return_(self):

        response = self.client.get(reverse('add book'))

        self.assertEqual(302, response.status_code)
