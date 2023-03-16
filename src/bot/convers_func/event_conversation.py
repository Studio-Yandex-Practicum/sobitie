from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.keyboards.event import EVENT_MENU, EVENT_MENU_BUTTONS


async def show_event_menu(update: Update, _: CallbackContext):
    """Отправляет клавиатуру с меню раздела мероприятий."""
    keyboard = InlineKeyboardMarkup(EVENT_MENU_BUTTONS)
    await update.callback_query.answer()
    message_text = """Мы организуем показы спектаклей, проводим открытые репетиции, мастер-классы, участвуем в \
благотворительных ярмарках, фестивалях...
Хотите узнать больше о предстоящих событиях?"""
    await update.callback_query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )
    return EVENT_MENU


async def show_upcoming_events(update: Update, _: CallbackContext):
    """Отправляет сообщения с ближайшими событиями."""
    pass


async def show_gratitude_and_subscribe_to_notifications(update: Update, _: CallbackContext):
    """Отправляет сообщение благодарности за подписку и включает уведомления пользователю на события."""
    pass
