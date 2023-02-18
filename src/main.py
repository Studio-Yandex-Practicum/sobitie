from bot.services import start_bot


def main() -> None:
    bot = start_bot()
    bot.run_polling()


if __name__ == '__main__':
    main()
