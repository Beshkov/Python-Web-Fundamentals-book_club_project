from django.db import models


class BookEvent(models.Model):
    title = models.CharField(max_length=120)
    book_picture = models.URLField()
    description = models.TextField(max_length=800)
    duration = models.DurationField()
    expired = models.BooleanField(default=False)


class Like(models.Model):
    event = models.ForeignKey(BookEvent, on_delete=models.CASCADE)


class Dislike(models.Model):
    event = models.ForeignKey(BookEvent, on_delete=models.CASCADE)
