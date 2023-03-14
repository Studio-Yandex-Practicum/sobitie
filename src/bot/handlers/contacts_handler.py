from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.convers_func.contacts_conversation import show_contacts
from bot.keyboards.about_us import CONTACTS
from bot.keyboards.main import END
from bot.convers_func.main_conversation import end

contacts_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_contacts, pattern="^" + CONTACTS + "$")],
    states={},
    fallbacks=[CommandHandler(END, end)],
)
