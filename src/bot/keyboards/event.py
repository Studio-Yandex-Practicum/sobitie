import emoji
from telegram import InlineKeyboardButton

from bot.keyboards.main import create_return_to_start_button

# Константы для меню "Мероприятия"
CHOOSE_EVENT = 'CHOOSE_EVENT'
GET_MASTER_CLASS = 'GET_MASTER_CLASS'
GET_PERFORMANCES = 'GET_PERFORMANCES'
RETURN_TO_BACK='EVENTS'
RETURN_TO_BACK_BUTTON_TEXT = f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу"

# КНОПКИ МЕНЮ "Мероприятия"
EVENTS_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':artist:')} 'Мастер-классы'",
            callback_data=GET_MASTER_CLASS,
        ),
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':performing_arts:')} 'Спектакли'",
            callback_data=GET_PERFORMANCES,
        ),
    ],
    [
        create_return_to_start_button(),
    ],
]


# Кнопка возврата на предыдущую страницу
BUTTON_BACK = [
    [
        InlineKeyboardButton(
            text=RETURN_TO_BACK_BUTTON_TEXT,
            callback_data=RETURN_TO_BACK,
        )
    ],
]