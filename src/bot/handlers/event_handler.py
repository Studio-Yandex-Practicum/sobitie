from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func.event_conversation import get_events, get_master_classes, get_perfomances
from bot.convers_func.main_conversation import end
from bot.keyboards.event import CHOOSE_EVENT, GET_MASTER_CLASS, GET_PERFORMANCES
from bot.keyboards.main import END, EVENTS

event_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(get_events, pattern="^" + EVENTS + "$")],
    states={
        CHOOSE_EVENT: [
            CallbackQueryHandler(get_perfomances, pattern="^" + GET_PERFORMANCES + "$"),
            CallbackQueryHandler(
                get_master_classes, pattern="^" + GET_MASTER_CLASS + "$"
            ),
        ]
    },
    fallbacks=[CommandHandler(END, end)],
)
