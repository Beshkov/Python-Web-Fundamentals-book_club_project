from django import forms

from book_club.book_event.models import BookEvent


class BookEventForm(forms.ModelForm):
    class Meta:
        model = BookEvent
        exclude = ('user', 'date_of_creation')
        fields = '__all__'


class EditBookEventForm(BookEventForm):
    pass

