from django.urls import path, include
from .views import EventDetail, EventList, AttendanceList, ParticipantDetail \
                    , ParticipantList, UserEventList, EventAttendanceList \
                    , EventParticipantList, UserUpcomingEvent, UserDoneEvent \
                    , AddEventParticipant

from rest_framework.authtoken import views
urlpatterns = [

    path('participant/', ParticipantList.as_view()),
    path('participant/detail/', ParticipantDetail.as_view()),

    path('api-token-auth/', views.obtain_auth_token),

    path('events/', UserEventList.as_view()),
    path('events/upcoming/', UserUpcomingEvent.as_view()),
    path('events/done/', UserDoneEvent.as_view()),

    path('events/all/', EventList.as_view()),
    path('events/detail/<int:event_id>/', EventDetail.as_view()),
    
    path('events/attendance/<int:event_id>/', EventAttendanceList.as_view()),
    path('events/participant/<int:event_id>/', EventParticipantList.as_view()),

    path('attendance/', AttendanceList.as_view()),

    path('events/participant/add/', AddEventParticipant.as_view()),
]