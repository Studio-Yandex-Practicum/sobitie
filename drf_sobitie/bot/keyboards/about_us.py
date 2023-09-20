import emoji
from telegram import InlineKeyboardButton

from bot.keyboards.main import (
    ABOUT_US,
    RETURN_BACK_BUTTON_TEXT,
    SHORT_RETURN_BACK_BUTTON_TEXT,
    SHORT_RETURN_TO_START_BUTTON_TEXT,
    create_return_to_start_button,
)

# Константы для меню "О нас"
CONTACTS = "CONTACTS"
LEGAL_DOCUMENTS = "LEGAL_DOCUMENTS"
REPORTS = "REPORTS"
PROJECTS = "PROJECTS"
PEOPLE = "PEOPLE"

# Константы для подменю "Документы"
STATUTORY_DOCUMENTS = "STATUTORY_DOCUMENTS"

# Константы для подменю "Отчёты"
REPORTS_MINISTRY = "REPORTS_MINISTRY"
ANNUAL_REPORTS = "ANNUAL_REPORTS"

# Константы для подменю "Проекты"
INCLUSIVE_WORKSHOP = "INCLUSIVE_WORKSHOP"
THEATRE_SCHOOL = "THEATRE_SCHOOL"
MOSCOW_ONLINE = "MOSCOW_ONLINE"

# Константы для подменю "Контакты"
CONTACTS_INFO = "CONTACTS_INFO"
EMAIL_INFO = "EMAIL_INFO"

# Константы кнопки "НАЗАД"
RETURN_TO_BACK = "RETURN_TO_BACK"

RETURN_BACK_BUTTON = [
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=RETURN_TO_BACK,
        ),
    ],
]

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
            text=f"{emoji.emojize(':chart_increasing:')} Уставные документы. Реквизиты",
            callback_data=LEGAL_DOCUMENTS,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':card_file_box:')} Отчеты о деятельности",
            callback_data=REPORTS,
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
    [create_return_to_start_button(text=SHORT_RETURN_BACK_BUTTON_TEXT)],
]

# КНОПКИ ПОДМЕНЮ "ДОКУМЕНТЫ"
DOCUMENTS_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Уставные документы",
            callback_data=STATUTORY_DOCUMENTS,
            url="https://sobytie.center/documents/",
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=ABOUT_US,
        )
    ],
]

# КНОПКИ ПОДМЕНЮ "ОТЧЁТЫ"
REPORTS_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Посмотреть отчёты на сайте Минюста РФ",
            callback_data=REPORTS_MINISTRY,
        )
    ],
    [
        InlineKeyboardButton(
            text="Ознакомиться с годовыми отчётами",
            callback_data=ANNUAL_REPORTS,
            url="https://sobytie.center/reports/",
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=ABOUT_US
        )
    ],
]

# КНОПКИ ПОДМЕНЮ "ОТЧЁТЫ НА ПОРТАЛЕ МИНЮСТА"
MINISTRY_REPORTS_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Информационный портал Минюста РФ",
            url="http://unro.minjust.ru/NKOReports.aspx",
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=REPORTS,
        )
    ],
]

# КНОПКИ ПОДМЕНЮ "ПРОЕКТЫ"
PROJECTS_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':artist:')} Инклюзивная мастерская",
            callback_data=INCLUSIVE_WORKSHOP,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':school:')} Театральная студия i-Школы",
            callback_data=THEATRE_SCHOOL,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':cityscape:')} Москва - Партала. Онлайн.",
            callback_data=MOSCOW_ONLINE,
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=ABOUT_US,
        )
    ],
]

# КНОПКИ ПОДМЕНЮ "КОНТАКТЫ"
CONTACTS_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':envelope:')} Электронная почта",
            callback_data=EMAIL_INFO,
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":page_facing_up:")} Форма обратной связи:',
            url="https://forms.yandex.ru/cloud/63ee7e3bc417f30921e2fe6e/",
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":blue_heart:")} Вконтакте:\n',
            url="https://vk.com/sobytie.center",
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":star:")} Telegram:\n',
            url="https://t.me/sobytiecenter",
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=ABOUT_US
        )
    ],
]

# Кнопки подменю "Люди"
PEOPLE_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":collision:")}Кураторы проектов',
            url="https://sobytie.center/contacts/",
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":fire:")} Актёры ИТС "Событие"',
            url="https://sobytie.center/actors/",
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":sparkles:")} Волонтёры',
            url="https://sobytie.center/volunteers/",
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=ABOUT_US,
        )
    ],
]


# Кнопки подменю "Инклюзивная мастерская"
INCLUSIVE_WORKSHOP_BUTTON = [
    [
        InlineKeyboardButton(
            text='О мастерской',
            url="https://sobytie.center/project/inklyuzivnaya-masterskaya/",
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=RETURN_TO_BACK,
        )
    ],

]

# Кнопки подменю "Инклюзивная мастерская"
THEATRE_SCHOOL_BUTTON = [
    [
        InlineKeyboardButton(
            text='О студии',
            url="https://sobytie.center/teatrischool",
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=RETURN_TO_BACK,
        )
    ],

]

# Кнопки подменю "Москва-Партала.Онлайн"
MOSCOW_ONLINE_BUTTONS = [
    [
        InlineKeyboardButton(
            text='Москва - Партала. Онлайн.',
            url="https://sobytie.center/project/moskva-partala-onlajn/",
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=RETURN_TO_BACK,
        )
    ],

]


# Кнопки подменю "Электронная почта""
EMAIL_INFO_BUTTON = [
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=CONTACTS,
        )
    ],

]