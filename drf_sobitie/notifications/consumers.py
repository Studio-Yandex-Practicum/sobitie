from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from telegram import Bot

from drf_sobitie.bot.convers_func.event_conversation import notify_subscribers_about_new_event


class EventNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        await self.send("Соединение разорвано.")

    async def receive(self, text_data=None, bytes_data=None):
        event_data = text_data
        await self.send("Отправка уведомлений началась.")
        await notify_subscribers_about_new_event(
            event_data=event_data,
            bot=Bot(token=settings.TELEGRAM_TOKEN)
        )
