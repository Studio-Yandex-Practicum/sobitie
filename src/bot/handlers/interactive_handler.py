from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler
from bot.convers_func.support_conversation import go_back
from bot.convers_func.interactive_conversation import menu_interactive, get_quiz, ask_question, get_quote
from bot.convers_func.main_conversation import end
from core.states import INTERACTIVE_STATE
from bot.keyboards.interactive import (QUIZZES, ASK_QUESTIONS,
                                       RANDOM_QUOTE, RETURN_TO_PREVIOUS)
from bot.keyboards.main import INTERACTIVE_GAME, END

interactive_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(menu_interactive, pattern='^' + INTERACTIVE_GAME + '$')],
    states={
        INTERACTIVE_STATE: [
            CallbackQueryHandler(get_quiz, pattern='^' + QUIZZES + '$'),
            CallbackQueryHandler(ask_question, pattern='^' + ASK_QUESTIONS + '$'),
            CallbackQueryHandler(get_quote, pattern='^' + RANDOM_QUOTE + '$'),
            CallbackQueryHandler(go_back, pattern='^' + RETURN_TO_PREVIOUS + '$'),
        ]
    },
    fallbacks=[CommandHandler(END, end)]
)