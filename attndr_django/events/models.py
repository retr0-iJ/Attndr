from django.db import models
from django.db import models
from django.db.models.query import FlatValuesListIterable


class Event(models.Model):
    event_name       = models.CharField(max_length=255)
    speaker_name    = models.CharField(max_length=255)
    location        = models.CharField(max_length=255)
    date            = models.DateField(null=True)
    time            = models.TimeField(null=True)
    




