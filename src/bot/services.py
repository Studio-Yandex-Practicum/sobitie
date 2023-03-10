from telegram.ext import ApplicationBuilder, CallbackQueryHandler
from core.settings import TELEGRAM_TOKEN

from bot.handlers.main_handler import conversation_handler

from bot.keyboards.main import RETURN_TO_START

from bot.convers_func.main_conversation import start


def start_bot():
    """Старт бота."""
    bot = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    bot.add_handler(conversation_handler)
    bot.add_handler(CallbackQueryHandler(start, pattern='^' + RETURN_TO_START + '$'))
    return bot
