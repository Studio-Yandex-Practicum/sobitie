from telegram import InlineKeyboardMarkup, Update


from bot.keyboards.main import START_MENU_BUTTONS, MAIN_TEXT
from core.states import START_STATE


async def start(update: Update, _):
    """Главное меню, кнопка старт."""
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await update.message.reply_text(
        text=MAIN_TEXT,
        reply_markup=keyboard,
    )
    return START_STATE


async def end(update: Update, _):
    await update.message.reply_text('bye')


async def main_menu(update: Update, _):
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    query = update.callback_query
    await query.message.reply_text(
        text=MAIN_TEXT,
        reply_markup=keyboard,
    )
