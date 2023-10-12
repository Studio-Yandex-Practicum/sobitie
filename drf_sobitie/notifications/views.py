import json
import asyncio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot
from django.http import HttpRequest
from bot.convers_func.event_conversation import notify_subscribers_about_new_event
from drf_sobitie.settings import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)

@csrf_exempt
async def send_event_notification(request: HttpRequest) -> JsonResponse:
    """Принимает запрос на отправку уведомлений и обрабатывает его."""
    if request.method == 'POST':
        try:
            event_data = json.loads(request.body.decode("utf-8"))
            await notify_subscribers_about_new_event(event_data=event_data, bot=bot)
            return JsonResponse({"message": "Отправка уведомлений началась."})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({"error": "Только POST запросы поддерживаются."})
