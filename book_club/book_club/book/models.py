from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()

class Book(models.Model):
    MARKS = (
        ('dislike', 'dislike'),
        ('did not like', 'did not like'),
        ('neutral', 'neutral'),
        ('liked', 'liked'),
        ('loved it', 'loved it'),
    )
    GENRE_TYPES = (
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-fiction'),
    )

    title = models.CharField(max_length=35)
    author = models.CharField(max_length=30)
    genre = models.CharField(max_length=11, choices=GENRE_TYPES, default="None")
    length = models.IntegerField()
    audiobook = models.BooleanField(default=False)
    emotional_value = models.TextField(max_length=255)
    review = models.TextField(max_length=1500)
    mark = models.CharField(max_length=12, choices=MARKS)
    favorite = models.BooleanField(default=False)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
