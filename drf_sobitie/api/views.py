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
    queryset = Event.objects.all()
    serializer_class = EventSerializer

