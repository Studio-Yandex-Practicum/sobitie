from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func.event_conversation import (
    show_event_menu,
    show_gratitude_and_subscribe_to_notifications,
    show_upcoming_events,
)
from bot.convers_func.main_conversation import end
from bot.keyboards.event import EVENT_MENU, NOTIFICATIONS, UPCOMING_EVENTS
from bot.keyboards.main import END, EVENTS

event_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_event_menu, pattern="^" + EVENTS + "$")],
    states={
        EVENT_MENU: [
            CallbackQueryHandler(
                show_gratitude_and_subscribe_to_notifications,
                pattern="^" + NOTIFICATIONS + "$",
            ),
            CallbackQueryHandler(
                show_upcoming_events, pattern="^" + UPCOMING_EVENTS + "$"
            ),
        ]
    },
    fallbacks=[CommandHandler(END, end)],
)
