from django.urls import path, include
from .views import EventList, AttendanceList, ParticipantList, CRUDAttendance



urlpatterns = [
    path('events/', EventList.as_view()),
    path('events/attendance/', AttendanceList.as_view()),
    path('events/participant/', ParticipantList.as_view()),

    path('events/attendance/<str:event_id>/<str:participant>/<str:token>/', CRUDAttendance.as_view()),

]