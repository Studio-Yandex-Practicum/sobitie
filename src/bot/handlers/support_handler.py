from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func import support_conversation
from bot.convers_func.main_conversation import end
from bot.keyboards import support
from bot.keyboards.main import END, GIVE_SUPPORT
from core import states

order_souvenir = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CallbackQueryHandler(
            support_conversation.order_souvenir,
            pattern="^" + support.ORDER_SOUVENIRS + "$",
        )
    ],
    states={
        states.ORDER_SOUVENIR_STATE: [
            CallbackQueryHandler(
                support_conversation.charity_fair_order,
                pattern="^" + support.CHARITY_FAIR + "$",
            ),
            CallbackQueryHandler(
                support_conversation.corporate_gifts_order,
                pattern="^" + support.CORPORATE_FAIR + "$",
            ),
        ]
    },
    fallbacks=[CommandHandler(END, end)],
)

support_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CallbackQueryHandler(
            support_conversation.give_support, pattern="^" + GIVE_SUPPORT + "$"
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
                support_conversation.show_cashback_connection_instructions,
                pattern="^" + support.CASHBACK + "$",
            ),
            CallbackQueryHandler(
                support_conversation.create_a_collection,
                pattern="^" + support.CREATE_COLLECTION + "$",
            ),
            CallbackQueryHandler(
                support_conversation.move_to_help_chat,
                pattern="^" + support.COMMUNICATE_FOR_HELP + "$",
            ),
        ],
    },
    fallbacks=[CommandHandler(END, end)],
)
