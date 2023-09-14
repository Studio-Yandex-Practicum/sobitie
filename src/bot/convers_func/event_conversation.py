import logging
from datetime import datetime
from http import HTTPStatus
from json import dumps
from typing import Dict, List

import emoji
from requests import Response
from telegram import Bot, CallbackQuery, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.error import BadRequest, TelegramError
from telegram.ext import CallbackContext

from bot.async_requests import async_delete_request, async_get_request, async_send_json_post_request
from bot.convers_func.api_conversation import *
from bot.keyboards.event import EVENT_MENU, NOTIFICATION_BUTTONS, create_event_menu_buttons, create_finish_event_buttons
from core.settings import NOTIFICATIONS_API_URL

EVENT_MESSAGE_TEMPLATE = emoji.emojize(
        """:calendar: {event_time_formatted}

:round_pushpin: {location}

{description}
"""
)
CLOSING_NOTIFICATION_TEXT = "\n\nА пока можете посмотреть опубликованные анонсы или вернуться в главное меню."

logger = logging.getLogger(__name__)


async def show_event_menu(update: Update, _: CallbackContext):
    """Отправляет клавиатуру с меню раздела мероприятий."""
    query = update.callback_query
    await query.answer()
    event_menu_buttons = await create_event_menu_buttons(user_id=query.from_user.id)
    keyboard = InlineKeyboardMarkup(event_menu_buttons)
    message_text = (
        "Мы организуем показы спектаклей, проводим открытые репетиции, мастер-классы, участвуем в благотворительных ярмарках и фестивалях."
    )
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )
    return EVENT_MENU


async def _send_message_or_handle_error(bot, message_text, user_id):
    try:
        await bot.send_message(chat_id=user_id, text=message_text, parse_mode=ParseMode.HTML)
    except TelegramError as e:
        await APIClient._handle_bot_block_error(error=e, user_id=user_id)


async def _check_api_response_status(
    message_text: str, response: Response, user_id: int, expected_status=HTTPStatus.CREATED
) -> str:
    """Проверяет статус ответа API, если он неудачный, то возвращает другое сообщение для пользователя."""
    status_code = response.status_code
    if status_code != expected_status:
        await _log_subscription_status_failure(response=response, user_id=user_id)
        message_text = emoji.emojize(
            """Что-то пошло не так :confused_face:
Попробуйте позже."""
        )
    return message_text


async def _log_subscription_status_failure(response: Response, user_id: int) -> None:
    """Сообщает в логи о том, что подписка/отписка пользователя не удалась."""
    error_text = (
        f"При изменении статуса уведомлений пользователя с id={user_id} вернулся статус: {response.status_code}\n"
    )
    content_type_ = response.headers.get("content-type")
    if "application/json" in content_type_:
        error_text += dumps(response.json(), ensure_ascii=False)
    logger.error(error_text)


async def _process_no_events(query: CallbackQuery, closing_message: str) -> None:
    """Обрабатывает случай, когда список ближайших событий пуст."""
    finish_event_buttons = await create_finish_event_buttons(user_id=query.from_user.id)
    keyboard = InlineKeyboardMarkup(finish_event_buttons)
    message = "\n\n".join(["К сожалению, на данный момент у нас нет доступных событий.", closing_message])
    await query.edit_message_text(text=message, reply_markup=keyboard)


async def _send_event_messages(query: CallbackQuery, events: List[Dict], message_template: str) -> None:
    """Отправляет сообщения с информацией о ближайших мероприятиях."""
    for event in events:
        message = await _fill_in_message_template_with_event(event_data=event, message_template=message_template)
        try:
            await query.message.reply_text(text=message, parse_mode=ParseMode.HTML)
        except BadRequest as exc:
            logger.warning(msg=f"Ошибка при отправке события: {message}.", exc_info=exc)


async def _fill_in_message_template_with_event(event_data: Dict, message_template: str) -> str:
    """Заполняет шаблон сообщения о событии данными события."""
    event_time = datetime.fromisoformat(event_data["event_time"])
    event_time_formatted = event_time.strftime("%d.%m.%Y %H:%M")
    message = message_template.format(**event_data, event_time_formatted=event_time_formatted)
    return message


async def _send_closing_message(query: CallbackQuery, closing_message: str):
    """Отправляет завершающее сообщение после вывода всех доступных событий."""
    finish_event_buttons = await create_finish_event_buttons(user_id=query.from_user.id)
    keyboard = InlineKeyboardMarkup(finish_event_buttons)
    message = "\n\n".join(["На данный момент это все доступные события.", closing_message])
    await query.message.reply_text(text=message, reply_markup=keyboard)
