import urllib.request

import emoji
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.keyboards.interactive import INTERACTIVE_BUTTONS, RETURN_TO_INTERACTIVE_MENU_BUTTON
from drf_sobitie.settings import QUOTE_URL, STICKERPACK_URL
from drf_sobitie.constants import INTERACTIVE_STATE


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


async def get_stickers(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Стикерпаки'."""
    response = requests.get(STICKERPACK_URL).json()
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(RETURN_TO_INTERACTIVE_MENU_BUTTON)

    def absence_stikers(text, my_moji):
        return (
            f"{emoji.emojize(my_moji)}"
            f"{text}"
            f"{emoji.emojize(my_moji)}"
        )

    if len(response) < 1:
        await query.edit_message_text(
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
            text = (
                f"{name} \n\n{description}\n\n"
            )
            caption = (
                f"{emoji.emojize(':backhand_index_pointing_up:')}"
                f"-Забирай-{emoji.emojize(':backhand_index_pointing_up:')}"
            )
            sticker_keyboard = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        text=caption,
                        url=url_sticker,
                    )
                ]]
            )
            query = update.callback_query
            if image:
                photo = urllib.request.urlopen(image).read()
                await query.message.reply_photo(photo=photo)
            await query.message.reply_text(reply_markup=sticker_keyboard, text=text)
        await query.edit_message_text(
            text=(
                f"Выбирайте и добавляйте себе понравившиеся варианты стикерпаков - их создают ученики нашего центра. А мы будем создавать для вас новые!"
                f"{emoji.emojize(':backhand_index_pointing_up:')}"
            ),
            reply_markup=keyboard
        )
        return
    await query.edit_message_text(
        text=absence_stikers("Редактируем, скоро релиз!!", ":fire:"),
        reply_markup=keyboard
    )
    return


async def get_quote(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Цитата недели'."""
    response = requests.get(QUOTE_URL).json()
    keyboard = InlineKeyboardMarkup(RETURN_TO_INTERACTIVE_MENU_BUTTON)
    query = update.callback_query
    if len(response) < 1:
        await query.edit_message_text(
            text=(
                f"{emoji.emojize(':detective:')}"
                f"В поисках подходящей цитаты"
                f"{emoji.emojize(':detective:')}"
            ), reply_markup=keyboard
        )
        return

    quote = response[0].get("text")
    if "image" in response[0] and response[0].get("image") is not None:
        image = response[0].get("image")
        photo = urllib.request.urlopen(image).read()
        await query.delete_message()
        await query.message.reply_photo(
            caption=quote,
            photo=photo,
            reply_markup=keyboard
        )
        return
    
    await query.edit_message_text(text=quote, reply_markup=keyboard)
    return