import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from drf_sobitie.api.serializers import EventSerializer
from drf_sobitie.conf.settings import API_ADDRESS
from drf_sobitie.event.models import Event


@receiver(post_save, sender=Event)
def event_save_signal_receiver(sender, instance, created, **kwargs):
    """
    Обрабатывает появление нового события в БД.
    Отправляет боту запрос отправить уведомления о нём.
    """
    if created:
        serializer = EventSerializer(instance=instance)
        data = serializer.data
        url = f"{API_ADDRESS}/api/send-event-notification/"
        requests.post(url, json=data)
