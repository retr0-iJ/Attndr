from rest_framework import serializers
from .models import Event, Participant, Attendance

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Participant
        fields  = '__all__'

class EventSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer(read_only=True, many=True)

    class Meta:
        model   = Event
        fields  = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Attendance
        fields  = '__all__'