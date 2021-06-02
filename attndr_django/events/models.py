from django.db import models
from django.db import models

class Participant(models.Model):
    name    = models.CharField(max_length=255, null=True)
    email   = models.EmailField(max_length=255, null=True)
    phone   = models.CharField(max_length=20, unique=True)
    city    = models.CharField(max_length=255, null=True)

    REQUIRED_FIELDS = ['name', 'email', 'phone', 'city']

class Event(models.Model):
    event_name      = models.CharField(max_length=255)
    speaker_name    = models.CharField(max_length=255)
    location        = models.CharField(max_length=255,blank=True, null=False)
    date            = models.DateField()
    time_start      = models.TimeField(null=True)
    time_end        = models.TimeField(null=True)
    quota           = models.IntegerField()
    participants    = models.ManyToManyField(Participant, through='Attendance')
    is_done         = models.BooleanField(default=False)

    REQUIRED_FIELDS = [
        'event_name', 
        'speaker_name', 
        'location', 
        'date', 
        'time_start', 
        'time_end',
        'quota', 
        'participants',
        'is_done'
    ]

class Attendance(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event       = models.ForeignKey(Event, on_delete=models.CASCADE)
    time_in     = models.TimeField(null=True)
    time_out    = models.TimeField(null=True)

    REQUIRED_FIELDS = ['participant', 'event', 'time_in', 'time_out']