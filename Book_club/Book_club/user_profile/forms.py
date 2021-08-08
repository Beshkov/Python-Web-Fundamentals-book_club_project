from django import forms

from Book_club.user_profile.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
