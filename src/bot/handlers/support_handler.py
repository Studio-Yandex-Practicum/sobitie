# объект класса ConversationHandler для меню с 8-ю кнопками "Помочь"
from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from src.bot.convers_func.support_conversation import (attend_event,
                                                       give_support,
                                                       go_back)
from src.bot.handlers.donation_handler import donation_conv


from src.bot.convers_func.main_conversation import end
from src.core import constants

support_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(give_support, pattern='^' + constants.GIVE_SUPPORT + '$')],
    states={
        constants.SUPPORT_STATE: [
            donation_conv,  # вложенный объект ConversationHandler
            CallbackQueryHandler(attend_event, pattern='^' + constants.ATTEND_EVENT + '$'),
            CallbackQueryHandler(go_back, pattern='^' + constants.RETURN_TO_PREVIOUS + '$'),
        ]
    },
    fallbacks=[CommandHandler(constants.END, end)]
)
