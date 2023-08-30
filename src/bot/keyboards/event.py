import logging
from typing import Sequence

import emoji
from requests import Response
from telegram import InlineKeyboardButton

from bot.async_requests import async_get_request
from bot.keyboards.main import (
    RETURN_BACK_BUTTON_TEXT, SHORT_RETURN_TO_START_BUTTON_TEXT,
    create_return_to_start_button, SHORT_RETURN_BACK_BUTTON_TEXT, RETURN_TO_START
)
from core.settings import CHECK_FOR_SUBSCRIPTION_API_URL

UPCOMING_EVENTS = "UPCOMING_EVENTS"
NOTIFICATION_SUBSCRIBE_CALLBACK = "NOTIFICATION_SUBSCRIBE_CALLBACK"
NOTIFICATION_UNSUBSCRIBE_CALLBACK = "NOTIFICATION_UNSUBSCRIBE_CALLBACK"
EVENT_MENU = "EVENT_MENU"

UPCOMING_EVENTS_BUTTON = InlineKeyboardButton(
    text=f"{emoji.emojize(':calendar:')} Ближайшие события",
    callback_data=UPCOMING_EVENTS,
)
RETURN_TO_EVENT_MENU_BUTTON = InlineKeyboardButton(
    text=RETURN_BACK_BUTTON_TEXT,
    callback_data=EVENT_MENU,
)
NOTIFICATION_BUTTONS = [
    [
        UPCOMING_EVENTS_BUTTON,
        create_return_to_start_button(text=SHORT_RETURN_TO_START_BUTTON_TEXT),
    ]
]
UNSUBSCRIBE_BUTTON_TEXT = emoji.emojize(":bell_with_slash: Выключить уведомления")
SUBSCRIBE_BUTTON_TEXT = emoji.emojize(":bell: Включить уведомления")

logger = logging.getLogger(__name__)


async def create_event_menu_buttons(
    user_id: int,
) -> Sequence[Sequence[InlineKeyboardButton]]:
    """Создаёт кнопки для клавиатуры меню Событий."""
    notification_button = await create_notification_button_based_on_subscription_status(
        user_id=user_id
    )
    event_menu_buttons = [
        [UPCOMING_EVENTS_BUTTON],
        [notification_button],
        [
            InlineKeyboardButton(
                text=SHORT_RETURN_BACK_BUTTON_TEXT,
                callback_data=RETURN_TO_START,
            )
        ],
    ]
    return event_menu_buttons


async def create_finish_event_buttons(
    user_id: int,
) -> Sequence[Sequence[InlineKeyboardButton]]:
    """Создаёт кнопки для клавиатуры актуальных событий."""
    notification_button = await create_notification_button_based_on_subscription_status(
        user_id=user_id
    )
    finish_event_buttons = [
        [
            notification_button,
            create_return_to_start_button(SHORT_RETURN_TO_START_BUTTON_TEXT),
        ]
    ]
    return finish_event_buttons


async def create_notification_button_based_on_subscription_status(
    user_id: int,
) -> InlineKeyboardButton:
    """В зависимости от наличия подписки создаёт кнопку: подписаться/отписаться."""
    button = InlineKeyboardButton(
        text=SUBSCRIBE_BUTTON_TEXT, callback_data=NOTIFICATION_SUBSCRIBE_CALLBACK
    )
    response = await async_get_request(
        url=f"{CHECK_FOR_SUBSCRIPTION_API_URL}{user_id}/"
    )
    button = await _process_and_update_button_based_on_api_response(
        button=button, response=response
    )
    return button


async def _process_and_update_button_based_on_api_response(
    button: InlineKeyboardButton, response: Response
) -> InlineKeyboardButton:
    """Обрабатывает ответ API и изменяет кнопку."""
    content_type_ = response.headers.get("content-type")
    if "application/json" in content_type_:
        button = await _update_notification_button_if_subscribed(
            button=button, response=response
        )
    else:
        logger.warning(
            f"Не удалось десериализовать ответ API по эндпоинту {response.url}, код ответа: {response.status_code}"
        )
    return button


async def _update_notification_button_if_subscribed(
    button: InlineKeyboardButton, response: Response
) -> InlineKeyboardButton:
    """Если пользователь подписан, то возвращает изменённый текст кнопки и callback."""
    data = response.json()
    if data.get("is_subscribed") is True:
        button = InlineKeyboardButton(
            text=UNSUBSCRIBE_BUTTON_TEXT,
            callback_data=NOTIFICATION_UNSUBSCRIBE_CALLBACK,
        )
    return button
