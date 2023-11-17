from asyncio import create_task

from django.conf import settings
from fastapi import FastAPI, Request
from telegram import Bot

from drf_sobitie.bot.convers_func.event_conversation import (
    notify_subscribers_about_new_event,
)

fastapi_app = FastAPI()

bot = Bot(token=settings.TELEGRAM_TOKEN)


@fastapi_app.post("/send-event-notification/")
async def send_event_notification(request: Request) -> str:
    """Принимает запрос на отправку уведомлений и обрабатывает его."""
    event_data = await request.json()
    create_task(notify_subscribers_about_new_event(event_data=event_data, bot=bot))
    return "Отправка уведомлений началась."
