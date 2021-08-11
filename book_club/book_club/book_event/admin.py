from django.contrib import admin

from book_club.book_event.models import BookEvent


@admin.register(BookEvent)
class ClubEventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'book_picture', 'description', 'duration', 'expired', 'likes_count', 'dislikes_count')

    def likes_count(self, obj):
        return obj.like_set.count()

    def dislikes_count(self, obj):
        return obj.dislike_set.count()
