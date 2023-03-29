import logging

from bot.services import start_bot
from core.logger import FORMAT


def main() -> None:
    logging.basicConfig(
        format=FORMAT, level=logging.INFO, handlers=[logging.StreamHandler()]
    )
    bot = start_bot()
    bot.run_polling()


if __name__ == "__main__":
    main()
