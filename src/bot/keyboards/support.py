from typing import Sequence

import emoji
from telegram import InlineKeyboardButton

from bot.keyboards.event import create_notification_button_based_on_subscription_status
from bot.keyboards.main import (
    GIVE_SUPPORT,
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

RETURN_TO_SUPPORT_BUTTON = [
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=GIVE_SUPPORT
        )
    ],
]

SUPPORT_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':credit_card:')} Сделать пожертвование",
            callback_data=SHOW_DONATION_OPTIONS,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':package:')} Приобрести сувениры",
            callback_data=ORDER_SOUVENIRS,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':handshake::money_bag:')} Создать сбор",
            callback_data=CREATE_COLLECTION,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':money_with_wings:')} Подключить кешбэк",
            callback_data=CASHBACK,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':mobile_phone_with_arrow:')} Стать активным подписчиком",
            callback_data=FOLLOW_US,
        )
    ],
    [
        InlineKeyboardButton(
            text=f"{emoji.emojize(':speech_balloon:')} Связь по вопросу помощи",
            callback_data=COMMUNICATE_FOR_HELP,
        )
    ],
    [create_return_to_start_button(text=SHORT_RETURN_BACK_BUTTON_TEXT)],
]

DONATION_OPTIONS_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Форма на сайте", url="https://sobytie.center/howtohelp/"
        )
    ],
    [
        InlineKeyboardButton(
            text='Благотворительный фонд "Нужна помощь"',
            url="https://nuzhnapomosh.ru/funds/centr-sobytie/",
        )
    ],
    [
        InlineKeyboardButton(
            text='Подписка "Рубль в день"', url="https://365.nuzhnapomosh.ru/f/sobytie"
        )
    ],
    [
        InlineKeyboardButton(
            text="Тинькофф", url="https://www.tinkoff.ru/payments/provider-sobytie/"
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=GIVE_SUPPORT
        ),
    ],
]

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
    *RETURN_TO_SUPPORT_BUTTON,
]

SUPPORT_CREATE_COLLECTION_BUTTONS = [
   [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=GIVE_SUPPORT
        ),
        InlineKeyboardButton(
            text="Перейти на сайт",
            url="https://sluchaem.ru/",
        )
    ]
]

SUPPORT_ORDER_SOUVENIR = [
   [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=GIVE_SUPPORT
        ),
        InlineKeyboardButton(
            text="Перейти в магазин",
            url="https://vk.com/market-190536221",
        )
    ]
]


async def create_menu_order_souvenir(
    user_id: int,
) -> Sequence[Sequence[InlineKeyboardButton]]:
    """Создаёт кнопки для клавиатуры раздела приобретения сувениров."""
    notification_button = await create_notification_button_based_on_subscription_status(
        user_id=user_id
    )
    menu_order_souvenir = [
        [notification_button],
        *SUPPORT_ORDER_SOUVENIR,
    ]
    return menu_order_souvenir
