import urllib.request

import emoji
import requests
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.keyboards.interactive import INTERACTIVE_BUTTONS
from core.settings import QUOTE_URL
from core.states import INTERACTIVE_STATE


async def menu_interactive(update: Update, _: CallbackContext):
    """Меню 'Интерактив'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(INTERACTIVE_BUTTONS)
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


async def get_stickers(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Стикерпаки'."""
    query = update.callback_query
    await query.message.reply_text(text="Стикерпаки")
    return


async def get_quote(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Случайная цитата'."""
    response = requests.get(QUOTE_URL).json()
    quote = response[0].get("text")
    author = response[0].get("author")
    caption = f"{quote} \n\n{emoji.emojize(':writing_hand:')} {author}"
    query = update.callback_query
    if "image" in response[0]:
        image = response[0].get("image")
        photo = urllib.request.urlopen(image).read()
        await query.message.reply_photo(photo=photo, caption=caption)
        return
    await query.message.reply_text(text=caption)
    return
