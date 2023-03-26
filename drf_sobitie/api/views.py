from datetime import datetime
import re
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from api.serializers import CategorySerializer, CategoryPostSerializer, EventSerializer, EventPostSerializer, QuoteSerializer
from event.models import Category, Event, Quote
from rest_framework.response import Response
from rest_framework import status

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


class VKView(APIView):
    def common(self, text, pk=None):
        events=[event.description for event in Event.objects.all()]
        if 'афиша собития' in text.lower() and text not in events:
            event_time=re.search(r'\d\d\.\d\d\.\d{4}', text).group(0)
            event_time=datetime.strptime(event_time, '%d.%m.%Y') # %H:%M:%S.%f
            description=text
            location=re.search(r'Место события: г.[а-яА-Я-, ]+', text).group(0)
            category=re.search(r'Жанр: [а-яА-Я-, ]+', text).group(0)
            try:
                category=Category.objects.get(name=category)
            except:
                name={'name': category}
                category_serializer = CategoryPostSerializer(data=name)
                if category_serializer.is_valid():
                    category_serializer.save()
                    category=Category.objects.get(name=category)
            category=category.id
            return event_time, description, location, category



    def post(self, request):
        data = dict(request.data)
        event_time, description, location, category=self.common(text=data['text'][0])
        vk_post_id=data['id']
        data = {'event_time':event_time, 'name': description[0], 'location':location, 'description': description, 'vk_post_id': vk_post_id[0], 'category': category}
        serializer=EventPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        event_time, description, location, category=self.common(text=request['text'])
        vk_post_id=request['id']
        event = Event.objects.get(vk_post_id=pk)
        data = {'event_time':event_time, 'name': description, 'location':location, 'description': description, vk_post_id: vk_post_id, 'category': category}
        serializer=EventPostSerializer(event, data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
