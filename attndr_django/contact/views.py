from django.http.response import BadHeaderError, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Contact
from .serializers import ContactUsSerializer
from django.core.mail import send_mail

# Create your views here.

class ContactUsNow(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            first_name = serializer.data.get('first_name')
            last_name = serializer.data.get('last_name')
            full_name = str(first_name) +' ' + str(last_name)
            subject = serializer.data.get('subject')
            from_email = serializer.data.get('email')
            message = serializer.data.get('message')

            message = "\n".join([full_name, from_email, subject, message])

            try:
                #Output cuman di CMD
                send_mail(subject, message, from_email, ['attndr.cs@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                
        return Response({})
