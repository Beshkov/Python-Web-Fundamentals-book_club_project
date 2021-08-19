from django.core.exceptions import ValidationError
from django.test import TestCase, Client

from book_club.account.admin import UserModel
from book_club.account.models import BookClubUser
from book_club.book.models import Book
from book_club.book_event.models import BookEvent


class ProfileModelsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')


    def test_profileCreate_whenInvalidInf_shouldRaise(self):
        user = BookClubUser(
            email='test@email.tt',
            password='123qwe!@#',
        )

        try:
            user.full_clean()
            user.save()
            # self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_profileCreate_whenValidInf_ShouldCreateIt(self):
        user = BookClubUser(
            email='test@email.tt',
            password='123qwe!@#',
        )

        user.full_clean()
        user.save()
        self.assertIsNotNone(user)


    def test_book_eventCreate_WhenUserLoggedIn_shouldCreateIt(self):
        self.client.force_login(self.user)
        book_ev = BookEvent(
            title= 'test event',
            book_picture='https://th.bing.com/th/id/OIP.Yzv6eCg955HV1nZtAiZCHAHaE7?pid=ImgDet&rs=1',
            description='test desc',
            duration='1 day',
            expired=False,
            user=self.user,
        )

        book_ev.full_clean()
        book_ev.save()
        self.assertIsNotNone(book_ev)

    def test_book_eventCreate_WhenUserNotLoggedIn_shouldRaiseErr(self):
        book_ev = BookEvent(
            title= 'test event',
            book_picture='https://th.bing.com/th/id/OIP.Yzv6eCg955HV1nZtAiZCHAHaE7?pid=ImgDet&rs=1',
            description='test desc',
            duration='1 day',
            expired=False,
            user=self.user,
        )

        try:
            book_ev.full_clean()
            book_ev.save()

        except ValidationError as ex:
            self.assertIsNotNone(ex)


    def test_bookCreate_WhenUserNotLoggedIn_shouldRaiseErr(self):
        book = Book(
            title='Brothers Karamazov',
            author='Dostoevsky',
            genre='fiction',
            length=824,
            emotional_value='strong book',
            review='very good book',
            favorite=False,
            mark='neutral',
            user=self.user
        )

        try:
            book.full_clean()
            book.save()

        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_bookCreate_WhenUserLoggedIn_shouldCreateIt(self):
        book = Book(
            title='Brothers Karamazov',
            author='Dostoevsky',
            genre='fiction',
            length=824,
            emotional_value='strong book',
            review='very good book',
            favorite=False,
            mark='neutral',
            user=self.user
        )

        book.full_clean()
        book.save()
        self.assertIsNotNone(book)
