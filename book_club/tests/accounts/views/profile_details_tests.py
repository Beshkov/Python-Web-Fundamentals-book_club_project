from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

UserModel = get_user_model()


class ProfileDetailsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')

    def test_get_details__whenLoggedInUser_shouldGetDetails(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('view profile'))

        books = list(response.context['user_books'])
        # use the same data you give into the "CONTEXT {}" can't name it 'books' when there is 'user_books'
        profile = response.context['profile']

        self.assertListEqual(books, [])
        self.assertEqual(self.user.id, profile.user.id)
