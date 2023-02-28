from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from core import constants
from core.menu_constants import (ABOUT_US_MENU_BUTTONS,
                                 PROJECTS_MENU_BUTTONS,
                                 START_MENU_BUTTONS)


async def show_about_us(update: Update, context):
    """Нажатие на кнопку 'О нас'.
    Открывает подменю с четырьмя кнопками
    разной информации."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(ABOUT_US_MENU_BUTTONS)
    await query.edit_message_text(
        text='Узнайте о нас побольше. Выберите интересуещее Вас:',
        reply_markup=keyboard,
    )
    return constants.ABOUT_US_STATE


async def show_projects(update: Update, context):
    '''Нажатие на кнопку 'Проекты'.'''
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(PROJECTS_MENU_BUTTONS)
    await query.edit_message_text(
        text='Вот они наши проекты. Нажми!',
        reply_markup=keyboard,
    )

    return constants.PROJECTS_STATE


async def go_back_to_start(update: Update, context):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await query.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return constants.START_STATE
