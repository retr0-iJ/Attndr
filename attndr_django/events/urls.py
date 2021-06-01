from django.urls import path

from events.views import (
    event_list_view,
    event_single_view,
    event_create_view,
    event_delete_view,

)

app_name = 'events'

urlpatterns = [
    path('', event_list_view, name='event_list'),
    path('<int:id>/', event_single_view, name='event_detail'), 
    path('create/', event_create_view, name='event_create'),
    path('<int:id>/delete/', event_delete_view, name='event_delete'),



]