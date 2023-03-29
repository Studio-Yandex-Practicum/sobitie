import emoji
from telegram import InlineKeyboardButton

from bot.keyboards.main import (
    RETURN_BACK_BUTTON_TEXT,
    SHORT_RETURN_TO_START_BUTTON_TEXT,
    create_return_to_start_button,
)

UPCOMING_EVENTS = "UPCOMING_EVENTS"
NOTIFICATIONS = "NOTIFICATIONS"
EVENT_MENU = "EVENT_MENU"

UPCOMING_EVENTS_BUTTON = InlineKeyboardButton(
    text=f"{emoji.emojize(':calendar:')} Ближайшие события",
    callback_data=UPCOMING_EVENTS,
)
NOTIFICATIONS_BUTTON = InlineKeyboardButton(
    text=f"{emoji.emojize(':bell:')} Включить уведомления",
    callback_data=NOTIFICATIONS,
)
RETURN_TO_EVENT_MENU_BUTTON = InlineKeyboardButton(
    text=RETURN_BACK_BUTTON_TEXT,
    callback_data=EVENT_MENU,
)

EVENT_MENU_BUTTONS = [
    [UPCOMING_EVENTS_BUTTON],
    [NOTIFICATIONS_BUTTON],
    [create_return_to_start_button()],
]

FINISH_EVENT_BUTTONS = [
    [
        NOTIFICATIONS_BUTTON,
        create_return_to_start_button(SHORT_RETURN_TO_START_BUTTON_TEXT),
    ]
]

NOTIFICATION_BUTTONS = [
    [
        UPCOMING_EVENTS_BUTTON,
        create_return_to_start_button(text=SHORT_RETURN_TO_START_BUTTON_TEXT),
    ]
]
