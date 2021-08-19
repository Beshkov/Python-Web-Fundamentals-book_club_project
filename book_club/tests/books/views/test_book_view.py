from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from book_club.account.admin import UserModel
from book_club.book.models import Book


class BookDetailsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')
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

    def test_get_book_details_if_UserLoggedIn_shouldReturnBook(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('view book', kwargs={
            'pk': self.book.id,
        }))
        book_test = list(Book.objects.filter(user=self.user))[0]

        self.assertEqual(book_test, self.book)
        self.assertTemplateUsed(response, 'book_templates/book-details.html')


