from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer, StringRelatedField

from event.models import Category, Event, Quote
from quiz.models import Answer, Question, Quiz, QuizResult


class CategorySerializer(ModelSerializer):
    """Сериализатор для категорий."""

    event = StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("name", "add_time", "change_time", "event")


class EventSerializer(ModelSerializer):
    """Сериализатор для мероприятий."""

    category = StringRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = (
            "name",
            "description",
            "add_time",
            "change_time",
            "category",
            "event_time",
            "location",
        )


class QuoteSerializer(ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Quote
        fields = ("text", "author", "image")


class QuizSerializer(ModelSerializer):
    """Сериализатор для квизов."""

    class Meta:
        model = Quiz
        fields = (
            "id",
            "name",
            "description"
        )


class AnswerSerializer(ModelSerializer):
    """Сериализатор для ответов."""

    class Meta:
        model = Answer
        fields = ("question", "answer_text", "is_right")


class QuestionSerializer(ModelSerializer):
    """Сериализатор для вопросов."""
    
    options = AnswerSerializer(many=True)
    quiz = StringRelatedField
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Question
        fields = (
            "quiz",
            "image",
            "question_text",
            "answers"
        )


class QuizResultSerializer(ModelSerializer):
    """Сериализатор для рузельтатов квиза."""

    quiz = StringRelatedField
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = QuizResult
        fields = ("quiz_id", "image", "text")