import emoji
from telegram import InlineKeyboardButton

from bot.keyboards.main import (
    GIVE_SUPPORT,
    RETURN_BACK_BUTTON_TEXT,
    SHORT_RETURN_BACK_BUTTON_TEXT,
    SHORT_RETURN_TO_START_BUTTON_TEXT,
    create_return_to_start_button,
)

# Константы для меню "Помочь"
ATTEND_EVENT = "ATTEND_EVENT"
COMMUNICATE_FOR_HELP = "COMMUNICATE_FOR_HELP"
OUR_NEEDS = "OUR_NEEDS"
SHOW_DONATION_OPTIONS = "SHOW_DONATION_OPTIONS"
PARTNERSHIP = "PARTNERSHIP"
ORDER_SOUVENIRS = "ORDER_SOUVENIRS"
BECOME_SPONSOR = "BECOME_SPONSOR"
BECOME_VOLUNTEER = "BECOME_VOLUNTEER"
FOLLOW_US = "FOLLOW_US"
FOLLOW_US_VKONTAKTE = "FOLLOW_US_VKONTAKTE"
FOLLOW_US_TELEGRAM = "FOLLOW_US_TELEGRAM"
CREATE_COLLECTION = "CREATE_COLLECTION"
CASHBACK = "CASHBACK"

# Константы для подменю "Заказать сувениры"
CHARITY_FAIR = "CHARITY_FAIR"
CORPORATE_FAIR = "CORPORATE_FAIR"

RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS = [
    [
        InlineKeyboardButton(text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=GIVE_SUPPORT),
        create_return_to_start_button(text=SHORT_RETURN_TO_START_BUTTON_TEXT),
    ]
]

# КНОПКИ МЕНЮ "ПОМОЧЬ"
SUPPORT_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':speech_balloon:')} Связь по вопросу помощи",
            callback_data=COMMUNICATE_FOR_HELP,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':credit_card:')} Сделать пожертвование",
            callback_data=SHOW_DONATION_OPTIONS,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':package:')} Заказать сувениры",
            callback_data=ORDER_SOUVENIRS,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':handshake::money_bag:')} Создать сбор", callback_data=CREATE_COLLECTION
        )
    ],
    [InlineKeyboardButton(text=f"{emoji.emojize(':money_with_wings:')} Подключить кешбэк", callback_data=CASHBACK)],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':mobile_phone_with_arrow:')} Стать активным подписчиком",
            callback_data=FOLLOW_US,
        )
    ],
    [create_return_to_start_button()],
]

# КНОПКИ ПОДМЕНЮ "ВЫБРАТЬ СПОСОБ ПОЖЕРТВОВАНИЯ"
DONATION_OPTIONS_MENU_BUTTONS = [
    [InlineKeyboardButton(text="Форма на сайте", url="https://sobytie.center/howtohelp/")],
    [
        InlineKeyboardButton(
            text='Благотворительный фонд "Нужна помощь"', url="https://nuzhnapomosh.ru/funds/centr-sobytie/"
        )
    ],
    [InlineKeyboardButton(text='Подписка "Рубль в день"', url="https://365.nuzhnapomosh.ru/")],
    [InlineKeyboardButton(text="Тинькофф", url="https://www.tinkoff.ru/payments/provider-sobytie/")],
    *RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS,
]

# кнопки для подписок на соцсети
SUPPORT_FOLLOW_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":blue_heart:")} Вконтакте:\n',
            callback_data=FOLLOW_US_VKONTAKTE,
            url="https://vk.com/sobytie.center",
        )
    ],
    [
        InlineKeyboardButton(
            text=f'{emoji.emojize(":star:")} Telegram:\n',
            callback_data=FOLLOW_US_TELEGRAM,
            url="https://t.me/sobytiecenter",
        )
    ],
    *RETURN_TO_SUPPORT_AND_RETURN_TO_START_BUTTONS,
]

MENU_ORDER_SUVENIR = [
    [InlineKeyboardButton(text="Благотворительная ярмарка", callback_data=CHARITY_FAIR)],
    [InlineKeyboardButton(text="Корпоративные подарки", callback_data=CORPORATE_FAIR)],
    [InlineKeyboardButton(text=RETURN_BACK_BUTTON_TEXT, callback_data=GIVE_SUPPORT)],
]
