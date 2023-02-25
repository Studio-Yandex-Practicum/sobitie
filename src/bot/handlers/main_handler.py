from telegram.ext import (ConversationHandler, CommandHandler)

from src.bot.convers_func.main_conversation import (start, end)
from src.bot.handlers.event_handler import event_conv
from src.core import constants

conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[CommandHandler('start', start)],
    states={
        constants.SELECT_ACTION: [
            event_conv,

        ],
    },
    fallbacks=[CommandHandler('end', end)],
)
