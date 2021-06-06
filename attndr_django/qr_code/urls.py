from django import urls
from django.contrib import admin
from django.urls import path, include 

from .views import ShowQRCode, QRCodeResponse

urlpatterns = [
    
    path('qr_code/', ShowQRCode.as_view()),
    path('qr_code/response/', QRCodeResponse.as_view()),
]
