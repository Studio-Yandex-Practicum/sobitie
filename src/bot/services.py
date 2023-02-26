from telegram.ext import ApplicationBuilder
from core.settings import TELEGRAM_TOKEN

from bot.handlers.main_handler import conversation_handler


def start_bot():
    """Старт бота."""
    bot = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    bot.add_handler(conversation_handler)
    return bot
