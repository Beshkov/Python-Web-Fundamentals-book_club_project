from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from book_club.account.managers import BookClubUserManager


class BookClubUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,

    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = BookClubUserManager()


class Profile(models.Model):

    profile_image = models.ImageField(
        upload_to='user_profile_picture',
        blank=True,
    )

    user = models.OneToOneField(
        BookClubUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.user}'

    # def delete(self, *args, **kwargs):
    #
    #     self.profile_image.delete()
    #     self.user.delete()
    #
    #     super().delete(*args, **kwargs)  # Call the "real" save() method.




from .signals import *
