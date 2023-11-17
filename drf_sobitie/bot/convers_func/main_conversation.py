from telegram import InlineKeyboardMarkup, Update

from drf_sobitie.bot.constants import START_STATE
from drf_sobitie.bot.keyboards.main import MAIN_TEXT, START_MENU_BUTTONS


async def send_start_menu(update: Update, _):
    """Отправка стартового меню и обработка возврата к нему."""
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    query = update.callback_query
    if query is None:
        send_method = update.message.reply_text
    elif update.effective_message.text is None:
        send_method = query.message.reply_text
    else:
        send_method = query.message.edit_text
    await send_method(
        text=MAIN_TEXT,
        reply_markup=keyboard,
    )
    return START_STATE


async def end(update: Update, _):
    await update.message.reply_text("bye")
