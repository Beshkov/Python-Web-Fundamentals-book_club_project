from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse

from book_club.account.models import BookClubUser
from book_club.book.models import Book
from book_club.book_event.models import BookEvent

UserModel = get_user_model()


class ProfileDetailsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')

    def test_get_details__whenLoggedInUser_without_books_shouldGetDetails(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('view profile'))

        books = list(response.context['user_books'])
        # use the same data you give into the "CONTEXT {}" can't name it 'books' when there is 'user_books'
        profile = response.context['profile']

        self.assertListEqual(books, [])
        self.assertEqual(self.user.id, profile.user.id)

    def test_get_details__whenLoggedInUser_with_books_shouldGetDetails(self):
        self.client.force_login(self.user)
        book = Book.objects.create(
            title='Brothers Karamazov',
            author='Dostoevsky',
            genre='fiction',
            length='824 pages',
            emotional_value='strong book',
            review='very good book',
            favorite=False,
            user=self.user
        )

        response = self.client.get(reverse('view profile'))

        books = list(response.context['user_books'])[0]
        # use the same data you give into the "CONTEXT {}" can't name it 'books' when there is 'user_books'
        profile = response.context['profile']

        self.assertEqual(books, book)
        self.assertEqual(self.user.id, profile.user.id)


    


    # the code bellow test models not Views :
    # def test_profileCreate_whenInvalidInf_shouldRaise(self):
    #     user = BookClubUser(
    #         email='test@email.tt',
    #         password='123qwe!@#',
    #     )
    #
    #     try:
    #         user.full_clean()
    #         user.save()
    #         # self.fail()
    #     except ValidationError as ex:
    #         self.assertIsNotNone(ex)
    #
    # def test_profileCreate_whenValidInf_ShouldCreateIt(self):
    #     user = BookClubUser(
    #         email='test@email.tt',
    #         password='123qwe!@#',
    #     )
    #
    #     user.full_clean()
    #     user.save()
    #     self.assertIsNotNone(user)
    #
    #
    # def test_book_eventCreate_WhenUserLoggedIn_shouldCreateIt(self):
    #     self.client.force_login(self.user)
    #     book_ev = BookEvent(
    #         title= 'test event',
    #         book_picture='https://th.bing.com/th/id/OIP.Yzv6eCg955HV1nZtAiZCHAHaE7?pid=ImgDet&rs=1',
    #         description='test desc',
    #         duration='1 day',
    #         expired=False,
    #         user=self.user,
    #     )
    #
    #     book_ev.full_clean()
    #     book_ev.save()
    #     self.assertIsNotNone(book_ev)
    #
    # def test_book_eventCreate_WhenUserNotLoggedIn_shouldRaiseErr(self):
    #     book_ev = BookEvent(
    #         title= 'test event',
    #         book_picture='https://th.bing.com/th/id/OIP.Yzv6eCg955HV1nZtAiZCHAHaE7?pid=ImgDet&rs=1',
    #         description='test desc',
    #         duration='1 day',
    #         expired=False,
    #         user=self.user,
    #     )
    #
    #     try:
    #         book_ev.full_clean()
    #         book_ev.save()
    #
    #     except ValidationError as ex:
    #         self.assertIsNotNone(ex)
    #
    #
    # def test_bookCreate_WhenUserNotLoggedIn_shouldRaiseErr(self):
    #     book = Book(
    #         title='Brothers Karamazov',
    #         author='Dostoevsky',
    #         genre='fiction',
    #         length='824 pages',
    #         emotional_value='strong book',
    #         review='very good book',
    #         favorite=False,
    #         mark='neutral',
    #         user=self.user
    #     )
    #
    #     try:
    #         book.full_clean()
    #         book.save()
    #
    #     except ValidationError as ex:
    #         self.assertIsNotNone(ex)
    #
    # def test_bookCreate_WhenUserLoggedIn_shouldCreateIt(self):
    #     book = Book(
    #         title='Brothers Karamazov',
    #         author='Dostoevsky',
    #         genre='fiction',
    #         length='824 pages',
    #         emotional_value='strong book',
    #         review='very good book',
    #         favorite=False,
    #         mark='neutral',
    #         user=self.user
    #     )
    #
    #     book.full_clean()
    #     book.save()
    #     self.assertIsNotNone(book)
