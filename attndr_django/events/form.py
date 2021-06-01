from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    event_name      = forms.CharField(max_length=50, label='Event Name')
    speaker_name    = forms.CharField(max_length=50, label='Speaker Name')
    location        = forms.CharField(max_length=120, label='Location')
    date            = forms.DateField(auto_now=True, label='Date')
    time            = forms.TimeField(auto_now=True, label='Time')

    class Meta:
        model = Event
        fields = [
            'event_name',
            'speaker_name',
            'location',
            'date',
            'time',
        ]