from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func.api_conversation import APIClient
from bot.convers_func.interactive_conversation import menu_interactive
from bot.convers_func.main_conversation import end
from bot.handlers.quiz_handler import questions_handler, quizzes_handler
from bot.keyboards.interactive import GET_STICKERS, RANDOM_QUOTE
from bot.keyboards.main import END, INTERACTIVE_GAME
from core.states import INTERACTIVE_STATE

interactive_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CallbackQueryHandler(menu_interactive, pattern="^" + INTERACTIVE_GAME + "$")
    ],
    states={
        INTERACTIVE_STATE: [
            questions_handler,
            quizzes_handler,
            CallbackQueryHandler(APIClient.get_stickers, pattern="^" + GET_STICKERS + "$"),
            CallbackQueryHandler(APIClient.get_quote, pattern="^" + RANDOM_QUOTE + "$"),
        ]
    },
    fallbacks=[CommandHandler(END, end)],
)
