# объект класса ConversationHandler для меню с 8-ю кнопками "Помочь"
from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.convers_func.support_conversation import (attend_event, become_follower, 
                                                   become_volunteer, become_sponsor,
                                                   give_support, go_back)
from bot.handlers.donation_handler import donation_conv


from bot.convers_func.main_conversation import end
from core import constants

support_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(give_support, pattern='^' + constants.GIVE_SUPPORT + '$')],
    states={
        constants.SUPPORT_STATE: [
            donation_conv,  # вложенный объект ConversationHandler
            CallbackQueryHandler(attend_event, pattern='^' + constants.ATTEND_EVENT + '$'),
            CallbackQueryHandler(become_sponsor, pattern='^' + constants.BECOME_SPONSOR + '$'),
            CallbackQueryHandler(become_volunteer, pattern='^' + constants.BECOME_VOLUNTEER + '$'),
            CallbackQueryHandler(become_follower, pattern='^' + constants.FOLLOW_US + '$'),
            CallbackQueryHandler(go_back, pattern='^' + constants.RETURN_TO_PREVIOUS + '$'),
        ],
        constants.SUPPORT_FOLLOW_STATE: [
            CallbackQueryHandler(give_support, pattern='^' + constants.RETURN_TO_PREVIOUS + '$'),
        ]
    },
    fallbacks=[CommandHandler(constants.END, end)]
)
