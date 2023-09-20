import emoji
from telegram import InlineKeyboardButton

from bot.keyboards.main import create_return_to_start_button, INTERACTIVE_GAME, SHORT_RETURN_BACK_BUTTON_TEXT
from bot.keyboards.quiz import START_QUIZZES


GET_STICKERS = "GET_STICKERS"
RANDOM_QUOTE = "RANDOM_QUOTE"

INTERACTIVE_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':game_die:')}Викторины",
            callback_data=START_QUIZZES,
        ),
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize('	:star-struck:')}Стикерпаки",
            callback_data=GET_STICKERS,
        ),
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':books:')}Цитата недели",
            callback_data=RANDOM_QUOTE,
        ),
    ],
    [create_return_to_start_button()],
]

RETURN_TO_INTERACTIVE_MENU_BUTTON = [
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=INTERACTIVE_GAME
        )
    ]
]
