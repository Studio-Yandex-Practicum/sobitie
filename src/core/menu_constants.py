from telegram import InlineKeyboardButton

from src.core.constants import EVENTS, GET_MASTER_CLASS, GET_PERFOMANSES, GET_EVENT

BUTTONS_MAIN_MENU = [
    [
        InlineKeyboardButton(
            text='О нас',
            callback_data='TestCallback',
        )
    ],
    [
        InlineKeyboardButton(
            text='Мероприятия',
            callback_data=EVENTS,
        )
    ],
    [
        InlineKeyboardButton(
            text='Помочь',
            callback_data='TestCallbackdata2',
        )
    ],
    [
        InlineKeyboardButton(
            text='Интерактив',
            callback_data='TestCallbackdata2',
        )
    ],
]

EVENTS_BUTTONS = [
     [
        InlineKeyboardButton(
            text='Мастер-классы',
            callback_data=GET_MASTER_CLASS,
        ),
    ],
    [
        InlineKeyboardButton(
            text='Спектакли',
            callback_data=GET_PERFOMANSES,
        ),
    ],
    [
        InlineKeyboardButton(
            text='Сообщить о мероприятии',
            callback_data=GET_EVENT,
        ),
    ],
]
