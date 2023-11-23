import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from notifications.consumers import EventNotificationConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_sobitie.conf.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path(r'ws/send-event-notification/$', EventNotificationConsumer.as_asgi()),
    ]),
})
