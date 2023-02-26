from telegram import Update, InlineKeyboardMarkup

from core import constants
from core.menu_constants import DONATION_OPTIONS_MENU_BUTTONS, SUPPORT_MENU_BUTTONS


async def show_donations_options(update: Update, context):
    """Нажатие на кнопку 'Выбрать способ пожертвования'.
    Открывает подменю с выбором четырех способов
    внесения денег."""
    query = update.callback_query
    keyboard = InlineKeyboardMarkup(DONATION_OPTIONS_MENU_BUTTONS)
    await query.edit_message_text(
        text='Выберите удобный для Вас способ внесения пожертвования',
        reply_markup=keyboard,
    )
    return constants.DONATION_OPTIONS_STATE


async def donate_with_site_form(update: Update, context):
    """Нажатие на кнопку 'Форма на сайте'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Ваша ссылка на страницу сайта с формой: https://sobytie.center/howtohelp/'
    )
    return


async def donate_with_vk(update: Update, context):
    """Нажатие на кнопку 'Вконтакте'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Ваша ссылка на пожертвование через VK: https://vk.com/app8168823_-190536221?ref=group_menu'
    )
    return


async def donate_with_tinkoff(update: Update, context):
    """Нажатие на кнопку 'Тинькофф'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Ссылка на сайт пожертвований через Тинькоф-банк: <http://link>'
    )
    return


async def donate_through_charity_fund(update: Update, context):
    """Нажатие на кнопку 'Через БФ "Нужна помощь"'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Ссылка на сайт БФ "Нужна помощь: https://nuzhnapomosh.ru/funds/centr-sobytie/#help'
    )
    return


async def go_back_to_help_menu(update: Update, context):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(SUPPORT_MENU_BUTTONS)
    await query.message.reply_text(
        text='Помочь',
        reply_markup=keyboard,
    )
    return constants.SUPPORT_STATE
