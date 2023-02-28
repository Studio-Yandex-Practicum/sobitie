
from telegram.ext import ConversationHandler, CommandHandler
from bot.handlers.support_handler import support_conv

from bot.convers_func.main_conversation import start, end

from core import constants

from bot.handlers.about_us_handler import about_us_conv
from bot.handlers.event_handler import event_conv
from bot.handlers.interactive_handler import interactive_conv


conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[CommandHandler('start', start)],
    states={
        constants.START_STATE:
            [
                about_us_conv,
                support_conv,
                event_conv,
                interactive_conv
            ]

    },
    fallbacks=[CommandHandler('end', end)]
)

