from django import forms

from book_club.book.models import Book


class BooksForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'