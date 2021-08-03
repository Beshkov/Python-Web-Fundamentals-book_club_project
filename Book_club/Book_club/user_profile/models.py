from django.db import models


class UserProfile(models.Model):
    user_name = models.CharField(max_length=16)
    age = models.IntegerField()
    profile_picture = models.URLField  # TODO should change to media file
    tell_us_more_about_yourself = models.CharField(max_length=510)
    user_email = models.EmailField()
