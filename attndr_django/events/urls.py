from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from .views import EventViewSet

route = DefaultRouter()
route.register('events', EventViewSet)
app_name = 'events'
urlpatterns = [
    path('api/', include(route.urls))
]