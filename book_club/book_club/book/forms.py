from django import forms

from book_club.book.models import Book


class BooksForms(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)
        fields = '__all__'


class CreateBookForm(BooksForms):
    pass


class EditBookForm(BooksForms):
    pass


class DeleteBookForm(BooksForms):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
