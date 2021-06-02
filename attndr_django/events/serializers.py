from rest_framework import serializers
from .models import Event, Participant, Attendance

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Participant
        fields  = (
            "id",
            "name",
            "email",
            "phone",
            "city"
        )

class EventSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer(read_only=True, many=True)

    class Meta:
        model   = Event
        fields  = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Attendance
        fields  = (
            "id",
            "participant",
            "event",
            "time_in",
            "time_out"
        )