from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func.main_conversation import end, start
from bot.handlers.about_us_handler import about_us_conv
from bot.handlers.event_handler import event_conv
from bot.handlers.interactive_handler import interactive_conv
from bot.handlers.support_handler import support_conv
from bot.keyboards.main import RETURN_TO_START
from core.states import START_STATE

conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CommandHandler('start', start),
        CallbackQueryHandler(start, pattern='^' + RETURN_TO_START + '$'),
    ],
    states={
        START_STATE: [
            about_us_conv,
            support_conv,
            event_conv,
            interactive_conv,
        ]
    },
    fallbacks=[CommandHandler('end', end)],
)
