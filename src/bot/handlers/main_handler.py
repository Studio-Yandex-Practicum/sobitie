from telegram.ext import ConversationHandler, CommandHandler
from bot.handlers.support_handler import support_conv

from bot.convers_func.main_conversation import start, end

from src.core import constants


conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[CommandHandler('start', start)],
    states={
        constants.START_STATE:
            [
                support_conv
            ]

    },
    fallbacks=[CommandHandler('end', end)]
)





