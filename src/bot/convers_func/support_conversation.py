from telegram import InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from bot.keyboards.support import (
    DONATION_OPTIONS_MENU_BUTTONS,
    MENU_ORDER_SUVENIR,
    RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS,
    SUPPORT_FOLLOW_BUTTONS,
    SUPPORT_MENU_BUTTONS,
)
from core import states


async def give_support(update: Update, context):
    """Меню 'Помочь'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(SUPPORT_MENU_BUTTONS)
    await query.edit_message_text(
        text="Помочь",
        reply_markup=keyboard,
    )
    return states.SUPPORT_STATE


async def create_a_collection(update: Update, context):
    """Обработчик кнопки 'Создать сбор'."""
    query = update.callback_query
    await query.answer()
    message = """Создайте сбор или организуйте благотворительное мероприятие на платформе \
<a href="https://sluchaem.ru/">«Пользуясь случаем»</a>."""
    keyboard = InlineKeyboardMarkup(RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS)
    await query.edit_message_text(
        text=message,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
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


async def show_social_links_and_gratitude(update: Update, _: CallbackContext):
    """Меню 'Стать активным подписчиком'."""
    query = update.callback_query
    await query.answer()
    message = """Спасибо большое за вашу поддержку! Вместе мы можем изменить мир к лучшему. Будем держать вас в курсе \
наших проектов и достижений в соцсетях."""
    keyboard = InlineKeyboardMarkup(SUPPORT_FOLLOW_BUTTONS)
    await query.edit_message_text(
        text=message,
        reply_markup=keyboard,
    )
    return states.SUPPORT_FOLLOW_STATE


async def move_to_help_chat(update: Update, context):
    """Обработчик кнопки 'Связь по вопросу помощи'."""
    query = update.callback_query
    await query.message.reply_text(text="Ваша ссылка на чат с обсуждением вариантов помощи: <http://link>")
    return


async def order_souvenir(update: Update, context):
    """Обработчик кнопки 'Заказать сувенир'."""
    query = update.callback_query
    await query.message.reply_text(
        text="Заказать сувенир",
        reply_markup=InlineKeyboardMarkup(MENU_ORDER_SUVENIR),
    )
    return states.ORDER_SOUVENIR_STATE


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


async def show_donations_options(update: Update, context):
    """Нажатие на кнопку 'Выбрать способ пожертвования'.
    Открывает подменю с выбором четырех способов
    внесения денег."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(DONATION_OPTIONS_MENU_BUTTONS)
    await query.edit_message_text(
        text="Сделать пожертвование",
        reply_markup=keyboard,
    )
    return states.DONATION_OPTIONS_STATE
