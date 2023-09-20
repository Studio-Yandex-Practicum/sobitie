from telegram.ext import CallbackQueryHandler

from bot.convers_func import what_we_do_conversation
from bot.keyboards import main


what_we_do = CallbackQueryHandler(
    what_we_do_conversation.show_info_what_we_do,
    pattern="^" + main.WHAT_WE_DO + "$",
)
