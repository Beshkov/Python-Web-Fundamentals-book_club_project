from django.contrib import admin

from book_club.book_event.models import BookEvents


@admin.register(BookEvents)
class ClubEventsAdmin(admin.ModelAdmin):
    pass