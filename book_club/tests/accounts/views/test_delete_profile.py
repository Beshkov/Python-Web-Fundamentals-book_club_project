from django.contrib.auth import get_user_model

from django.test import TestCase, Client
from django.urls import reverse



UserModel = get_user_model()


class ProfileDetailsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')


    def test_get_on_delete_profile_shouldDelete(self):
        """ go to delete user profile form"""

        self.client.force_login(self.user)

        response = self.client.get(reverse('delete profile'))

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'accounts/delete-profile.html')

    def test_post_on_delete_profile_shouldDelete(self):
        """redirect to home"""

        self.client.force_login(self.user)

        response = self.client.post(reverse('delete profile'))

        self.assertEqual(302, response.status_code)
