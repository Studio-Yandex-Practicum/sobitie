from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler
from bot.convers_func.support_conversation import go_back
from bot.convers_func.interactive_conversation import menu_interactive, get_quiz, ask_question, get_quote
from bot.convers_func.main_conversation import end
from core import constants

interactive_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(menu_interactive, pattern='^' + constants.INTERACTIVE_GAME + '$')],
    states={
        constants.INTERACTIVE_STATE: [
            CallbackQueryHandler(get_quiz, pattern='^' + constants.QUIZZES + '$'),
            CallbackQueryHandler(ask_question, pattern='^' + constants.ASK_QUESTIONS + '$'),
            CallbackQueryHandler(get_quote, pattern='^' + constants.RANDOM_QUOTE + '$'),
            CallbackQueryHandler(go_back, pattern='^' + constants.RETURN_TO_PREVIOUS + '$'),
        ]
    },
    fallbacks=[CommandHandler(constants.END, end)]
)
