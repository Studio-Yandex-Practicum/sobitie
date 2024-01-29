from telegram import InlineKeyboardButton

from drf_sobitie.bot.keyboards.main import (
    ABOUT_US,
    SHORT_RETURN_BACK_BUTTON_TEXT,
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
INCLUSIVE_THEATER = "INCLUSIVE THEATER"

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
            text="Контакты",
            callback_data=CONTACTS,
        )
    ],
    [
        InlineKeyboardButton(
            text="Уставные документы",
            callback_data=LEGAL_DOCUMENTS,
        )
    ],
    [
        InlineKeyboardButton(
            text="Ознакомиться с годовыми отчётами",
            callback_data=REPORTS,
        )
    ],
    [
        InlineKeyboardButton(
            text="Проекты",
            callback_data=PROJECTS,
        )
    ],
    [
        InlineKeyboardButton(
            text="Люди",
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
    [InlineKeyboardButton(text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=ABOUT_US)],
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
            text="Инклюзивная мастерская",
            callback_data=INCLUSIVE_WORKSHOP,
        )
    ],
    [
        InlineKeyboardButton(
            text="Театральная студия i-Школы",
            callback_data=THEATRE_SCHOOL,
        )
    ],
    [
        InlineKeyboardButton(
            text="Москва - Партала. Онлайн",
            callback_data=MOSCOW_ONLINE,
        )
    ],
    [
        InlineKeyboardButton(
            text="Инклюзивный театр",
            callback_data=INCLUSIVE_THEATER,
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
            text="Электронная почта",
            callback_data=EMAIL_INFO,
        )
    ],
    [
        InlineKeyboardButton(
            text="Форма обратной связи:",
            url="https://forms.yandex.ru/cloud/63ee7e3bc417f30921e2fe6e/",
        )
    ],
    [
        InlineKeyboardButton(
            text="Вконтакте:",
            url="https://vk.com/sobytie.center",
        )
    ],
    [
        InlineKeyboardButton(
            text="Telegram:",
            url="https://t.me/sobytiecenter",
        )
    ],
    [InlineKeyboardButton(text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=ABOUT_US)],
]

# Кнопки подменю "Люди"
PEOPLE_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Кураторы проектов",
            url="https://sobytie.center/contacts/",
        )
    ],
    [
        InlineKeyboardButton(
            text='Актёры ИТС "Событие"',
            url="https://sobytie.center/actors/",
        )
    ],
    [
        InlineKeyboardButton(
            text="Волонтёры",
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
            text="О мастерской",
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
            text="О студии",
            url="https://vk.com/teatr.ischool",
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
            text="Москва - Партала. Онлайн",
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

INCLUSIVE_THEATER_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Инклюзивный театр",
            url="https://sobytie.center/project/inklyuzivnyj-teatr-studiya-sobytie/",
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
