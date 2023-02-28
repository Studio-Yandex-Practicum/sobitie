# объект класса ConversationHandler для меню с 8-ю кнопками "Помочь"
from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.convers_func.support_conversation import (attend_event, become_follower, 
                                                   become_volunteer, become_sponsor,
                                                   give_support, go_back,
                                                   charity_fair_order,
                                                   corporate_gifts_order, order_souvenir,
                                                   become_partner)
from bot.handlers.donation_handler import donation_conv
from bot.convers_func.main_conversation import end
from core.states import (SUPPORT_STATE,
                         SUPPORT_FOLLOW_STATE,
                         ORDER_SOUVENIR_STATE)
from bot.convers_func.donation_conversation import go_back_to_help_menu
from bot.keyboards.main import END, GIVE_SUPPORT
from bot.keyboards.support import (ATTEND_EVENT, BECOME_SPONSOR,
                                   BECOME_VOLUNTEER, FOLLOW_US,
                                   RETURN_TO_PREVIOUS, ORDER_SOUVENIRS,
                                   CHARITY_FAIR, CORPORATE_FAIR,
                                   RETURN_TO_HELP_MENU, PARTNERSHIP)

order_suvenir = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CallbackQueryHandler(order_souvenir, pattern='^' + ORDER_SOUVENIRS + '$')
    ],
    states={
        ORDER_SOUVENIR_STATE: [
            CallbackQueryHandler(charity_fair_order, pattern='^' + CHARITY_FAIR + '$'),
            CallbackQueryHandler(corporate_gifts_order, pattern='^' + CORPORATE_FAIR + '$'),
            CallbackQueryHandler(go_back_to_help_menu, pattern='^' + RETURN_TO_HELP_MENU + '$')
        ]
    },
    fallbacks=[CommandHandler(END, end)]
)

support_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(give_support, pattern='^' + GIVE_SUPPORT + '$')],
    states={
        SUPPORT_STATE: [
            donation_conv,  # вложенный объект ConversationHandler
            order_suvenir,
            CallbackQueryHandler(attend_event, pattern='^' + ATTEND_EVENT + '$'),
            CallbackQueryHandler(become_sponsor, pattern='^' + BECOME_SPONSOR + '$'),
            CallbackQueryHandler(become_volunteer, pattern='^' + BECOME_VOLUNTEER + '$'),
            CallbackQueryHandler(become_follower, pattern='^' + FOLLOW_US + '$'),
            CallbackQueryHandler(become_partner, pattern='^' + PARTNERSHIP + '$'),
            CallbackQueryHandler(go_back, pattern='^' + RETURN_TO_PREVIOUS + '$'),
        ],
        SUPPORT_FOLLOW_STATE: [
            CallbackQueryHandler(give_support, pattern='^' + RETURN_TO_PREVIOUS + '$'),
        ],
    },
    fallbacks=[CommandHandler(END, end)]
)
