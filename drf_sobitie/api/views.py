from datetime import datetime

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from api.serializers import CategorySerializer, EventSerializer, QuestionSerializer, QuizSerializer, QuizResultSerializer, QuoteSerializer
from event.models import Category, Event, Quote
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
