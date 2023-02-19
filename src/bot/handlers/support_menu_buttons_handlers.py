from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from constants import START_MENU_BUTTONS


async def send_donation(update: Update, context):
    """Нажатие на кнопку 'Пожертвования'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Ваша ссылка на сайт с пожертвованиями: <http://link>'
    )
    return


async def attend_event(update: Update, context):
    """Нажатие на кнопку 'Прийти на спектакль'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Ваша ссылка на сайт с билетами: <http://link>'
    )
    return


async def go_back(update: Update, context):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await query.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return 'START_STATE'
