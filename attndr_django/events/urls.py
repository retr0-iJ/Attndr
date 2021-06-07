from django.urls import path, include
from .views import EventList, AttendanceList, ParticipantList, UserEventList, EventAttendanceList, EventParticipantList

from rest_framework.authtoken import views
urlpatterns = [
    path('events/all/', EventList.as_view()),
    #path('events/attendance/', AttendanceList.as_view()),
    path('participant/', ParticipantList.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    #path('events/attendance/<str:event_id>/<str:participant>/<str:token>/', CRUDAttendance.as_view()),

    path('events/', UserEventList.as_view()),
    path('events/attendance/', EventAttendanceList.as_view()),
    path('events/participant/', EventParticipantList.as_view()),
]