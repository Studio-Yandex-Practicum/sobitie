from telegram import InlineKeyboardMarkup, Update

from bot.keyboards.about_us import ABOUT_US_MENU_BUTTONS, PROJECTS_MENU_BUTTONS
from bot.keyboards.main import START_MENU_BUTTONS
from core.states import ABOUT_US_STATE, PROJECTS_STATE, START_STATE


async def show_about_us(update: Update, _):
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
    return ABOUT_US_STATE


async def show_projects(update: Update, _):
    '''Нажатие на кнопку 'Проекты'.'''
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(PROJECTS_MENU_BUTTONS)
    await query.edit_message_text(
        text='Вот они наши проекты. Нажми!',
        reply_markup=keyboard,
    )

    return PROJECTS_STATE


async def go_back_to_start(update: Update, context):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await query.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return START_STATE
