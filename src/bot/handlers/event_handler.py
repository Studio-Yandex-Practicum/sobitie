from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from src.bot.convers_func.event_conversation import (get_events, get_perfomances,
                                                     get_about_event, get_master_classes)
from src.bot.convers_func.main_conversation import end
from src.core.constants import (EVENTS, CHOISE_EVENT, END, GET_MASTER_CLASS,
                                GET_PERFOMANSES, GET_EVENT)

event_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(get_events, pattern='^' + EVENTS + '$')],
    states={
        CHOISE_EVENT: [
            CallbackQueryHandler(get_perfomances, pattern='^' + GET_MASTER_CLASS +'$'),
            CallbackQueryHandler(get_about_event, pattern='^' + GET_PERFOMANSES + '$'),
            CallbackQueryHandler(get_master_classes, pattern='^' + GET_EVENT + '$'),
        ]
    },
    fallbacks=[CommandHandler(END, end)]
)