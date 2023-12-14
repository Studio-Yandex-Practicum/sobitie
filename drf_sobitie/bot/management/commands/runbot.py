import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from telegram.ext import Application, ApplicationBuilder, DictPersistence

from drf_sobitie.bot.handlers.main_handler import main_conversation_handler


def _create_bot_app() -> Application:
    """Создание экземпляра PTB приложения."""
    app = (
        ApplicationBuilder()
        .token(settings.TELEGRAM_TOKEN)
        .arbitrary_callback_data(True)
        .persistence(DictPersistence())
        .build())
    app.add_handler(main_conversation_handler)
    return app


class Command(BaseCommand):
    help = "Start telegram bot."

    def handle(self, *args, **kwargs):
        logging.basicConfig(
            format=settings.FORMAT,
            level=logging.INFO,
            handlers=[logging.StreamHandler()],
        )
        bot_app = _create_bot_app()
        bot_app.run_polling()
