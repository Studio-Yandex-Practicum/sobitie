from telegram import InlineKeyboardMarkup, Update

from core import constants
from core.menu_constants import START_MENU_BUTTONS, SUPPORT_MENU_BUTTONS, SUPPORT_FOLLOW_BUTTONS, SUPPORT_ORDER_BUTTONS


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


async def become_sponsor(update: Update, context):
    """Нажатие на кнопку 'Стать спонсором'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Чтобы стать спонсором, заполните форму: <http://link>'
    )
    return


async def become_volunteer(update: Update, context):
    """Нажатие на кнопку 'Стать волонтером'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Заполните форму, выбрав тему «Волонтёрство»: https://forms.yandex.ru/u/62c16ab249d6959ae05b57d1/'
    )
    return


async def become_follower(update: Update, context):
    """Меню 'Стать активным подписчиком'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(SUPPORT_FOLLOW_BUTTONS)
    await query.edit_message_text(
        text='Подписаться на нас',
        reply_markup=keyboard,
    )
    return constants.SUPPORT_FOLLOW_STATE


async def order_souvenirs(update: Update, context):
    """Меню 'Заказать сувениры'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(SUPPORT_ORDER_BUTTONS)
    await query.edit_message_text(
        text='Заказать сувениры',
        reply_markup=keyboard,
    )
    return constants.SUPPORT_ORDER_STATE
