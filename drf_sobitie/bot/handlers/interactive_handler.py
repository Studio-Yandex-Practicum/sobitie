from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from drf_sobitie.bot.constants import INTERACTIVE_STATE
from drf_sobitie.bot.convers_func.interactive_conversation import (
    cleanup_stickerpack_messages,
    get_quote,
    get_stickers,
    menu_interactive,
)
from drf_sobitie.bot.convers_func.main_conversation import end
from drf_sobitie.bot.handlers.quiz_handler import questions_handler, quizzes_handler
from drf_sobitie.bot.keyboards.interactive import GET_STICKERS, RANDOM_QUOTE
from drf_sobitie.bot.keyboards.main import END, INTERACTIVE_GAME

interactive_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CallbackQueryHandler(menu_interactive, pattern="^" + INTERACTIVE_GAME + "$")
    ],
    states={
        INTERACTIVE_STATE: [
            questions_handler,
            quizzes_handler,
            CallbackQueryHandler(get_stickers, pattern="^" + GET_STICKERS + "$"),
            CallbackQueryHandler(get_quote, pattern="^" + RANDOM_QUOTE + "$"),
            CallbackQueryHandler(cleanup_stickerpack_messages),
        ]
    },
    fallbacks=[CommandHandler(END, end)],
)
