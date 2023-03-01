from telegram.ext import ApplicationBuilder, CallbackQueryHandler
from core.settings import TELEGRAM_TOKEN

from bot.handlers.main_handler import conversation_handler

from bot.keyboards.about_us import RETURN_TO_START

from bot.convers_func.main_conversation import main_menu


def start_bot():
    """Старт бота."""
    bot = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    bot.add_handler(conversation_handler)
    bot.add_handler(CallbackQueryHandler(main_menu, pattern='^' + RETURN_TO_START + '$'))
    return bot
