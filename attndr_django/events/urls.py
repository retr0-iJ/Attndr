from django.urls import path, include
from .views import EventList, AttendanceList, ParticipantList

urlpatterns = [
    path('events/', EventList.as_view()),
    path('events/attendance/', AttendanceList.as_view()),
    path('events/participant/', ParticipantList.as_view()),
]