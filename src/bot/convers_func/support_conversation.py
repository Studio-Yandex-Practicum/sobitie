from telegram import InlineKeyboardMarkup, Update

from src.core import constants
from core.menu_constants import START_MENU_BUTTONS, SUPPORT_MENU_BUTTONS


async def give_support(update: Update, context):
    """Меню 'Помочь'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(SUPPORT_MENU_BUTTONS)
    await query.edit_message_text(
        text='Помочь',
        reply_markup=keyboard,
    )
    return constants.SUPPORT_STATE


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
    return constants.START_STATE
