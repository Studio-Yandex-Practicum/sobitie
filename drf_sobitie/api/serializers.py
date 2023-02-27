from rest_framework.serializers import ModelSerializer, StringRelatedField

from event.models import Category, Event


class CategorySerializer(ModelSerializer):
    """Сериализатор для категорий."""
    event = StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'add_time', 'change_time', 'event')


class EventSerializer(ModelSerializer):
    """Сериализатор для мероприятий."""
    category = StringRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = ('name', 'description', 'add_time', 'change_time', 'category',
                  'event_time', 'location')
