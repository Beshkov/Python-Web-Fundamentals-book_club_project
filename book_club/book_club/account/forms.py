from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

# class SignInForm(AuthenticationForm):
#     email = forms.EmailField(
#
#     )
#
#     password = forms.CharField(
#         widget=forms.PasswordInput(),
#     )
#
#     def clean(self):
#         self.user = authenticate(
#             email=self.cleaned_data['email'],
#             password=self.cleaned_data['password'],
#         )
#
#         if not self.user:
#             raise ValidationError('Email and/or password incorrect')
from book_club.account.models import Profile, BookClubUser


class SignInForm(forms.Form):
    user = None
    email = forms.EmailField(
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorrect')

    def save(self):
        return self.user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)


class CreateProfileForm(UserCreationForm):
    class Meta:
        model = BookClubUser
        fields = ['email']
