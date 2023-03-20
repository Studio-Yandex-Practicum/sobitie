from telegram import InlineKeyboardButton

from bot.keyboards.main import create_return_to_start_button

START_QUIZZES = 'START_QUIZZES'
START_QUESTIONS = "START_QUESTIONS"
NEXT_QUESTIONS = "NEXT_QUESTIONS"

QUESTIONS_MENU_BUTTON = [
    [InlineKeyboardButton(text="Следующий вопрос.", callback_data=NEXT_QUESTIONS)],
    [create_return_to_start_button(),]
]

FINISH_QUIZ_MENU_BUTTON = [
    [create_return_to_start_button(),]
]
