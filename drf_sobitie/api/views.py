import re
from datetime import datetime

from django.http import JsonResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from drf_sobitie.api.mixins import BaseListCreateDeleteViewSet
from drf_sobitie.api.serializers import (
    EventPostSerializer,
    EventSerializer,
    QuoteSerializer,
    StickerpackSerializer,
    SubscriberSerializer,
)
from drf_sobitie.event.models import Event, Quote, Subscriber
from drf_sobitie.sticker_pack.models import Stickerpack


class StickerpackViewSet(ModelViewSet):
    """Вьюсет для стикеров."""

    queryset = Stickerpack.objects.filter(is_active=True)
    serializer_class = StickerpackSerializer


class EventViewSet(ModelViewSet):
    """Вьюсет для мероприятий."""

    serializer_class = EventSerializer

    def get_queryset(self):
        """Возвращаем только актуальные события."""
        return Event.objects.filter(event_time__gte=datetime.now())


class QuoteViewSet(ModelViewSet):
    """Вьюсет для цитат."""

    # Берем случайный объект модели Quote
    queryset = Quote.objects.order_by("?")[:1]
    serializer_class = QuoteSerializer


class NotificationsViewSet(BaseListCreateDeleteViewSet):
    """Представление для активации/деактивации уведомлений на события и получения всех подписчиков."""

    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    lookup_field = "user_id"


class CheckForSubscription(APIView):
    """Представление для проверки, что конкретный пользователь подписан."""

    def get(self, _: Request, user_id):
        is_subscribed = Subscriber.objects.filter(user_id=user_id).exists()
        return JsonResponse({"is_subscribed": is_subscribed})


class VKView(APIView):
    @staticmethod
    def __remove_not_actual_events(events, vk_posts):
        events.exclude(
            vk_post_id__in=[post["id"] for post in vk_posts]
        ).delete()

    @staticmethod
    def __get_event_data(text):
        descriptions_of_events = [event.description for event in Event.objects.all()]
        if "афиша события" in text.lower() and text not in descriptions_of_events:
            event_time = re.search(r"\d\d\.\d\d\.\d{4} \d{2}:\d{2}", text).group(0)
            event_time = datetime.strptime(event_time, "%d.%m.%Y %H:%M")
            description = text.split("#")[0]
            location = re.search(r"Место события: г.[а-яА-Я-, ]+", text).group(0)

            return {
                "event_time": event_time,
                "location": location,
                "description": description
            }
        return None

    def post(self, request):
        data = self.__get_event_data(text=request.data["text"])
        if data is None:
            return Response(status=status.HTTP_200_OK)
        data["vk_post_id"] = int(request.data["id"])
        serializer = EventPostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        events = Event.objects.order_by("-event_time")
        vk_posts = request.data
        self.__remove_not_actual_events(events, vk_posts)
        for post in vk_posts:
            data = self.__get_event_data(text=post["text"])
            data["vk_post_id"] = post["id"]
            serializer = EventPostSerializer(data=data)
            if not events.filter(vk_post_id=post["id"]).exists():
                if serializer.is_valid():
                    serializer.save()
                continue

            event = events.get(vk_post_id=post["id"])
            if serializer.is_valid():
                event.event_time = data["event_time"]
                event.description = data["description"]
                event.location = data["location"]
                event.save()

        return Response(status=status.HTTP_200_OK)
