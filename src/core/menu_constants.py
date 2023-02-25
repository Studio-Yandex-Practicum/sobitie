from telegram import InlineKeyboardButton

from src.core import constants

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
            callback_data=constants.EVENTS,
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
            callback_data=constants.GET_MASTER_CLASS,
        ),
    ],
    [
        InlineKeyboardButton(
            text='Спектакли',
            callback_data=constants.GET_PERFOMANSES,
        ),
    ],
    [
        InlineKeyboardButton(
            text='Сообщить о мероприятии',
            callback_data=constants.GET_EVENT,
        ),
    ],
]
