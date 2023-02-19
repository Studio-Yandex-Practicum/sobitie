from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from constants import ABOUT_US_MENU_BUTTONS


async def about_us(update: Update, context):
    """Меню 'О нас'"""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(ABOUT_US_MENU_BUTTONS)
    await query.edit_message_text(
        text='О нас',
        reply_markup=keyboard,
    )

    return 'ABOUT_US_STATE'


async def projects(update: Update, context):
    """Меню проектов"""
    query = update.callback_query
    await query.answer()
    buttons = [
        [
            InlineKeyboardButton(
                text='Project 1',
                callback_data='Project_1',

            )
        ],
        [
            InlineKeyboardButton(
                text='Project 2',
                callback_data='Project_2',
            )
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await query.edit_message_text(
        text='Наши проекты',
        reply_markup=keyboard,
    )

    return 'PROJECTS'

