import logging

from telegram.ext import Application, ApplicationBuilder
from django.core.management.base import BaseCommand

from drf_sobitie.settings import FORMAT
from drf_sobitie.settings import TELEGRAM_TOKEN
from bot.handlers.main_handler import main_conversation_handler


def _create_bot_app() -> Application:
    """Создание экземпляра PTB приложения."""
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(main_conversation_handler)
    return app


class Command(BaseCommand):
    help = 'Start telegram bot.'

    def handle(self, *args, **kwargs):
        logging.basicConfig(format=FORMAT, level=logging.INFO, handlers=[logging.StreamHandler()])
        bot_app = _create_bot_app()
        bot_app.run_polling()
