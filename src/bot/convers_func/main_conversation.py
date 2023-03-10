from telegram import InlineKeyboardMarkup, Update

from bot.keyboards.main import MAIN_TEXT, START_MENU_BUTTONS
from core.states import START_STATE


async def start(update: Update, _):
    """Главное меню, кнопка старт."""
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await update.effective_message.reply_text(
        text=MAIN_TEXT,
        reply_markup=keyboard,
    )
    return START_STATE if update.callback_query is None else None


async def end(update: Update, _):
    await update.message.reply_text('bye')
