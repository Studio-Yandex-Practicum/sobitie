from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from constants import ABOUT_US_MENU_BUTTONS, PROJECTS_MENU_BUTTONS


MENU_MESSAGES = {
    'about_us': 'Узнайте о нас побольше. Выберите интересуещее Вас:',
    'projects': 'Вот они наши проекты. Нажми!',
}


async def about_us(update: Update, context):
    '''Меню "О нас"'''
    query = update.callback_query
    await query.answer()
    
    keyboard = InlineKeyboardMarkup(ABOUT_US_MENU_BUTTONS)
    await query.edit_message_text(
        text=MENU_MESSAGES['about_us'],
        reply_markup=keyboard,
    )
    
    return 'ABOUT_US_STATE'


async def projects(update: Update, context):
    '''Меню проектов'''
    query = update.callback_query
    await query.answer()
    
    keyboard = InlineKeyboardMarkup(PROJECTS_MENU_BUTTONS)
    await query.edit_message_text(
        text=MENU_MESSAGES['projects'],
        reply_markup=keyboard,
    )

    return 'PROJECTS_STATE'
