from django.test import TestCase, Client
from django.urls import reverse

from book_club.account.admin import UserModel
from book_club.book.models import Book


class BookRemoveTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')

    def test_remove_book_post_view_WhenUserLoggedIn_expect_to_redirect_to_Home(self):
        self.client.force_login(self.user)
        self.book = Book.objects.create(
            title='Test',
            author='Test_Auth',
            genre='fiction',
            length=888,
            audiobook=False,
            emotional_value='neutral',
            review='test',
            mark='neutral',
            favorite=False,
            user=self.user,
        )

        request = self.client.post(reverse('remove book', kwargs={
          'pk': self.book.id,
        }, ))

        self.assertEqual(302, request.status_code)

    def test_remove_book_get_view_WhenUserLoggedIn_expect_to_remove(self):
        self.client.force_login(self.user)
        self.book = Book.objects.create(
            title='Test',
            author='Test_Auth',
            genre='fiction',
            length=888,
            audiobook=False,
            emotional_value='neutral',
            review='test',
            mark='neutral',
            favorite=False,
            user=self.user,
        )

        request = self.client.get(reverse('remove book', kwargs={
          'pk': self.book.id,
        }))

        self.assertEqual(200, request.status_code)



