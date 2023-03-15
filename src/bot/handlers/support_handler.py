# объект класса ConversationHandler для меню с 8-ю кнопками "Помочь"
from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.convers_func import support_conversation
from bot.convers_func.main_conversation import end
from bot.keyboards.main import END, GIVE_SUPPORT
from bot.keyboards import support
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
            # donation_conv,  вложенный объект ConversationHandler лишнее
            order_souvenir,
            CallbackQueryHandler(
                support_conversation.show_donations_options,
                pattern="^" + support.SHOW_DONATION_OPTIONS + "$",
            ),
            CallbackQueryHandler(
                support_conversation.become_follower,
                pattern="^" + support.FOLLOW_US + "$",
            ),
            CallbackQueryHandler(
                support_conversation.connect_cashback,
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
        states.SUPPORT_FOLLOW_STATE: [
            CallbackQueryHandler(
                support_conversation.give_support,
                pattern="^" + support.RETURN_TO_PREVIOUS + "$",
            ),
        ],
        # выход из меню Сделать пожертвование
        states.DONATION_OPTIONS_STATE: [
            CallbackQueryHandler(
                support_conversation.give_support,
                pattern="^" + support.RETURN_TO_PREVIOUS + "$",
            ),
        ],
    },
    fallbacks=[CommandHandler(END, end)],
)
