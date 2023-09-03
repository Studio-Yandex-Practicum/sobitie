from telegram import InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from bot.keyboards.support import (
    DONATION_OPTIONS_MENU_BUTTONS,
    RETURN_TO_SUPPORT_BUTTON,
    SUPPORT_CREATE_COLLECTION_BUTTONS,
    SUPPORT_FOLLOW_BUTTONS,
    SUPPORT_MENU_BUTTONS,
    TINKOFF_CASHBACK_MENU_BUTTONS,
    TINKOFF_DONATION_MENU_BUTTONS,
    create_menu_order_souvenir,
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
    message_text = (
        "Создайте сбор или организуйте благотворительное мероприятие на платформе «Пользуясь случаем»."
    )
    keyboard = InlineKeyboardMarkup(SUPPORT_CREATE_COLLECTION_BUTTONS)
    await query.edit_message_text(
        text=message_text,
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
    )


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
    keyboard_markup = InlineKeyboardMarkup(
        RETURN_TO_SUPPORT_BUTTON
    )
    await query.edit_message_text(text=message_text, reply_markup=keyboard_markup)


async def show_souvenir_purchase_menu(update: Update, _: CallbackContext):
    """Обработчик кнопки 'Приобрести сувенир'."""
    query = update.callback_query
    message_text = (
        "Посетите наш благотворительный магазин во «ВКонтакте» и приобретите сувениры, сделанные в нашей инклюзивной мастерской ИТС «Событие», "
        "что поможет нам реализовывать наши проекты и инициативы. \n\n"
        "Также вы можете включить уведомления о наших мероприятиях, "
        "чтобы всегда быть в курсе, когда и где пройдут мастер-классы и благотворительная ярмарка. Ваша поддержка очень важна для нас, спасибо!"
    )
    menu_order_souvenir = await create_menu_order_souvenir(user_id=query.from_user.id)
    keyboard_markup = InlineKeyboardMarkup(menu_order_souvenir)
    await query.edit_message_text(
        text=message_text, reply_markup=keyboard_markup, parse_mode=ParseMode.HTML
    )
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
    await query.edit_message_text(
        text=message_text, reply_markup=keyboard, parse_mode=ParseMode.HTML
    )
    return states.DONATION_OPTIONS_STATE


async def show_tinkoff_donation(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Клиентам Тинькофф'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(TINKOFF_DONATION_MENU_BUTTONS)
    message_text = "Выберите удобный вариант пожертвования"
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard
    )


async def show_tinkoff_cashback(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Кэшбек во благо'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(TINKOFF_CASHBACK_MENU_BUTTONS)
    message_text = "Скоро будет"
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard
    )
