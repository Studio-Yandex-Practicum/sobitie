from telegram import InlineKeyboardMarkup

from core.menu_constants import START_MENU_BUTTONS
from core import constants


async def start(update, context):
    """Главное меню, кнопка старт."""
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await update.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return constants.START_STATE


async def end(update):
    await update.message.reply_text('bye')
