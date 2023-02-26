from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Update

from core.menu_constants import SUPPORT_MENU_BUTTONS, SUPPORT_FOLLOW_BUTTONS


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
    return 'SUPPORT_FOLLOW_STATE'
