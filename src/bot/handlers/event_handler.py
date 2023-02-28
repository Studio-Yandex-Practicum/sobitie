from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.convers_func.event_conversation import (get_events, get_perfomances,
                                                     get_about_event, get_master_classes)
from bot.convers_func.main_conversation import end
from bot.keyboards.main import END, EVENTS
from bot.keyboards.event import (GET_MASTER_CLASS,
                                 GET_PERFORMANCES, GET_EVENT,
                                 CHOOSE_EVENT)
# from core.states import EVENTS

event_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(get_events, pattern='^' + EVENTS + '$')],
    states={
        CHOOSE_EVENT: [
            CallbackQueryHandler(get_perfomances, pattern='^' + GET_MASTER_CLASS +'$'),
            CallbackQueryHandler(get_about_event, pattern='^' + GET_PERFORMANCES + '$'),
            CallbackQueryHandler(get_master_classes, pattern='^' + GET_EVENT + '$'),
        ]
    },
    fallbacks=[CommandHandler(END, end)]
)