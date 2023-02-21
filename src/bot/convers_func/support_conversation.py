from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Update

from constants import SUPPORT_MENU_BUTTONS, SUPPORT_FOLLOW_BUTTONS


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


async def become_follower(update: Update, context):
    """Меню 'Стать активным подписчиком'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(SUPPORT_FOLLOW_BUTTONS)
    await query.edit_message_text(
        text='Подписаться на нас',
        reply_markup=keyboard,
    )
    return 'SUPPORT_FOLLOW_STATE'
