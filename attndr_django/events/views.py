from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event, Attendance, Participant
from .serializers import AttendanceSerializer, EventSerializer, ParticipantSerializer

from rest_framework.authtoken.models import Token

from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.parsers import MultiPartParser
import pandas, json

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
        headerToken = request.headers.get('Authorization')
        token = Token.objects.get(key = headerToken.split()[1])
        request.data['user'] = token.user_id
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
    

class UserUpcomingEvent(APIView):
    def get(self, request):
        headerToken = request.headers.get('Authorization')
        token = Token.objects.get(key = headerToken.split()[1])
        events = Event.objects.filter(user=token.user_id, is_done=False)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class UserDoneEvent(APIView):
    def get(self, request):
        headerToken = request.headers.get('Authorization')
        token = Token.objects.get(key = headerToken.split()[1])
        events = Event.objects.filter(user=token.user_id, is_done=True)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventDetail(APIView):
    def get(self, request, event_id):
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
    def get(self, request, event_id):
        event = Event.objects.filter(id=event_id)
        participant = event.first().participants.all()
        serializer = ParticipantSerializer(data=participant, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class AddEventParticipant(APIView):
    parser_classes = (MultiPartParser, )
    def post(self, request, format=None):
        file_obj = request.data["file"]
        excel = pandas.read_excel(file_obj, sheet_name='Sheet1', converters={'phone': str})
        excel_json = excel.to_json(orient='records')
        excel_json = list(eval(excel_json))
        event_id = int(request.data['event_id'])
        participant_id = []
        for d in excel_json:
            serializer = ParticipantSerializer(data=d)
            if serializer.is_valid():
                serializer.save()
                participant_id.append(serializer.data['id'])
            else:
                instance = get_object_or_404(Participant.objects.all(), phone=d['phone'])
                update_serializer = ParticipantSerializer(instance, data=d)
                if update_serializer.is_valid():
                    update_serializer.save()
                    participant_id.append(update_serializer.data['id'])

        for p in participant_id:
            dicAttendance = {}
            dicAttendance['participant'] = p
            dicAttendance['event'] = event_id
            attendanceJson = json.dumps(dicAttendance)
            attendanceJson = eval(attendanceJson)

            
            attendance = Attendance.objects.filter(event=attendanceJson['event'], participant=attendanceJson['participant']).first()
            if attendance is None:
                serializer = AttendanceSerializer(data=attendanceJson)
                if serializer.is_valid():
                    serializer.save()
            else:
                instance = attendance
                update_serializer = AttendanceSerializer(instance, data=p)
                if update_serializer.is_valid():
                    update_serializer.save()
        return Response({'Adding Success' : 'True'})
