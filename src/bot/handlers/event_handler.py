from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from src.bot.convers_func.event_conversation import (get_events, get_perfomances,
                                                     get_about_event, get_master_classes)
from src.bot.convers_func.main_conversation import end

from src.core import constants

event_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(get_events, pattern='^' + constants.EVENTS + '$')],
    states={
        constants.CHOISE_EVENT: [
            CallbackQueryHandler(get_perfomances, pattern='^' + constants.GET_MASTER_CLASS +'$'),
            CallbackQueryHandler(get_about_event, pattern='^' + constants.GET_PERFOMANSES + '$'),
            CallbackQueryHandler(get_master_classes, pattern='^' + constants.GET_EVENT + '$'),
        ]
    },
    fallbacks=[CommandHandler(constants.END, end)]
)