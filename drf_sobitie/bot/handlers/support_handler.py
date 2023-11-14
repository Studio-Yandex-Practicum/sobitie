from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from drf_sobitie.bot import constants as states
from drf_sobitie.bot.convers_func import support_conversation
from drf_sobitie.bot.convers_func.main_conversation import end
from drf_sobitie.bot.handlers.event_handler import (
    event_conv,
    subscribe_to_notifications_handler,
    unsubscribe_handler,
    other_help_notifications_handler
)
from drf_sobitie.bot.keyboards import support
from drf_sobitie.bot.keyboards.main import END, GIVE_SUPPORT

order_souvenir = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CallbackQueryHandler(
            support_conversation.show_souvenir_purchase_menu,
            pattern="^" + support.ORDER_SOUVENIRS + "$",
        )
    ],
    states={
        states.ORDER_SOUVENIR_STATE: [
            subscribe_to_notifications_handler,
            unsubscribe_handler,
        ],
        **event_conv.states,
    },
    fallbacks=[CommandHandler(END, end)],
)

other_help = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CallbackQueryHandler(
            support_conversation.show_other_help_menu,
            pattern="^" + support.OTHER_HELP + "$",
        )
    ],
    states={
        states.OTHER_HELP_STATE: [
            other_help_notifications_handler,
            unsubscribe_handler,
        ],
    },
    fallbacks=[CommandHandler(END, end)],
)

support_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CallbackQueryHandler(
            support_conversation.show_give_support_menu,
            pattern="^" + GIVE_SUPPORT + "$",
        )
    ],
    states={
        states.SUPPORT_STATE: [
            order_souvenir,
            other_help,
            CallbackQueryHandler(
                support_conversation.show_donations_options,
                pattern="^" + support.SHOW_DONATION_OPTIONS + "$",
            ),
            CallbackQueryHandler(
                support_conversation.show_social_links_and_gratitude,
                pattern="^" + support.FOLLOW_US + "$",
            ),
            CallbackQueryHandler(
                support_conversation.create_a_collection,
                pattern="^" + support.CREATE_COLLECTION + "$",
            ),
            CallbackQueryHandler(
                support_conversation.show_link_to_support_chat,
                pattern="^" + support.COMMUNICATE_FOR_HELP + "$",
            ),
        ],
        states.DONATION_OPTIONS_STATE: [
            CallbackQueryHandler(
                support_conversation.show_tinkoff_donation,
                pattern="^" + support.TINKOFF_DONATION + "$",
            ),
            CallbackQueryHandler(
                support_conversation.show_tinkoff_cashback,
                pattern="^" + support.TINKOFF_CASHBACK + "$",
            ),
            CallbackQueryHandler(
                support_conversation.show_donations_options,
                pattern="^" + support.SHOW_DONATION_OPTIONS + "$",
            ),
        ]
    },
    fallbacks=[CommandHandler(END, end)],
)
