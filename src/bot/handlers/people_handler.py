from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.keyboards.about_us import PEOPLE
from bot.convers_func.people_conversation import show_people
from bot.convers_func.main_conversation import end
from bot.keyboards.main import END

people_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_people, pattern='^' + PEOPLE + '$')],
    states={},
    fallbacks=[CommandHandler(END, end)]
)
