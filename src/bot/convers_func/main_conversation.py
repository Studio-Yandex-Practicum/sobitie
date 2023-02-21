from telegram import InlineKeyboardMarkup

from src.core.constants import SELECT_ACTION
from src.core.menu_constants import BUTTONS_MAIN_MENU


async def start(update, _):
    """Главное меню, кнопка старт."""
    keyboard = InlineKeyboardMarkup(BUTTONS_MAIN_MENU)
    await update.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return SELECT_ACTION


async def end(update, _):
    await update.message.reply_text('bye')
