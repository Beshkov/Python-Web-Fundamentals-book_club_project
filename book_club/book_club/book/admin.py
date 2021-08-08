from django.contrib import admin

from book_club.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass