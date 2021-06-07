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
        
        print(attendance.id)
        #token = ''.join((random.choice(string.ascii_letters) for x in range(10)))        strLink = '/'+'/'.join([event_id, participant_phone_number, token])+'/'

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(attendance.id)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        location = 'qr_code\images\qrcode.png'
        img.save(location)
        return Response({'location' : location})

from datetime import datetime
import json
from django.core import serializers
#Fix This
class QRCodeResponse(APIView):
    def get(self, request):
        date_now = datetime.now()
        time_in = date_now.strftime("%H:%M:%S")

        attendance = Attendance.objects.filter(id=request.data.get("attendance_id")).first()
        attendance.time_in = time_in
        print(type(attendance))

        #Cara ngupdate attendancenya masi belom nemu
        jsonAttendance = serializers.serialize('json', [attendance, ])
        print(jsonAttendance)
        serializer = AttendanceSerializer(data=jsonAttendance.data)
        if serializer.is_valid():
            #serializer.save()
            print("success")
        else:
            print("failed")
            serializer.errors()

        return Response({})




