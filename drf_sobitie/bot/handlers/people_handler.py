from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from drf_sobitie.bot.convers_func.main_conversation import end
from drf_sobitie.bot.convers_func.people_conversation import show_people
from drf_sobitie.bot.keyboards.about_us import PEOPLE
from drf_sobitie.bot.keyboards.main import END

people_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_people, pattern="^" + PEOPLE + "$")],
    states={},
    fallbacks=[CommandHandler(END, end)],
)
