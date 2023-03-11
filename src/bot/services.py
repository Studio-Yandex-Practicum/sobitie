from telegram.ext import ApplicationBuilder

from bot.handlers.main_handler import main_conversation_handler
from core.settings import TELEGRAM_TOKEN


def start_bot():
    """Старт бота."""
    bot = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    bot.add_handler(main_conversation_handler)
    return bot
