import emoji

from telegram import InlineKeyboardButton

from .support import RETURN_TO_PREVIOUS
QUIZZES = 'QUIZZES'
GET_STICKERS = 'GET_STICKERS'
RANDOM_QUOTE = 'RANDOM_QUOTE'

# кнопки для меню интерактив
INTERACTIVE_BUTTONS = [
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':game_die:')}Викторины",
                callback_data=QUIZZES
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize('	:star-struck:')}Стикерпаки",
                callback_data=GET_STICKERS
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':books:')}Цитата недели",
                callback_data=RANDOM_QUOTE
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':reverse_button:')}Вернуться",
                callback_data=RETURN_TO_PREVIOUS,
            )
        ]
    ]