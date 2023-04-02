import logging

from telegram.ext import Application, ApplicationBuilder

from bot.handlers.main_handler import main_conversation_handler
from core.logger import FORMAT
from core.settings import TELEGRAM_TOKEN


def _create_bot_app() -> Application:
    """Создание экземпляра PTB приложения."""
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(main_conversation_handler)
    return app


if __name__ == "__main__":
    logging.basicConfig(format=FORMAT, level=logging.INFO, handlers=[logging.StreamHandler()])
    bot_app = _create_bot_app()
    bot_app.run_polling()
