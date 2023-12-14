from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from drf_sobitie.bot.keyboards.main import (
    create_return_to_start_button,
    INTERACTIVE_GAME,
    SHORT_RETURN_BACK_BUTTON_TEXT,
)

GET_STICKERS = "GET_STICKERS"
RANDOM_QUOTE = "RANDOM_QUOTE"

INTERACTIVE_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Стикерпаки",
            callback_data=GET_STICKERS,
        ),
    ],
    [
        InlineKeyboardButton(
            text="Цитата недели",
            callback_data=RANDOM_QUOTE,
        ),
    ],
    [create_return_to_start_button()],
]

RETURN_TO_INTERACTIVE_MENU_BUTTON = [
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=INTERACTIVE_GAME
        )
    ]
]

INTERACTIVE_MENU_KEYBOARD = InlineKeyboardMarkup(INTERACTIVE_BUTTONS)

RETURN_TO_INTERACTIVE_MENU_KEYBOARD = InlineKeyboardMarkup(RETURN_TO_INTERACTIVE_MENU_BUTTON)
