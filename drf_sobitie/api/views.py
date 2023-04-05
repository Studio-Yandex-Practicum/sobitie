import re
from datetime import datetime
from django.http import JsonResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from api.mixins import BaseListCreateDeleteViewSet

from api.serializers import CategorySerializer, EventPostSerializer, EventSerializer, QuestionSerializer, QuizSerializer, QuizResultSerializer, QuoteSerializer, SubscriberSerializer

from event.models import Event, Quote, Subscriber
from quiz.models import Question, Quiz, QuizResult


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



class QuizViewSet(ModelViewSet):
    """Вьюсет для квизов."""

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @action(method=['GET'])
    def questions(self):
        req = self.request
        quiz_id = req.query_params.get('quiz_id')
        last_question_id = req.query_params.get('last_question_id')
        if quiz_id is None:
            return None
        if last_question_id:
            self.queryset = Quiz.objects.filter(quiz_id=quiz_id).order_by("id")
            return self.queryset
        else:
            self.queryset = Quiz.objects.filter(quiz_id=quiz_id).order_by("id").first()
            return self.queryset


class QuizResultViewSet(ModelViewSet):
    """Вьюсет для результатов квизов."""

    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer


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
