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
from bot.keyboards.event import EVENT_MENU, NOTIFICATION_BUTTONS, create_event_menu_buttons, create_finish_event_buttons
from core.settings import EVENTS_URL, NOTIFICATIONS_API_URL

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
    closing_message = """Вы можете подписаться на уведомления об анонсах, чтобы первыми узнавать о наших \
будущих мероприятиях. Также вы можете вернуться в главное меню и ознакомиться с другими разделами. Спасибо за интерес \
к нашей организации."""
    query = update.callback_query
    await query.answer()
    event_response = await async_get_request(url=EVENTS_URL)
    events = event_response.json()
    if len(events) == 0:
        await _process_no_events(query=query, closing_message=closing_message)
        return
    await _send_event_messages(query=query, events=events, message_template=EVENT_MESSAGE_TEMPLATE)
    await _send_closing_message(query=query, closing_message=closing_message)


async def show_gratitude_and_subscribe_to_notifications(update: Update, _: CallbackContext):
    """Отправляет сообщение благодарности за подписку и включает уведомления пользователю на события."""
    query = update.callback_query
    await query.answer()
    message_text = """Спасибо за интерес к нашим событиям! Вы будете получать уведомления о новых мероприятиях."""
    user_id = query.from_user.id
    response = await async_send_json_post_request(url=NOTIFICATIONS_API_URL, data={"user_id": user_id})
    message_text = await _check_api_response_status(message_text=message_text, response=response, user_id=user_id)
    keyboard = InlineKeyboardMarkup(NOTIFICATION_BUTTONS)
    await query.edit_message_text(text=(message_text + CLOSING_NOTIFICATION_TEXT), reply_markup=keyboard)
    return EVENT_MENU


async def unsubscribe_and_notify_user(update: Update, _: CallbackContext):
    """Отключение уведомлений пользователю на события и отправка сообщения с оповещением об этом."""
    query = update.callback_query
    await query.answer()
    message_text = """Вы успешно отписались от уведомлений о наших событиях. Мы будем скучать по вашему участию, \
но вы всегда можете подписаться на уведомления в любое время снова."""
    user_id = query.from_user.id
    response = await async_delete_request(url=f"{NOTIFICATIONS_API_URL}{user_id}/")
    message_text = await _check_api_response_status(
        message_text=message_text, response=response, user_id=user_id, expected_status=HTTPStatus.NO_CONTENT
    )
    keyboard = InlineKeyboardMarkup(NOTIFICATION_BUTTONS)
    await query.edit_message_text(text=(message_text + CLOSING_NOTIFICATION_TEXT), reply_markup=keyboard)
    return EVENT_MENU


async def notify_subscribers_about_new_event(event_data: Dict, bot: Bot) -> None:
    """Отправляет уведомления о новом событии всем подписчикам."""
    response = await async_get_request(url=NOTIFICATIONS_API_URL)
    subscribers = response.json()
    for user_data in subscribers:
        message = await _fill_in_message_template_with_event(
            event_data=event_data, message_template=EVENT_MESSAGE_TEMPLATE
        )
        await _send_message_or_handle_error(bot=bot, message_text=message, user_id=user_data["user_id"])


async def _send_message_or_handle_error(bot, message_text, user_id):
    try:
        await bot.send_message(chat_id=user_id, text=message_text, parse_mode=ParseMode.HTML)
    except TelegramError as e:
        await _handle_bot_block_error(error=e, user_id=user_id)


async def _handle_bot_block_error(error: TelegramError, user_id: int) -> None:
    """Проверяет, что ошибка связана с блокировкой бота пользователем, обрабатывая этот случай."""
    if "Forbidden: bot was blocked by the user" in str(error):
        logger.info(f"Бот был заблокирован пользователем, пользователь {user_id} будет удалён из подписчиков.")
        response = await async_delete_request(url=f"{NOTIFICATIONS_API_URL}{user_id}/")
        if response.status_code != HTTPStatus.NO_CONTENT:
            await _log_subscription_status_failure(response=response, user_id=user_id)
    else:
        logger.error(f"При отправке уведомления пользователю {user_id} произошла ошибка:", exc_info=error)


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
