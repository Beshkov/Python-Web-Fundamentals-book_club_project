from django import forms

from book_club.book_event.models import BookEvent


class BookEventForm(forms.ModelForm):
    class Meta:
        model = BookEvent
        exclude = ('user',)
        fields = '__all__'


class EditBookEventForm(BookEventForm):
    pass

