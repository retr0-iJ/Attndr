from django.urls import path

from .views import ContactUsNow

urlpatterns = [
    path('contact/', ContactUsNow.as_view()),
]