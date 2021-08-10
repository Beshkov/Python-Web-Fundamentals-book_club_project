import os
from os.path import join

from django import forms
from django.conf import settings

from book_club.user_profile.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class EditProfileForm(UserProfileForm):

    def save(self, commit=True):
        db_user_profile = UserProfile.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, db_user_profile.profile_picture.url[len('/media/'):])
            os.remove(image_path)
        return super().save(commit)
