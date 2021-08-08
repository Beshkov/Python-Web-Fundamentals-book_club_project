from django import forms

from Book_club.events.models import Events


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
