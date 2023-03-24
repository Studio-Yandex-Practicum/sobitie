from telegram import InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from bot.keyboards.support import (
    DONATION_OPTIONS_MENU_BUTTONS,
    MENU_ORDER_SOUVENIR,
    RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS,
    SUPPORT_FOLLOW_BUTTONS,
    SUPPORT_MENU_BUTTONS,
)
from core import states


async def show_give_support_menu(update: Update, _: CallbackContext):
    """Меню 'Помочь'."""
    query = update.callback_query
    await query.answer()
    message_text = """АНО «Событие» — некоммерческая организация. Мы стараемся оказать помощь тем, кому она \
необходима. Но это не значит, что сами не нуждаемся в поддержке. Чтобы чувствовать себя увереннее и планировать \
долгосрочные проекты, нам тоже нужна помощь. Любой неравнодушный человек может поддержать НКО ниже приведёнными \
способами."""
    keyboard = InlineKeyboardMarkup(SUPPORT_MENU_BUTTONS)
    await query.edit_message_text(text=message_text, reply_markup=keyboard)
    return states.SUPPORT_STATE


async def create_a_collection(update: Update, _: CallbackContext):
    """Обработчик кнопки 'Создать сбор'."""
    query = update.callback_query
    await query.answer()
    message_text = """Создайте сбор или организуйте благотворительное мероприятие на платформе \
<a href="https://sluchaem.ru/">«Пользуясь случаем»</a>."""
    keyboard = InlineKeyboardMarkup(RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS)
    await query.edit_message_text(
        text=message_text,
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
    message_text = """Спасибо большое за вашу поддержку! Вместе мы можем изменить мир к лучшему. Будем держать вас в \
курсе наших проектов и достижений в соцсетях."""
    keyboard = InlineKeyboardMarkup(SUPPORT_FOLLOW_BUTTONS)
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )
    return states.SUPPORT_FOLLOW_STATE


async def show_link_to_support_chat(update: Update, _: CallbackContext):
    """Обработчик кнопки 'Связь по вопросу помощи'."""
    query = update.callback_query
    # TODO: Здесь нужно улучшить текст сообщения и вставить реальную ссылку
    message_text = "Ваша ссылка на чат с обсуждением вариантов помощи: <http://link>"
    keyboard_markup = InlineKeyboardMarkup(RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS)
    await query.edit_message_text(text=message_text, reply_markup=keyboard_markup)


async def show_souvenir_purchase_menu(update: Update, _: CallbackContext):
    """Обработчик кнопки 'Приобрести сувенир'."""
    query = update.callback_query
    message_text = """Посетите <a href="https://vk.com/market-190536221">наш благотворительный магазин во \
«ВКонтакте»</a> и приобретите сувениры, сделанные в нашей инклюзивной мастерской ИТС "Событие", что поможет нам \
реализовывать наши проекты и инициативы.

Также вы можете включите уведомления о наших мероприятиях, чтобы всегда быть в курсе, когда и где пройдут \
мастер-классы и благотворительная ярмарка. Ваша поддержка очень важна для нас, спасибо!"""
    keyboard_markup = InlineKeyboardMarkup(MENU_ORDER_SOUVENIR)
    await query.edit_message_text(text=message_text, reply_markup=keyboard_markup, parse_mode=ParseMode.HTML)
    return states.ORDER_SOUVENIR_STATE


async def show_donations_options(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Сделать пожертвование'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(DONATION_OPTIONS_MENU_BUTTONS)
    message_text = """Спасибо, что хотите поддержать нашу организацию. Вы можете внести свой вклад в нашу работу, \
чтобы помочь нам реализовывать наши проекты и инициативы, следующими способами:

🔹Сделать пожертвование на нашем сайте
🔸Оформить разовое или регулярное пожертвование на сайте благотворительного фонда «Нужна помощь»
🔹Оформить небольшое регулярное пожертвование «Рубль в день»
🔸Сделать пожертвование в банке «Тинькофф» (для клиентов банка)

Спасибо, что поддерживаете нас!"""
    await query.edit_message_text(text=message_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    return states.DONATION_OPTIONS_STATE
