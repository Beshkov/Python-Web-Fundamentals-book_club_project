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
    # username = models.CharField(
    #     max_length=25,
    #     unique=True,
    # ) #TODO implement later on

    profile_image = models.ImageField(
        upload_to='user_profile_picture',
        blank=True,
    )

    user = models.OneToOneField(
        BookClubUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

from .signals import *
