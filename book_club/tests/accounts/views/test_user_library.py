import random
from os.path import join
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from book_club.account.models import Profile
from book_club.book.models import Book


UserModel = get_user_model()


class ProfileLibraryTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')

    def test_get_library__whenLoggedInUser_with_books_shouldGetDetails(self):
        self.client.force_login(self.user)
        book = Book.objects.create(
            title='Brothers Karamazov',
            author='Dostoevsky',
            genre='fiction',
            length=824,
            emotional_value='strong book',
            review='very good book',
            favorite=False,
            user=self.user
        )

        response = self.client.get(reverse('user library'))

        books = list(response.context['books'])[0]
        # use the same data you give into the "CONTEXT {}" can't name it 'books' when there is 'user_books'
        profile = response.context['user']

        self.assertEqual(books, book)
        self.assertEqual(self.user.id, profile.user.id)

    def test_get_library__whenLoggedInUser_without_books_shouldGetDetails(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('user library'))

        books = list(response.context['books'])

        """
        use the same data you give into the "CONTEXT {}" can't name it 'books' when there is 'user_books'
        """

        profile = response.context['user']

        self.assertListEqual(books, [])
        self.assertEqual(self.user.id, profile.user.id)