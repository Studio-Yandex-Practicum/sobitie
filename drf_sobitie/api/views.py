from datetime import datetime

from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import CategorySerializer, EventSerializer, QuoteSerializer, SubscriberSerializer
from event.models import Category, Event, Quote, Subscriber


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


class QuoteViewSet(ModelViewSet):
    """Вьюсет для цитат."""

    queryset = Quote.objects.order_by("-add_time")[:1]
    serializer_class = QuoteSerializer


class NotificationsView(ListCreateAPIView):
    """Представление для активации уведомлений на события и получения всех подписчиков."""

    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class CheckForSubscription(APIView):
    """Представление для проверки, что конкретный пользователь подписан."""

    def get(self, _: Request, user_id):
        is_subscribed = Subscriber.objects.filter(user_id=user_id).exists()
        return JsonResponse({"is_subscribed": is_subscribed})
