from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func.contacts_conversation import show_contacts
from bot.convers_func.main_conversation import end
from bot.keyboards.about_us import CONTACTS
from bot.keyboards.main import END

contacts_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_contacts, pattern="^" + CONTACTS + "$")],
    states={},
    fallbacks=[CommandHandler(END, end)],
)
