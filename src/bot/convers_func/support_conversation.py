from telegram import InlineKeyboardMarkup, Update


from core.states import SUPPORT_STATE, START_STATE, SUPPORT_FOLLOW_STATE, ORDER_SOUVENIR_STATE
from bot.keyboards.main import START_MENU_BUTTONS

from bot.keyboards.support import (SUPPORT_MENU_BUTTONS, SUPPORT_FOLLOW_BUTTONS,
                                   MENU_ORDER_SUVENIR, DONATION_OPTIONS_MENU_BUTTONS)


async def give_support(update: Update, context):
    """Меню 'Помочь'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(SUPPORT_MENU_BUTTONS)
    await query.edit_message_text(
        text='Помочь',
        reply_markup=keyboard,
    )
    return SUPPORT_STATE


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
    return START_STATE


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
        text='Заполните форму, выбрав тему «Волонтёрство»:\
              https://forms.yandex.ru/u/62c16ab249d6959ae05b57d1/'
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
    return SUPPORT_FOLLOW_STATE


async def become_partner(update: Update, context):
    """Обработчик кнопки 'Партнерство'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Партнерство'
    )
    return


async def our_needs(update: Update, context):
    """Обработчик кнопки 'Наши нужды'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Наши нужды'
    )
    return


async def go_to_play(update: Update, context):
    """Обработчик кнопки 'Перейти на спектакль'."""
    query = update.callback_query
    await query.message.reply_text(
        text='перейти на спектакль',
    )


async def order_souvenir(update: Update, context):
    """Обработчик кнопки 'Заказать сувенир'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Заказать сувенир',
        reply_markup=InlineKeyboardMarkup(MENU_ORDER_SUVENIR)
    )
    return ORDER_SOUVENIR_STATE

#  Путь к вызову функций
#  СТАРТ -> Помочь -> Заказать сувениры
#  функции обработчики кнопок 'Заказать сувениры'


async def charity_fair_order(update: Update, context):
    """Обработчик кнопки 'Благотворительная ярмарка'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Благотворительная ярмарка'
    )
    return


async def corporate_gifts_order(update: Update, context):
    """Обработчик кнопки 'Корпоративные подарки'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Корпоративные подарки'
    )
    return
