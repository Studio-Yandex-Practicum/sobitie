from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from telegram import Bot

from bot.convers_func.event_conversation import notify_subscribers_about_new_event
from drf_sobitie.settings import TELEGRAM_TOKEN


class EventNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        event_data = text_data
        await self.send("Отправка уведомлений началась.")
        await (database_sync_to_async(notify_subscribers_about_new_event)
               (event_data=event_data, bot=Bot(token=TELEGRAM_TOKEN)))
