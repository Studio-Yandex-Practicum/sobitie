from consumers import EventNotificationConsumer
from django.urls import path

websocket_urlpatterns = [
    path(r'ws/send-event-notification/$', EventNotificationConsumer.as_asgi()),
]
