from drf_extra_fields.fields import Base64ImageField
from event.models import Event, Quote
from rest_framework.serializers import ModelSerializer, StringRelatedField


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
            "event_time",
            "location",
        )


class EventPostSerializer(ModelSerializer):
    """Сериализатор для мероприятий."""

    class Meta:
        model = Event
        fields = (
            "name",
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
