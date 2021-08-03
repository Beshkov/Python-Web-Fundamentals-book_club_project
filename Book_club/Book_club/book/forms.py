from django import forms

from Book_club.book.models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'