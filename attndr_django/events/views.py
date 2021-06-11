from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event, Attendance, Participant
from .serializers import AttendanceSerializer, EventSerializer, ParticipantSerializer

from rest_framework.authtoken.models import Token

from django.shortcuts import get_list_or_404, get_object_or_404

class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class UserEventList(APIView):
    def get(self, request):
        headerToken = request.headers.get('Authorization')
        token = Token.objects.get(key = headerToken.split()[1])
        events = Event.objects.filter(user=token.user_id)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request):
        event_id = request.data.get('event_id')
        instance = get_object_or_404(Event.objects.all(), pk=event_id)
        serializer = EventSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)

    def delete(self, request):
        event_id = request.data.get('event_id')
        event = get_object_or_404(Event.objects.all(), pk=event_id)
        event.delete()
        return Response({})
    


class EventDetail(APIView):
    def get(self, request):
        event_id = request.data.get('event_id')
        event = Event.objects.get(id=event_id)
        serializer = EventSerializer(event)
        
        return Response(serializer.data)
    
    


class AttendanceList(APIView):
    def get(self, request):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)


class EventAttendanceList(APIView):
    def get(self, request):
        #Validasi user id harus angka
        attendance = Attendance.objects.filter(event=request.data.get("event_id"))
        serializer = AttendanceSerializer(attendance, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class ParticipantList(APIView):
    def get(self, request, format=None):
        participant = Participant.objects.all()
        serializer = ParticipantSerializer(participant, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class ParticipantDetail(APIView):
    def get(self, request, format=None):
        participant = Participant.objects.get(phone_number=request.data.get('phone_number'))
        serializer = ParticipantSerializer(participant)
        return Response(serializer.data)


class EventParticipantList(APIView):
    def get(self, request, format=None):
        event = Event.objects.filter(id=request.data.get("event_id"), user=request.data.get("user_id"))
        participant = event.first().participants.all()
        #print(event.first().participants.all())
        serializer = ParticipantSerializer(data=participant, many=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

  
