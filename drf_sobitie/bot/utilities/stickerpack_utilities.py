from typing import Optional

from dataclasses import dataclass

from telegram import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from drf_sobitie.bot.utilities.common_utilities import emojify_text, read_photo_url


@dataclass
class StickerPackMessage:
    name: str
    url_sticker: str
    description: Optional[str] = None
    image_url: Optional[str] = None

    def __post_init__(self):
        self.text = f"{self.name} \n\n{self.description}\n\n"
        caption = emojify_text('-Забирай-', ':backhand_index_pointing_up:', surround=True)
        self.keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text=caption, url=self.url_sticker)]
            ])

def make_cleanup_keyboard(messages: list[Message]) -> InlineKeyboardMarkup:
    """Создание клавиатуры, хранящей в себе сообщения, 
       которые должны быть удалены при выходе из меню.
       Для этого используется arbitrary_callback_data."""
    return InlineKeyboardMarkup([[InlineKeyboardButton(text='Назад', callback_data=messages)]])


def make_stickerpack_message(sticker: dict) -> StickerPackMessage:
    return StickerPackMessage(name=sticker.get("name"), 
                              url_sticker=sticker.get("url_sticker"), 
                              description=sticker.get("description"), 
                              image_url=sticker.get("image"))


async def send_stickerpack_message(query: CallbackQuery, sticker: dict) -> Message:
    message = make_stickerpack_message(sticker)
    if message.image_url:
        photo = read_photo_url(message.image_url)
        return await query.message.reply_photo(reply_markup=message.keyboard,
                                                        photo=photo, 
                                                        caption=message.text)
    return await query.message.reply_text(reply_markup=message.keyboard, 
                                                        text=message.text)
