from telegram import InlineKeyboardButton

from drf_sobitie.bot.keyboards.main import (
    INTERACTIVE_GAME,
    SHORT_RETURN_BACK_BUTTON_TEXT,
)

START_QUIZZES = "START_QUIZZES"
START_QUESTIONS = "START_QUESTIONS"
NEXT_QUESTIONS = "NEXT_QUESTIONS"

QUESTIONS_MENU_BUTTON = [
    [InlineKeyboardButton(text="Следующий вопрос.", callback_data=NEXT_QUESTIONS)],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=INTERACTIVE_GAME,
        )
    ],
]

FINISH_QUIZ_MENU_BUTTON = [
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=INTERACTIVE_GAME,
        )
    ],
]
