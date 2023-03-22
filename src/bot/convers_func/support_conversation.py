from telegram import InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from bot.keyboards import support
from bot.keyboards.support import RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS
from core import states


async def give_support(update: Update, context):
    """Меню 'Помочь'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(support.SUPPORT_MENU_BUTTONS)
    await query.edit_message_text(
        text="Помочь", reply_markup=keyboard,
    )
    return states.SUPPORT_STATE


async def create_a_collection(update: Update, context):
    """Обработчик кнопки 'Создать сбор'."""
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        text=(
            "Создайте сбор или организуйте благотворительное"
            'мероприятие на платформе <a href="https://sluchaem.ru/">«Пользуясь случаем»</a>.'
            "Могу помочь!"
        ),
        parse_mode=ParseMode.HTML,
    )


async def show_cashback_connection_instructions(update: Update, _: CallbackContext):
    """Обработчик кнопки 'Подключить кэшбэк'."""
    query = update.callback_query
    await query.answer()
    message = """Для клиентов банка «Тинькофф»
Оформите «Кэшбэк во благо» в приложении «Тинькофф»:
🔹 На главном экране нажмите на счёт карты
🔸 Пролистайте вниз до блока «Куда зачислять»
🔹 Нажмите на «Кэшбэк», далее «В благотворительный фонд»
🔸 Пролистайте вниз и нажмите на кнопку «Все фонды»
🔹 Введите в поиске: Событие
✔️ Готово
"""
    keyboard = InlineKeyboardMarkup(RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS)
    await query.edit_message_text(text=message, reply_markup=keyboard)


async def become_follower(update: Update, context):
    """Меню 'Стать активным подписчиком'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(support.SUPPORT_FOLLOW_BUTTONS)
    await query.edit_message_text(
        text="Подписаться на нас", reply_markup=keyboard,
    )
    return states.SUPPORT_FOLLOW_STATE


async def move_to_help_chat(update: Update, context):
    """Обработчик кнопки 'Наши нужды'."""
    query = update.callback_query
    await query.message.reply_text(
        text="Ваша ссылка на чат с обсуждением вариантов помощи: <http://link>"
    )
    return


async def order_souvenir(update: Update, context):
    """Обработчик кнопки 'Заказать сувенир'."""
    query = update.callback_query
    await query.message.reply_text(
        text="Заказать сувенир",
        reply_markup=InlineKeyboardMarkup(support.MENU_ORDER_SUVENIR),
    )
    return states.ORDER_SOUVENIR_STATE


#  Путь к вызову функций
#  СТАРТ -> Помочь -> Заказать сувениры
#  функции обработчики кнопок 'Заказать сувениры'


async def charity_fair_order(update: Update, context):
    """Обработчик кнопки 'Благотворительная ярмарка'."""
    query = update.callback_query
    await query.message.reply_text(text="Благотворительная ярмарка")
    return


async def corporate_gifts_order(update: Update, context):
    """Обработчик кнопки 'Корпоративные подарки'."""
    query = update.callback_query
    await query.message.reply_text(text="Корпоративные подарки")
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
        text="Сделать пожертвование", reply_markup=keyboard,
    )
    return states.DONATION_OPTIONS_STATE
