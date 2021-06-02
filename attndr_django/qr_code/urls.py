from django import urls
from django.contrib import admin
from django.urls import path, include 

from .views import ShowQRCode, QRCodeResponse
urlpatterns = [
    
    path('qr_code/<str:event_id>/<str:phone_number>/', ShowQRCode.as_view()),
    path('qr_code/<str:event_id>/<str:phone_number>/<str:token>', QRCodeResponse.as_view()),
]