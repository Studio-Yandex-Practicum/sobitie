from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func import support_conversation
from bot.convers_func.main_conversation import end
from bot.handlers.event_handler import event_conv, subscribe_to_notifications_handler, unsubscribe_handler
from bot.keyboards import support
from bot.keyboards.main import END, GIVE_SUPPORT
from core import states

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
    },
    fallbacks=[CommandHandler(END, end)],
)
