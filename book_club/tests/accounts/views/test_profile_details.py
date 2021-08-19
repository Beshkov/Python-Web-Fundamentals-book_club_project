import random
import shutil
from os.path import join
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from book_club.account.models import Profile


UserModel = get_user_model()


class ProfileDetailsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='alex_b@gmail.com', password='asd123!@#')

    def test_get_details__whenLoggedInUser_without_books_shouldGetDetails(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('view profile'))

        """
        use the same data you give into the "CONTEXT {}" can't name it 'books' when there is 'user_books'
        """

        profile = response.context['profile']

        self.assertEqual(self.user.id, profile.user.id)
        self.assertTemplateUsed(response, 'accounts/user_profile.html')

    def test_postDetails_when_userLoggedInWithoutImage_shouldChangeImage(self):
        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test_image.jpg')
        file_name = f'{random.randint(1, 10000)}-test_image.jpg'
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpeg',
        )

        self.client.force_login(self.user)

        response = self.client.post(reverse('view profile'), data={
            'profile_image': file,
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
        self.assertTrue(str(profile.profile_image).endswith(file_name))

