import re
from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import EventPostSerializer, EventSerializer, QuoteSerializer
from event.models import Event, Quote


class EventViewSet(ModelViewSet):
    """Вьюсет для мероприятий."""

    serializer_class = EventSerializer

    def get_queryset(self):
        """Возвращаем только актуальные события."""
        actual_events = Event.objects.filter(event_time__gte=datetime.now())
        return actual_events


class QuoteViewSet(ModelViewSet):
    """Вьюсет для цитат."""

    queryset = Quote.objects.order_by("-add_time")[:1]
    serializer_class = QuoteSerializer


class VKView(APIView):
    def common(self, text):
        events = [event.description for event in Event.objects.all()]
        if "афиша собития" in text.lower() and text not in events:
            event_time = re.search(r"\d\d\.\d\d\.\d{4} \d{2}:\d{2}", text).group(0)
            event_time = datetime.strptime(event_time, "%d.%m.%Y %H:%M")
            description = text.split("#")[0]
            location = re.search(r"Место события: г.[а-яА-Я-, ]+", text).group(0)
            return event_time, description, location
        else:
            return None

    def post(self, request):
        data = dict(request.data)
        vk_post_id = int(data["id"][0])
        data = self.common(text=data["text"][0])
        if data is None:
            return Response(status=status.HTTP_200_OK)
        event_time, description, location = data
        data = {
            "event_time": event_time,
            "location": location,
            "description": description,
            "vk_post_id": vk_post_id,
        }
        serializer = EventPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        event_time, description, location = self.common(text=request["text"])
        vk_post_id = request["id"]
        event = Event.objects.get(vk_post_id=pk)
        data = {
            "event_time": event_time,
            "location": location,
            "description": description,
            "vk_post_id": vk_post_id,
        }
        serializer = EventPostSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
