from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Update

from constants import SUPPORT_MENU_BUTTONS


async def give_support(update: Update, context):
    """Меню 'Помочь'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(SUPPORT_MENU_BUTTONS)
    await query.edit_message_text(
        text='Помочь',
        reply_markup=keyboard,
    )
    return 'SUPPORT_STATE'
