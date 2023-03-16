import emoji
from telegram import InlineKeyboardButton

from bot.keyboards.main import create_return_to_start_button

UPCOMING_EVENTS = "UPCOMING_EVENTS"
NOTIFICATIONS = "NOTIFICATIONS"
EVENT_MENU = "EVENT_MENU"
RETURN_TO_BACK_BUTTON_TEXT = f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу"

EVENT_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':date:')} Ближайшие события",
            callback_data=UPCOMING_EVENTS,
        ),
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':bell:')} Включить уведомления",
            callback_data=NOTIFICATIONS,
        ),
    ],
    [
        create_return_to_start_button(),
    ],
]

RETURN_TO_EVENT_MENU_BUTTON = [
    [
        InlineKeyboardButton(
            text=RETURN_TO_BACK_BUTTON_TEXT,
            callback_data=EVENT_MENU,
        )
    ],
]
