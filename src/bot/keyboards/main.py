from telegram import InlineKeyboardButton

# Константы стратового меню
ABOUT_US = 'ABOUT_US'
END = 'END'
EVENTS = 'EVENTS'
GIVE_SUPPORT = 'GIVE_SUPPORT'
INTERACTIVE_GAME = 'INTERACTIVE_GAME'

# КНОПКИ СТАРТОВОГО МЕНЮ
START_MENU_BUTTONS = [

        [
            InlineKeyboardButton(
                text='О нас',
                callback_data=ABOUT_US,
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
                callback_data=GIVE_SUPPORT,
            )
        ],
        [
            InlineKeyboardButton(
                text='Интерактив',
                callback_data=INTERACTIVE_GAME,
            )
        ],
    ]
