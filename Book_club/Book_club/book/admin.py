from django.contrib import admin

from Book_club.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass