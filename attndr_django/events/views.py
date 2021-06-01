from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from .models import Event
from .serializer import EventSerializer

class EventDetail(APIView):
    def get(self, request):
        None

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
