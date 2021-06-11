from django.urls import path, include
from .views import EventDetail, EventList, AttendanceList, ParticipantDetail, ParticipantList, UserEventList, EventAttendanceList, EventParticipantList

from rest_framework.authtoken import views
urlpatterns = [

    path('participant/', ParticipantList.as_view()),
    path('participant/detail/', ParticipantDetail.as_view()),

    path('api-token-auth/', views.obtain_auth_token),

    path('events/', UserEventList.as_view()),
    path('events/all/', EventList.as_view()),
    path('events/detail/', EventDetail.as_view()),
    
    path('events/attendance/', EventAttendanceList.as_view()),
    path('events/participant/', EventParticipantList.as_view()),
]