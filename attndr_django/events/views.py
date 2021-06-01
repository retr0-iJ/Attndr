from django.db.models.query import QuerySet
from events.form import EventForm
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

from .models import Event

def event_list_view(request):
    queryset = Event.objects.all()
    context = {
        'event_list' : queryset
    }
    
    return render(request, "", context)

def event_single_view(request, id):
    obj = get_object_or_404(Event, id=id)
    
    context = {
        'obj' : obj,
    }
    return render(request, '', context)


def event_delete_view(request, id):
    obj = get_object_or_404(Event, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('')
    
    context = {
        'object' : obj
    }
    #Kalau ga nemu balik ke normal page
    return render(request, '', context)


def event_create_view(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form
    }
    #'go to page createevent & show success createevent 
    # or go to home'
    return render(request, '', context)

    
