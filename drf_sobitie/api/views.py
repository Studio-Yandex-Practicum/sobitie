from datetime import datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from event.models import Category, Event
from api.serializers import CategorySerializer, EventSerializer


class CategoryViewSet(ModelViewSet):
    """Вьюсет для категорий."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EventViewSet(ModelViewSet):
    """Вьюсет для мероприятий."""
    serializer_class = EventSerializer

    def get_queryset(self):
        """Возвращаем только актуальные события."""
        actual_events = Event.objects.filter(event_time__gte=datetime.now())
        return actual_events

