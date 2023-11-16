from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler

from drf_sobitie.bot.constants import START_STATE
from drf_sobitie.bot.convers_func.main_conversation import end, send_start_menu
from drf_sobitie.bot.handlers.about_us_handler import about_us_conv
from drf_sobitie.bot.handlers.event_handler import event_conv
from drf_sobitie.bot.handlers.interactive_handler import interactive_conv
from drf_sobitie.bot.handlers.support_handler import support_conv
from drf_sobitie.bot.handlers.what_we_do_handler import what_we_do
from drf_sobitie.bot.keyboards.main import RETURN_TO_START

main_conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[
        CommandHandler("start", send_start_menu),
        CallbackQueryHandler(send_start_menu, pattern="^" + RETURN_TO_START + "$"),
    ],
    states={
        START_STATE: [
            what_we_do,
            about_us_conv,
            support_conv,
            event_conv,
            interactive_conv,
        ]
    },
    fallbacks=[CommandHandler("end", end)],
)
