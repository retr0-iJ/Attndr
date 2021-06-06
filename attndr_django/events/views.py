from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event, Attendance, Participant
from .serializers import AttendanceSerializer, EventSerializer, ParticipantSerializer


class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class UserEventList(APIView):
    def get(self, request):
        #Validasi user id harus angka
        if request.data.get("event_id") is not None:
            event = Event.objects.filter(id=request.data.get("event_id"))
        else:
            event = Event.objects.filter(user=request.data.get("user_id"))
        serializer = EventSerializer(event, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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

  
