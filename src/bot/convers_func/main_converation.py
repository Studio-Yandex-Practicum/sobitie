from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from constants import START_MENU_BUTTONS

async def start(update, context):
    """Главное меню, кнопка старт."""

    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await update.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return 'START_STATE'


async def end(update, context):
    await update.message.reply_text('bye')
