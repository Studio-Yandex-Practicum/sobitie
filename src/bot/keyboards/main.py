from telegram import InlineKeyboardButton

ABOUT_US = 'ABOUT_US'
END = 'END'
EVENTS = 'EVENTS'
GIVE_SUPPORT = 'GIVE_SUPPORT'
INTERACTIVE_GAME = 'INTERACTIVE_GAME'
MAIN_TEXT = """Привет! Познакомимся?

«Событие» — творческое содружество.

Мы верим:
каждый человек — творец,
каждый уникален и выразителен,
каждый имеет право делиться творчеством с другими.

Мы знаем:
искусство — это способ взаимодействия с собой и миром. Мы посвящаем свою деятельность социокультурной реабилитации и \
социальной интеграции людей с особыми возможностями, содействуем раскрытию их творческого потенциала, повышению \
социального и культурного уровня. А ещё мы развиваем инклюзивное волонтёрство.

Выберите раздел меню, чтобы узнать больше.
"""
RETURN_TO_START = 'RETURN_TO_START'

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
