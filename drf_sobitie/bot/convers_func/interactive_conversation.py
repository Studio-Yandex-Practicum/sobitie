from telegram import Update
from telegram.ext import CallbackContext

from drf_sobitie.bot.api_client import get_client
from drf_sobitie.bot.constants import INTERACTIVE_STATE
from drf_sobitie.bot.keyboards.interactive import INTERACTIVE_MENU_KEYBOARD, RETURN_TO_INTERACTIVE_MENU_KEYBOARD
from drf_sobitie.bot.utilities import emojify_text, make_cleanup_keyboard, read_photo_url, send_stickerpack_message


async def menu_interactive(update: Update, _: CallbackContext):
    """Меню 'Интерактив'."""
    query = update.callback_query
    await query.answer()

    if query.message.text is None:
        await query.delete_message()
        await query.message.reply_text(
            text="Интерактив",
            reply_markup=INTERACTIVE_MENU_KEYBOARD,
        )
    else:
        await query.edit_message_text(
            text="Интерактив",
            reply_markup=INTERACTIVE_MENU_KEYBOARD,
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
    await query.answer()
    api_client = get_client()
    response = await api_client.get_stickers()
    response = response.json()

    active_stickers = [i for i in response if i['is_active']]
    if not active_stickers:
        await query.edit_message_text(
            text=emojify_text("Стикеры пока не завезли, ждем на днях", ":ship:", surround=True),
            reply_markup=RETURN_TO_INTERACTIVE_MENU_KEYBOARD,
        )
        return
    sent_messages = [await send_stickerpack_message(query, sticker) for sticker in active_stickers]
    welcome_text = (
        "Выбирайте и добавляйте себе понравившиеся варианты стикерпаков - их создают ученики нашего центра. "
        "А мы будем создавать для вас новые!")
    await query.edit_message_text(
        text=emojify_text(welcome_text,':backhand_index_pointing_up:'),
        reply_markup=make_cleanup_keyboard(sent_messages))


async def cleanup_stickerpack_messages(update: Update, context: CallbackContext):
    """Удаление сообщений со скачиванием стикеров.
        Получает сообщения из arbitrary_callback_data, удаляет по одному.
        Удаляет welcome-сообщения и очищает кэш контекста для будущей работы."""
    query = update.callback_query
    await query.answer()
    for message in query.data:
        await message.delete()
    await query.delete_message()
    context.drop_callback_data(query)
    await query.message.reply_text(
            text="Интерактив",
            reply_markup=INTERACTIVE_MENU_KEYBOARD,
        )


async def get_quote(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Цитата недели'."""
    query = update.callback_query
    api_client = get_client()
    response = await api_client.get_quote()
    response = response.json()
    if len(response) < 1:
        await query.edit_message_text(
            text=emojify_text("В поисках подходящей цитаты", ':detective:', surround=True),
            reply_markup=RETURN_TO_INTERACTIVE_MENU_KEYBOARD,
        )
        return

    quote = response[0].get("text")
    if "image" in response[0] and response[0].get("image") is not None:
        image = response[0].get("image")
        photo = read_photo_url(image)
        await query.delete_message()
        await query.message.reply_photo(
            caption=quote, photo=photo, reply_markup=RETURN_TO_INTERACTIVE_MENU_KEYBOARD
        )
        return

    await query.edit_message_text(text=quote, reply_markup=RETURN_TO_INTERACTIVE_MENU_KEYBOARD)
    return
