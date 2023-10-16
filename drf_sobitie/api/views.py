import re
from datetime import datetime

import requests
from django.http import JsonResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.mixins import BaseListCreateDeleteViewSet
from api.serializers import (
    EventPostSerializer,
    EventSerializer,
    QuestionSerializer,
    QuizResultSerializer,
    QuizSerializer,
    QuoteSerializer,
    StickerpackSerializer,
    SubscriberSerializer,
)
from event.models import Event, Quote, Subscriber
from quiz.models import Question, Quiz, QuizResult
from sticker_pack.models import Stickerpack


class StickerpackViewSet(ModelViewSet):
    """Вьюсет для стикеров."""

    queryset = Stickerpack.objects.all()
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


class QuizViewSet(ModelViewSet):
    """Вьюсет для квизов."""
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizResultViewSet(ModelViewSet):
    """Вьюсет для результатов квизов."""
    serializer_class = QuizResultSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        correct_answer_count = int(self.request.query_params.get("correct_answer_count"))
        if correct_answer_count:
            return [QuizResult.objects.filter(
                quiz_id=quiz_id,
                correct_answer_cnt__lte=correct_answer_count
            ).first()]
        return [QuizResult.objects.filter(
            quiz_id=quiz_id,
            correct_answer_cnt__gte=correct_answer_count
        ).last()]


class QuestionQuizViewSet(ModelViewSet):
    """Вьюсет для вопросов."""
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        last_question_id = self.request.query_params.get("last_question_id")
        if last_question_id:
            return Question.objects.filter(
                quiz_id=quiz_id, id=int(last_question_id)+1
            )
        return [
            Question.objects.filter(
                quiz_id=quiz_id
            ).order_by("id").first()
        ]


class QuestionViewSet(ModelViewSet):
    """Вьюсет для вопросов."""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


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
    def common(self, text):
        events = [event.description for event in Event.objects.all()]
        if "афиша события" in text.lower() and text not in events:
            event_time = re.search(r"\d\d\.\d\d\.\d{4} \d{2}:\d{2}", text).group(0)
            event_time = datetime.strptime(event_time, "%d.%m.%Y %H:%M")
            description = text.split("#")[0]
            location = re.search(r"Место события: г.[а-яА-Я-, ]+", text).group(0)
            return event_time, description, location
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def remove_not_actual_events(self, vk_posts):
        events = Event.objects.all()
        events_to_delete = [event for event in events if
                            event.vk_post_id not in [post["id"] for post in vk_posts["items"]]]
        for event in events_to_delete:
            event.delete()

    def update_events(self, vk_posts):
        events = Event.objects.order_by("-event_time")
        self.remove_not_actual_events(vk_posts)
        for post in vk_posts["items"]:
            request_data = {"text": post["text"], "id": post["id"]}
            if not events.filter(vk_post_id=post["id"]).exists():
                url = reverse("events-list")
                requests.post(url, data=request_data)
                continue
            event = events.get(vk_post_id=post["id"])
            event_date = event.event_time
            current_date = datetime.now()
            post_text = post["text"].split("#")[0].rstrip()
            if not (event_date < current_date) and (post_text != event.description):
                url = reverse("events-detail", kwargs={"pk": post["id"]})
                self.put(request_data, pk=post["id"])
            continue