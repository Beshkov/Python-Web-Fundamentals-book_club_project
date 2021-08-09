from django.db import models


class BookEvents(models.Model):
    title = models.CharField(max_length=120)
    book_picture = models.URLField()
    description = models.TextField(max_length=800)
    duration = models.DurationField()
    expired = models.BooleanField(default=False)
