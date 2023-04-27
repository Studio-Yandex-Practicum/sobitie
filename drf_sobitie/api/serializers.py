from drf_extra_fields.fields import Base64ImageField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import IntegerField, ModelSerializer, SerializerMethodField
from rest_framework.validators import UniqueValidator

from event.models import Event, Quote, Subscriber
from quiz.models import Answer, Question, Quiz, QuizResult


class EventSerializer(ModelSerializer):
    """Сериализатор для мероприятий."""

    class Meta:
        model = Event
        fields = (
            "description",
            "add_time",
            "change_time",
            "event_time",
            "location",
        )


class EventPostSerializer(ModelSerializer):
    """Сериализатор для мероприятий."""

    class Meta:
        model = Event
        fields = (
            "description",
            "vk_post_id",
            "event_time",
            "location",
        )


class QuoteSerializer(ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Quote
        fields = ("text", "author", "image")


class AnswerSerializer(ModelSerializer):
    """Сериализатор для ответов."""

    class Meta:
        model = Answer
        fields = ("id", "answer_text", "is_right")


class QuestionSerializer(ModelSerializer):
    """Сериализатор для вопросов."""

    answers = AnswerSerializer(read_only=True, many=True)
    quiz = StringRelatedField
    image = Base64ImageField(required=False, allow_null=True)
    result_exist = SerializerMethodField(read_only=True)

    def get_result_exist(self, obj):
        if QuizResult.objects.filter(quiz_id=obj.quiz_id).exists():
            return True
        return False

    class Meta:
        model = Question
        fields = ("id", "image", "question_text", "answers", "result_exist")


class QuizSerializer(ModelSerializer):
    """Сериализатор для квизов."""
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ("id", "name", "description", "questions")


class QuizResultSerializer(ModelSerializer):
    """Сериализатор для рузельтатов квиза."""

    quiz = StringRelatedField
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = QuizResult
        fields = ("id", "quiz_id", "image", "text", "correct_answer_cnt")


class SubscriberSerializer(ModelSerializer):
    """Сериализатор для модели подписчика на уведомления на события."""

    user_id = IntegerField(
        min_value=0,
        validators=[UniqueValidator(queryset=Subscriber.objects.all())],
    )

    class Meta:
        model = Subscriber
        fields = ("user_id",)
