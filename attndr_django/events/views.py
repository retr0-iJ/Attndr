from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event, Attendance, Participant
from .serializers import AttendanceSerializer, EventSerializer, ParticipantSerializer

import json

class EventList(APIView):
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class AttendanceList(APIView):
    def get(self, request, format=None):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
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


class CRUDAttendance(APIView):
    def post(self, request, event_id, participant, token):
        # data = {}
        # data['event'] = event_id
        # data['participant'] = '1'
        # #print(Participant.objects.get(phone=participant))
        # data['time_in'] = None
        # data['time_out'] = None

        #Cari cara buat masukin attendance ga pake json
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            None
        else:
            print('invalid')
            print(serializer.errors)
        return Response(serializer.data)
