from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
import qrcode
from qrcode.image.svg import SvgImage

from io import BytesIO
import string, random

class ShowQRCode(APIView):
    def get(self, request, event_id, phone_number):
        event_id = event_id
        participant_phone_number = phone_number
        token = ''.join((random.choice(string.ascii_letters) for x in range(10)))
        strLink = '/'+'/'.join([event_id, participant_phone_number, token])+'/'
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(strLink)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        #img.save('qrcode001.png')
        return Response({})

class QRCodeResponse(APIView):
    def post(self, request, event_id, phone_number, token):

        print(event_id)
        print(phone_number)
        print(token)
        #Add participant into participant table
        #Add attendance into attendance table
        return Response({})




