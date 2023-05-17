import urllib.request

import emoji
import requests
import json
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.keyboards.interactive import INTERACTIVE_BUTTONS, RETURN_TO_INTERACTIVE_MENU_BUTTON
from core.settings import QUOTE_URL, STICKERPACK_URL
from core.states import INTERACTIVE_STATE


async def menu_interactive(update: Update, _: CallbackContext):
    """Меню 'Интерактив'."""
    query = update.callback_query
    await query.answer()

    keyboard = InlineKeyboardMarkup(INTERACTIVE_BUTTONS)
    await query.message.reply_text(
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
    response = requests.get(STICKERPACK_URL)
    print()
    print(response.status_code)
    print()
    print(response.url)
    print()
    print(response.text)
    print()

    response = json.loads(response.text)
    keyboard = InlineKeyboardMarkup([[RETURN_TO_INTERACTIVE_MENU_BUTTON]])
    query = update.callback_query

    def absence_stikers(text, my_moji):
        return (
            f"{emoji.emojize(my_moji)}"
            f"{text}"
            f"{emoji.emojize(my_moji)}"
        )

    if len(response) < 1:
        await query.message.reply_text(
            text=absence_stikers(
                "Стикеры пока не завезли, ждем на днях",
                ':ship:'
            ), reply_markup=keyboard
        )
        return

    active_stickerpaks = []
    for index, i in enumerate(response):
        if i["is_active"]:
            active_stickerpaks.append(index)
    if active_stickerpaks:
        for i in active_stickerpaks:
            name = response[i].get("name")
            description = response[i].get("description")
            url_sticker = response[i].get("url_sticker")
            image = response[i].get("image")
            caption = (
                f"{name} \n\n{description}\n\n{url_sticker}\n"
                f"{emoji.emojize(':backhand_index_pointing_up:')}"
                f"-Забирай-{emoji.emojize(':backhand_index_pointing_up:')}"
            )
            query = update.callback_query
            if image:
                photo = urllib.request.urlopen(image).read()
                await query.message.reply_photo(photo=photo)
            await query.message.reply_text(text=caption)
        await query.message.reply_text(
            text=f"{emoji.emojize(':backhand_index_pointing_up:')}",
            reply_markup=keyboard
        )
        return
    await query.message.reply_text(
        text=absence_stikers("Редактируем, скоро релиз!!", ":fire:"),
        reply_markup=keyboard
    )
    return


async def get_quote(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Случайная цитата'."""
    response = requests.get(QUOTE_URL).json()
    keyboard = InlineKeyboardMarkup([[RETURN_TO_INTERACTIVE_MENU_BUTTON]])
    query = update.callback_query
    if len(response) < 1:
        await query.message.reply_text(
            text=(
                f"{emoji.emojize(':detective:')}"
                f"В поисках подходящей цитаты"
                f"{emoji.emojize(':detective:')}"
            ), reply_markup=keyboard
        )
        return

    quote = response[0].get("text")
    author = response[0].get("author")
    caption = f"{quote} \n\n{emoji.emojize(':writing_hand:')} {author}"
    if "image" in response[0] and response[0].get("image") is not None:
        image = response[0].get("image")
        photo = urllib.request.urlopen(image).read()
        await query.message.reply_photo(
            photo=photo,
            caption=caption,
            reply_markup=keyboard
        )
        return
    await query.edit_message_text(text=caption, reply_markup=keyboard)
    return
