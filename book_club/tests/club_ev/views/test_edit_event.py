
from django.test import TestCase, Client
from django.urls import reverse

from book_club.account.admin import UserModel
from book_club.book_event.models import BookEvent


class TestEditBookEvents(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')
        self.book_event = BookEvent.objects.create(
            title='Test_event',
            book_picture='https://th.bing.com/th/id/R.633bfa78283de791d5d6766d0226421c?rik=fw5Bt7KfHeUyxg&pid=ImgRaw&r=0',
            description='test test',
            duration='1 day',
            expired=False,
            user=self.user,
        )

    def test_if_pages_can_be_reached_by_a_LoggedInUser_it_should_return_StatusCode_200(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('edit club event', kwargs={
            'pk': self.book_event.id,
        }))

        self.assertEqual(200, response.status_code)

    def test_if_it_can_edit_event_if_UserLoggedIn_should_edit_it(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('edit club event', kwargs={
            'pk': self.book_event.id,
        }), data={
            'title': 'Test_event_edit',
            'book_picture': 'https://th.bing.com/th/id/R.633bfa78283de791d5d6766d0226421c?rik=fw5Bt7KfHeUyxg&pid=ImgRaw&r=0',
            'description': 'test test edit',
            'duration': '1 day',
            'expired': True,
        },
        follow=True, )

        self.assertEqual(BookEvent.objects.first().title, 'Test_event_edit')
        self.assertEqual(BookEvent.objects.first().book_picture,
                         'https://th.bing.com/th/id/R.633bfa78283de791d5d6766d0226421c?rik=fw5Bt7KfHeUyxg&pid=ImgRaw&r=0')
        self.assertEqual(BookEvent.objects.first().description, 'test test edit')
        self.assertEqual(BookEvent.objects.first().expired, True)

