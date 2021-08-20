import datetime

from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, Client
from django.urls import reverse

from book_club.account.admin import UserModel
from book_club.book_event.models import BookEvent


class TestCreateBookEvents(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')

    def test_to_add_book_club_event_if_UserLoggedIn_should_be_created(self):
        self.client.force_login(self.user)
        self.client.post(reverse('create book event'),
                         data={
                             'title': 'Test_event',
                             'book_picture': 'https://th.bing.com/th/id/R.633bfa78283de791d5d6766d0226421c?rik=fw5Bt7KfHeUyxg&pid=ImgRaw&r=0',
                             'description': 'test test',
                             'duration': '1 day',
                             'expired': False,
                         },
                         follow=True, )

        self.assertEqual(BookEvent.objects.first().title, 'Test_event')
        self.assertEqual(BookEvent.objects.first().book_picture,
                         'https://th.bing.com/th/id/R.633bfa78283de791d5d6766d0226421c?rik=fw5Bt7KfHeUyxg&pid=ImgRaw&r=0')
        self.assertEqual(BookEvent.objects.first().description, 'test test')
        self.assertEqual(BookEvent.objects.first().duration, datetime.timedelta(days=1))
        self.assertEqual(BookEvent.objects.first().expired, False)


    def test_to_add_book_club_event_if_UserLoggedIn_should_redirect(self):
        self.user = AnonymousUser()
        response = self.client.get(reverse('create book event'))

        self.assertEqual(302, response.status_code)

    def test_to_add_book_club_event_if_UserLoggedIn_should_return_to_page(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('create book event'))

        self.assertEqual(200, response.status_code)