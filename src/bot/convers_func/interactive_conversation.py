import requests
import emoji
from telegram import InlineKeyboardMarkup, Update

from core.states import INTERACTIVE_STATE
from bot.keyboards.interactive import INTERACTIVE_BUTTONS

QUOTE_URL = "https://zenquotes.io/api/random"


async def menu_interactive(update: Update, context):
    """Меню 'Интерактив'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(INTERACTIVE_BUTTONS)
    await query.edit_message_text(
        text='Интерактив',
        reply_markup=keyboard,
    )
    return INTERACTIVE_STATE


async def get_quiz(update: Update, context):
    """Нажатие на кнопку 'Викторины'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Здесь будут викторины'
    )
    return


async def ask_question(update: Update, context):
    """Нажатие на кнопку 'Вопрос-ответ'."""
    query = update.callback_query
    await query.message.reply_text(
        text='Задать вопрос'
    )
    return


async def get_quote(update: Update, context):
    """Нажатие на кнопку 'Случайная цитата'."""
    response = requests.get(QUOTE_URL).json()
    quote = response[0].get('q')
    author = response[0].get('a')
    query = update.callback_query
    await query.message.reply_text(
        text=f"{quote} {emoji.emojize(':writing_hand:')} {author}"
    )
    return
