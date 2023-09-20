from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func.main_conversation import end
from bot.convers_func.quiz_converstation import send_quiz_question, send_start_quizzes_menu
from bot.keyboards.main import END, QUIZZES
from bot.keyboards.quiz import NEXT_QUESTIONS, START_QUESTIONS, START_QUIZZES

questions_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(send_quiz_question, pattern=r"^" + NEXT_QUESTIONS + "$")],
    states={},
    fallbacks=[CommandHandler(END, end)]
)

quizzes_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(send_start_quizzes_menu, pattern=r"^" + START_QUIZZES + "$")],
    states={
        QUIZZES: [
            CallbackQueryHandler(send_quiz_question, pattern=r"^" + START_QUESTIONS + r"#\d+$"),
        ],
    },
    fallbacks=[CommandHandler(END, end)]
)
