from telegram import InlineKeyboardMarkup, Update
from telegram.constants import ParseMode

from bot.keyboards.main import START_MENU_BUTTONS
from bot.keyboards import support
from core import states


async def give_support(update: Update, context):
    """Меню 'Помочь'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(support.SUPPORT_MENU_BUTTONS)
    await query.edit_message_text(
        text='Помочь',
        reply_markup=keyboard,
    )
    return states.SUPPORT_STATE


async def go_back(update: Update, context):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await query.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return states.START_STATE


async def create_a_collection(update: Update, context):
    """Обработчик кнопки 'Создать сбор'."""
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        text=('Создайте сбор или организуйте благотворительное'
              'мероприятие на платформе <a href="https://sluchaem.ru/">«Пользуясь случаем»</a>.'
              'Могу помочь!'),
        parse_mode=ParseMode.HTML,
    )


async def connect_cashback(update: Update, context):
    """Обработчик кнопки 'Подключить кэшбэк'."""
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        text=('Для клиентов банка «Тинькофф»'
              'Оформите «Кэшбэк во благо» в приложении «Тинькофф»:'
              'на главном экране нажмите на счёт карты → пролистайте'
              'до блока «Куда зачислять» → «Кэшбэк» → '
              '«В благотворительный фонд» → пролистать вниз и нажмите '
              '«Все фонды» → введите в поиске: Событие (без кавычек)')
    )


async def become_follower(update: Update, context):
    """Меню 'Стать активным подписчиком'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(support.SUPPORT_FOLLOW_BUTTONS)
    await query.edit_message_text(
        text='Подписаться на нас',
        reply_markup=keyboard,
    )
    return states.SUPPORT_FOLLOW_STATE


async def order_souvenir(update: Update, context):
    """Обработчик кнопки 'Заказать сувенир'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Заказать сувенир',
        reply_markup=InlineKeyboardMarkup(support.MENU_ORDER_SUVENIR)
    )
    return states.ORDER_SOUVENIR_STATE

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

# Путь к вызову функций
# СТАРТ -> Помочь -> сделать пожертвования
# функции обработчики кнопок 'Сделать пожертвования'


async def show_donations_options(update: Update, context):
    """Нажатие на кнопку 'Выбрать способ пожертвования'.
    Открывает подменю с выбором четырех способов
    внесения денег."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(support.DONATION_OPTIONS_MENU_BUTTONS)
    await query.edit_message_text(
        text='Сделать пожертвование',
        reply_markup=keyboard,
    )
    return states.DONATION_OPTIONS_STATE
