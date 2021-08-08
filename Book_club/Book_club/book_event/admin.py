from django.contrib import admin

from book_club.book_event.models import ClubEvents


@admin.register(ClubEvents)
class ClubEventsAdmin(admin.ModelAdmin):
    pass