from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class BookEvent(models.Model):
    title = models.CharField(max_length=120)
    book_picture = models.URLField()
    description = models.TextField(max_length=800)
    duration = models.DurationField()
    expired = models.BooleanField(default=False)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    event = models.ForeignKey(BookEvent, on_delete=models.CASCADE)


class Dislike(models.Model):
    event = models.ForeignKey(BookEvent, on_delete=models.CASCADE)
