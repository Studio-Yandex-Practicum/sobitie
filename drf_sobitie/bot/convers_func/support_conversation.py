from telegram import InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import CallbackContext

from drf_sobitie.bot import constants as states
from drf_sobitie.bot.keyboards.support import (
    DONATION_OPTIONS_MENU_BUTTONS,
    RETURN_TO_SUPPORT_BUTTON,
    SUPPORT_CREATE_COLLECTION_BUTTONS,
    SUPPORT_FOLLOW_BUTTONS,
    SUPPORT_MENU_BUTTONS,
    TINKOFF_CASHBACK_MENU_BUTTONS,
    TINKOFF_DONATION_MENU_BUTTONS,
    create_menu_order_souvenir,
    create_menu_other_help,
)


async def show_give_support_menu(update: Update, _: CallbackContext):
    """Меню 'Как помочь'."""
    query = update.callback_query
    await query.answer()
    message_text = (
        "АНО «Событие» — некоммерческая организация. Мы стараемся оказать помощь тем, кому она необходима. \n"
        "Но чтобы продолжать свою работу и планировать долгосрочные проекты, нам тоже нужна помощь. \n"
        "Если вы хотите поддержать нас, то выберите один или несколько способов, представленных ниже."
    )
    keyboard = InlineKeyboardMarkup(SUPPORT_MENU_BUTTONS)
    await query.edit_message_text(text=message_text, reply_markup=keyboard)
    return states.SUPPORT_STATE


async def create_a_collection(update: Update, _: CallbackContext):
    """Обработчик кнопки 'Создать сбор'."""
    query = update.callback_query
    await query.answer()
    message_text = "Создайте сбор или организуйте благотворительное мероприятие на платформе «Пользуясь случаем»."
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
    message_text = (
        "Наши социальные сети: <a href=https://vk.com/sobytie.center>ВКонтакте</a> и"
        " <a href=https://t.me/sobytiecenter>Telegram.</a>"
    )
    keyboard = InlineKeyboardMarkup(RETURN_TO_SUPPORT_BUTTON)
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )
    return states.SUPPORT_FOLLOW_STATE


async def show_link_to_support_chat(update: Update, _: CallbackContext):
    """Обработчик кнопки 'Связь по вопросам помощи'."""
    query = update.callback_query
    message_text = (
        "Ваша ссылка на чат с обсуждением вариантов помощи: \n"
        "<a href='https://t.me/gingersilence'>Оксана Приходько</a>"
    )
    keyboard_markup = InlineKeyboardMarkup(RETURN_TO_SUPPORT_BUTTON)
    await query.edit_message_text(text=message_text, reply_markup=keyboard_markup, parse_mode = ParseMode.HTML)


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
    message_text = (
        "Чтобы помочь нам реализовывать проекты и инициативы, вы можете внести свой вклад в нашу работу. \n"
        "Спасибо за поддержку!"
    )
    await query.edit_message_text(
        text=message_text, reply_markup=keyboard, parse_mode=ParseMode.HTML
    )
    return states.DONATION_OPTIONS_STATE


async def show_other_help_menu(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Иная помощь'"""
    query = update.callback_query
    await query.answer()
    message_text = (
        "Нам может потребоваться разная помощь: \n\n"
        "Иногда мы ищем реквизит для спектаклей \n"
        "Приглашаем волонтеров \n"
        "Нуждаемся в транспорте \n"
        "Расходные материалы для мастерской \n\n"
        "Включите уведомления, чтобы получать информацию о нашем центре, мероприятиях и возможных потребностях. \n"
    )
    menu_other_help = await create_menu_other_help(user_id=query.from_user.id)
    keyboard_markup = InlineKeyboardMarkup(menu_other_help)

    await query.edit_message_text(
        text=message_text, reply_markup=keyboard_markup, parse_mode=ParseMode.HTML
    )
    return states.OTHER_HELP_STATE


async def show_tinkoff_donation(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Клиентам Тинькофф'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(TINKOFF_DONATION_MENU_BUTTONS)
    message_text = "Выберите удобный вариант пожертвования"
    await query.edit_message_text(text=message_text, reply_markup=keyboard)


async def show_tinkoff_cashback(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Кэшбек во благо'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(TINKOFF_CASHBACK_MENU_BUTTONS)
    message_text = (
        "Оформите «Кэшбэк во благо» в приложении «Тинькофф»: \n\n"
        "1. На главном экране нажмите на счёт карты, с которой у вас начисляется кэшбек. \n"
        "2. Пролистайте вниз до блока «Куда зачислять». \n"
        "3. Нажмите на «Кэшбэк». \n"
        "4. Выберите пункт «Благотворительность». \n"
        "5. Пролистайте вниз и нажмите на кнопку «Все фонды». \n"
        "6. Введите в поиске: Событие и выберите фонд. \n\n"
        "✔️ Готово"
    )
    await query.edit_message_text(text=message_text, reply_markup=keyboard)
