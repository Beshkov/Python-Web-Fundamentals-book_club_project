from django.db import models


class Book(models.Model):
    LIKES = (
        ('1', 'dislike'),
        ('2', 'did not like'),
        ('3', 'neutral'),
        ('4', 'liked'),
        ('5', 'loved it'),
    )
    title = models.CharField(max_length=35)
    author = models.CharField(max_length=30)
    audiobook = models.BooleanField(default=False)
    length = models.CharField(max_length=10)
    emotional_value = models.TextField(max_length=255)
    review = models.TextField(max_length=1500)
    mark = models.CharField(max_length=1, choices=LIKES)
    private = models.BooleanField(default=False)
