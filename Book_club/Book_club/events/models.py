from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=120)
    event_picture = models.URLField()  # TODO make it into a media
    description = models.CharField(max_length=800)
    duration = models.DurationField()