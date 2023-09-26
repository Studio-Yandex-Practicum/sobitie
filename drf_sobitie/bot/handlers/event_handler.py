from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func.event_conversation import (
    show_event_menu,
    show_gratitude_and_subscribe_to_notifications,
    show_upcoming_events,
    unsubscribe_and_notify_user,
    other_help_subscribe_to_notifications
)
from bot.convers_func.main_conversation import end
from bot.keyboards.event import (
    EVENT_MENU,
    NOTIFICATION_SUBSCRIBE_CALLBACK,
    NOTIFICATION_UNSUBSCRIBE_CALLBACK,
    UPCOMING_EVENTS,
)
from bot.keyboards.main import END, EVENTS

subscribe_to_notifications_handler = CallbackQueryHandler(
    show_gratitude_and_subscribe_to_notifications,
    pattern="^" + NOTIFICATION_SUBSCRIBE_CALLBACK + "$",
)

unsubscribe_handler = CallbackQueryHandler(
    unsubscribe_and_notify_user, pattern="^" + NOTIFICATION_UNSUBSCRIBE_CALLBACK + "$"
)

other_help_notifications_handler = CallbackQueryHandler(
    other_help_subscribe_to_notifications,
    pattern="^" + NOTIFICATION_SUBSCRIBE_CALLBACK + "$",
)

event_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_event_menu, pattern="^" + EVENTS + "$")],
    states={
        EVENT_MENU: [
            subscribe_to_notifications_handler,
            unsubscribe_handler,
            CallbackQueryHandler(
                show_upcoming_events, pattern="^" + UPCOMING_EVENTS + "$"
            ),
        ]
    },
    fallbacks=[CommandHandler(END, end)],
)
