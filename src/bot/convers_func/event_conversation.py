import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Union

import requests
from telegram import CallbackQuery, InlineKeyboardMarkup, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext

from bot.keyboards.event import EVENT_MENU, EVENT_MENU_BUTTONS, FINISH_EVENT_BUTTONS, NOTIFICATION_BUTTONS

# TODO: Для работы в контейнерах нужно другое решение для ссылки на API событий
EVENTS_URL = "http://127.0.0.1:8000/api/events/"

logger = logging.getLogger(__name__)


async def show_event_menu(update: Update, _: CallbackContext):
    """Отправляет клавиатуру с меню раздела мероприятий."""
    keyboard = InlineKeyboardMarkup(EVENT_MENU_BUTTONS)
    query = update.callback_query
    await query.answer()
    message_text = """Мы организуем показы спектаклей, проводим открытые репетиции, мастер-классы, участвуем в \
благотворительных ярмарках, фестивалях...
Хотите узнать больше о предстоящих событиях?"""
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )
    return EVENT_MENU


async def show_upcoming_events(update: Update, _: CallbackContext):
    """Отправляет сообщения с ближайшими событиями."""
    message_template = """📅 {event_time_formatted}
🎭 {name}

📍 {location}

{description}
🏷️ {category}"""
    closing_message = """Вы можете подписаться на уведомления об анонсах, чтобы первыми узнавать о наших \
будущих мероприятиях. Также вы можете вернуться в главное меню и ознакомиться с другими разделами. Спасибо за интерес \
к нашей организации."""

    query = update.callback_query
    await query.answer()
    events = await _async_get_deserialized_json(url=EVENTS_URL)
    if len(events) == 0:
        await _process_no_events(query=query, closing_message=closing_message)
        return
    await _send_event_messages(query=query, events=events, message_template=message_template)
    await _send_closing_message(query=query, closing_message=closing_message)


async def show_gratitude_and_subscribe_to_notifications(update: Update, _: CallbackContext):
    # TODO: Реализовать логику уведомлений на новые мероприятия.
    """Отправляет сообщение благодарности за подписку и включает уведомления пользователю на события."""
    query = update.callback_query
    await query.answer()
    message_text = """Спасибо за интерес к нашим событиям! Вы будете получать уведомления о новых мероприятиях.

А пока можете посмотреть опубликованные анонсы или вернуться в главное меню."""
    keyboard = InlineKeyboardMarkup(NOTIFICATION_BUTTONS)
    await query.edit_message_text(text=message_text, reply_markup=keyboard)


async def _async_get_deserialized_json(url: str) -> Union[Dict, List]:
    """Отправляет GET-запрос по URL и возвращает десериализованный объект JSON."""
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(None, requests.get, url)
    return response.json()


async def _process_no_events(query: CallbackQuery, closing_message: str) -> None:
    """Обрабатывает случай, когда список ближайших событий пуст."""
    keyboard = InlineKeyboardMarkup(FINISH_EVENT_BUTTONS)
    message = "\n\n".join(["К сожалению, на данный момент у нас нет доступных событий.", closing_message])
    await query.edit_message_text(text=message, reply_markup=keyboard)


async def _send_event_messages(query: CallbackQuery, events: List[Dict], message_template: str) -> None:
    """Отправляет сообщения с информацией о ближайших мероприятиях."""
    for event in events:
        event_time = datetime.fromisoformat(event["event_time"])
        event_time_formatted = event_time.strftime("%d.%m.%Y %H:%M")
        message = message_template.format(**event, event_time_formatted=event_time_formatted)
        try:
            await query.message.reply_text(text=message, parse_mode="HTML")
        except BadRequest as exc:
            logger.warning(msg=f"Ошибка при отправке события: {message}.", exc_info=exc)


async def _send_closing_message(query: CallbackQuery, closing_message: str):
    """Отправляет завершающее сообщение после вывода всех доступных событий."""
    keyboard = InlineKeyboardMarkup(FINISH_EVENT_BUTTONS)
    message = "\n\n".join(["На данный момент это все доступные события.", closing_message])
    await query.message.reply_text(text=message, reply_markup=keyboard)
