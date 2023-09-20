from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from bot.convers_func.main_conversation import end, send_start_menu
from bot.handlers.about_us_handler import about_us_conv
from bot.handlers.event_handler import event_conv
from bot.handlers.interactive_handler import interactive_conv
from bot.handlers.support_handler import support_conv
from bot.handlers.what_we_do_handler import what_we_do
from bot.keyboards.main import RETURN_TO_START
from drf_sobitie.constants import START_STATE

main_conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CommandHandler("start", send_start_menu),
        CallbackQueryHandler(send_start_menu, pattern="^" + RETURN_TO_START + "$"),
    ],
    states={START_STATE: [what_we_do, about_us_conv, support_conv, event_conv, interactive_conv]},
    fallbacks=[CommandHandler("end", end)],
)
