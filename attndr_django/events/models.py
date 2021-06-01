from django.db import models
from django.db import models
from django.db.models.query import FlatValuesListIterable


class Event(models.Model):
    event_name      = models.CharField(max_length=50)
    speaker_name    = models.CharField(max_length=50)
    location        = models.TextField(blank=True, null=False)
    date            = models.DateField(auto_now=True)
    time            = models.TimeField(auto_now=True)
    




