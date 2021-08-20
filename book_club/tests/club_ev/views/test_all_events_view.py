from django.test import TestCase, Client
from django.urls import reverse

from book_club.account.admin import UserModel
from book_club.book_event.models import BookEvent



class TestAllBookEvents(TestCase):

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

    def test_if_page_can_be_loaded(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('all events'))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'book-events/all-events.html')




