from django.urls import path, include
from events import views

urlpatterns = [
    path('events/', views.EventList.as_view()),
]