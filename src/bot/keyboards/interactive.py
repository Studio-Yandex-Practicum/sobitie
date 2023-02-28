import emoji

from telegram import InlineKeyboardButton

from .support import RETURN_TO_PREVIOUS
QUIZZES = 'QUIZZES'
ASK_QUESTIONS = 'ASK_QUESTIONS'
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
                text=f"{emoji.emojize(':white_question_mark:')}Вопрос-ответ",
                callback_data=ASK_QUESTIONS,
                url="https://vk.com/im?sel=-190536221"
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':books:')}Случайная цитата",
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