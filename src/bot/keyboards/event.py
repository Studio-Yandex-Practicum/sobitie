import emoji

from telegram import InlineKeyboardButton

# Константы для меню "Мероприятия"
CHOOSE_EVENT = 'CHOOSE_EVENT'
GET_MASTER_CLASS = 'GET_MASTER_CLASS'
GET_PERFORMANCES = 'GET_PERFORMANCES'
GET_EVENT = 'GET_EVENT'

# КНОПКИ МЕНЮ "Мероприятия"
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
            callback_data=GET_PERFORMANCES,
        ),
     ],
     [
        InlineKeyboardButton(
            text='Сообщить о мероприятии',
            callback_data=GET_EVENT,
        ),

     ],
]