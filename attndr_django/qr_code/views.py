from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


from events.views import Event, Participant, Attendance
from events.serializers import AttendanceSerializer

# Create your views here.
import qrcode
from qrcode.image.svg import SvgImage

from io import BytesIO
import string, random

class ShowQRCode(APIView):
    def get(self, request):
        participant_phone_number = request.data.get("phone_number")
        
        participant = Participant.objects.filter(phone=participant_phone_number).first()
        
        event = Event.objects.filter(id=request.data.get("event_id")).first()
        
        attendance = Attendance.objects.filter(event=event, participant=participant).first()
        
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(attendance.id)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        location = 'qr_code\images\qrcode.png'
        img.save(location)
        return Response({'location' : location})

class QRCodeResponse(APIView):
    def get(self, request):
        participant_phone_number = request.data.get("phone_number")
        participant = Participant.objects.filter(phone=participant_phone_number).first()
        event = Event.objects.filter(id=request.data.get("event_id")).first()
        attendance = Attendance.objects.filter(event=event, participant=participant, time_in__isnull=True).first()
        if attendance is None:
            return Response({"login_message":"Success"})
        return Response({"login_message":"Failed"})






