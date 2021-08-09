from django import forms

from book_club.book_event.models import BookEvents


class BookEventForm(forms.ModelForm):
    class Meta:
        model = BookEvents
        fields = '__all__'
