import emoji

from telegram import InlineKeyboardButton


# Константы для меню "О нас"
CONTACTS = 'CONTACTS'
LEGAL_DOCUMENTS = 'LEGAL_DOCUMENTS'
REPORTS = 'REPORTS'
PROJECTS = 'PROJECTS'
PEOPLE = 'PEOPLE'
RETURN_TO_MAIN = 'RETURN_TO_MAIN'


# Константы для подменю "Проекты"
INCLUSIVE_THEATRE = 'INCLUSIVE_THEATRE'
INCLUSIVE_WORKSHOP = 'INCLUSIVE_WORKSHOP'
MOSCOW_ONLINE = 'MOSCOW_ONLINE'
RETURN_TO_ABOUT_US = 'RETURN_TO_ABOUT_US'


# КНОПКИ МЕНЮ "О НАС"
ABOUT_US_MENU_BUTTONS = [

        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':open_mailbox_with_raised_flag:')} Контакты",
                callback_data=CONTACTS,
                url='https://sobytie.center/contacts/'
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':chart_increasing:')} Уставные доументы",
                callback_data=LEGAL_DOCUMENTS,
                url='https://sobytie.center/documents/'
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':card_file_box:')} Отчеты о деятельности",
                callback_data=REPORTS,
                url='https://sobytie.center/reports/'
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':hatching_chick:')} Проекты",
                callback_data=PROJECTS,
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':woman_and_man_holding_hands:')} Люди",
                callback_data=PEOPLE,
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу",
                callback_data=RETURN_TO_MAIN,
            )
        ],
    ]


# КНОПКИ ПОДМЕНЮ "ПРОЕКТЫ"
PROJECTS_MENU_BUTTONS = [
    [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':performing_arts:')} Инклюзивный театр-студия 'Событие'",
                callback_data=INCLUSIVE_THEATRE,
                
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':artist:')} Инклюзивная мастерская",
                callback_data=INCLUSIVE_WORKSHOP,
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':cityscape:')} Москва - Партала. Онлайн.",
                callback_data=MOSCOW_ONLINE,
                url='https://sobytie.center/project/moskva-partala-onlajn/',
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу",
                callback_data=RETURN_TO_ABOUT_US,
            )
        ],
]
