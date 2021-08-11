from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class SignInForm(forms.Form):
    user = None
    username = forms.CharField(
        max_length=16,
    )

    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Incorrect logging details. (Username or/and password)!')

    def save(self):
        return self.user
