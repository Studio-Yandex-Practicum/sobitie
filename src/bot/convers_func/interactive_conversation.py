
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.keyboards.interactive import INTERACTIVE_BUTTONS
from core.states import INTERACTIVE_STATE


async def menu_interactive(update: Update, _: CallbackContext):
    """Меню 'Интерактив'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(INTERACTIVE_BUTTONS)

    if query.message.text is None:
        await query.delete_message()
        await query.message.reply_text(
        text="Интерактив",
        reply_markup=keyboard,
        )
    else:
        await query.edit_message_text(
            text="Интерактив",
            reply_markup=keyboard,
        )

    return INTERACTIVE_STATE


async def get_quiz(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Викторины'."""
    query = update.callback_query
    await query.message.reply_text(text="Здесь будут викторины")
    return
