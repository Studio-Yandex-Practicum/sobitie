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

# Константы для подменю "Контакты"
CONTACTS_INFO = 'CONTACTS_INFO'
RETURN_TO_START = 'RETURN_TO_START'

# КНОПКИ МЕНЮ "О НАС"
ABOUT_US_MENU_BUTTONS = [

        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':open_mailbox_with_raised_flag:')} Контакты",
                callback_data=CONTACTS,
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

#КНОПКИ ПОДМЕНЮ "КОНТАКТЫ"
CONTACTS_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':envelope:')} "
                 f"Электронная почта",
            url='mailto:sobytie.center@yandex.ru',
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":page_facing_up:")} Форма обратной связи:',
            url='https://forms.yandex.ru/cloud/63ee7e3bc417f30921e2fe6e/'
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":blue_heart:")} Вконтакте:\n',
            url='https://vk.com/sobytie.center',
        )
    ],
[
        InlineKeyboardButton(
            text=f'{emoji.emojize(":star:")} Telegram:\n',
            url='https://t.me/sobytiecenter',
        )
    ],
    [
        InlineKeyboardButton(
            text='Вернуться в главное меню',
            callback_data=RETURN_TO_START,
        )
    ],
]

#Кнопки подменю "Люди"
PEOPLE_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":collision:") }Кураторы проектов',
            url='https://test.ru',
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":fire:")} Актёры Инклюзивного театра-студии «Событие»',
            url='https://test.ru',
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":sparkles:")} Волонтёры',
            url='https://test.ru',
        )
    ],
    [
        InlineKeyboardButton(
            text='Вернуться в главное меню',
            callback_data=RETURN_TO_START,
        )
    ],
]
