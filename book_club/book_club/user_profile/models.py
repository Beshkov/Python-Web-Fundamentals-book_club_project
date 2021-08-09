from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=16)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='media') # TODO should change to media file
    tell_us_more_about_yourself = models.TextField(max_length=510)
    user_email = models.EmailField()

