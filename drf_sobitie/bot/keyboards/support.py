from typing import Sequence

from telegram import InlineKeyboardButton

from drf_sobitie.bot.keyboards.event import (
    create_notification_button_based_on_subscription_status,
)
from drf_sobitie.bot.keyboards.main import (
    GIVE_SUPPORT,
    SHORT_RETURN_BACK_BUTTON_TEXT,
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
OTHER_HELP = "OTHER_HELP"

# Константы для меню "Сделать пожертвование"
TINKOFF_DONATION = "TINKOFF_DONATION"

# Константы для подменю "Клиентам Т-банка"
TINKOFF_CASHBACK = "TINKOFF_CASHBACK"

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
            text="Сделать пожертвование",
            callback_data=SHOW_DONATION_OPTIONS,
        )
    ],
    # [
    #     InlineKeyboardButton(
    #         text="Приобрести сувениры",
    #         callback_data=ORDER_SOUVENIRS,
    #     )
    # ],
    # [
    #     InlineKeyboardButton(
    #         text="Создать сбор",
    #         callback_data=CREATE_COLLECTION,
    #     )
    # ],
    [
        InlineKeyboardButton(
            text="Стать активным подписчиком",
            callback_data=FOLLOW_US,
        )
    ],
    [
        InlineKeyboardButton(
            text="Связь по вопросам помощи",
            callback_data=COMMUNICATE_FOR_HELP,
        )
    ],
    # Кнопка "иная помощь" для раздела Как Помочь
    [
        InlineKeyboardButton(
            text="Иная помощь",
            callback_data=OTHER_HELP,
        )
    ],
    [create_return_to_start_button(text=SHORT_RETURN_BACK_BUTTON_TEXT)],
]

# Кнопки раздела "Сделать пожертвование"
DONATION_OPTIONS_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Форма на сайте", url="https://sobytie.center/howtohelp/"
        )
    ],
    # [
    #     InlineKeyboardButton(
    #         text='Благотворительный фонд "Нужна помощь"',
    #         url="https://nuzhnapomosh.ru/funds/centr-sobytie/",
    #     )
    # ],
    # [
    #     InlineKeyboardButton(
    #         text='Подписка "Рубль в день"', url="https://365.nuzhnapomosh.ru/f/sobytie"
    #     )
    # ],
    [
        InlineKeyboardButton(
            text="Клиентам Т-банка",
            callback_data=TINKOFF_DONATION,
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=GIVE_SUPPORT
        ),
    ],
]

# Кнопки раздела "Иная помощь"
OTHER_HELP_MENU_BUTTONS = [
    # Кнопка Назад - ведет на предыдущий раздел Как помочь
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT, callback_data=GIVE_SUPPORT
        ),
    ],
]

# КНОПКИ ПОДМЕНЮ "КЛИЕНТАМ Т-БАНКА"
TINKOFF_DONATION_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Разовое пожертвование",
            url="https://www.tinkoff.ru/payments/provider-sobytie/",
        )
    ],
    [
        InlineKeyboardButton(
            text="Кэшбек во благо",
            callback_data=TINKOFF_CASHBACK,
        )
    ],
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=SHOW_DONATION_OPTIONS,
        ),
    ],
]

# КНОПКИ ПОДМЕНЮ "КЭШБЕК ВО БЛАГО"
TINKOFF_CASHBACK_MENU_BUTTONS = [
    [
        InlineKeyboardButton(
            text=SHORT_RETURN_BACK_BUTTON_TEXT,
            callback_data=TINKOFF_DONATION,
        ),
    ],
]

SUPPORT_FOLLOW_BUTTONS = [
    [
        InlineKeyboardButton(
            text="Вконтакте:\n",
            callback_data=FOLLOW_US_VKONTAKTE,
            url="https://vk.com/sobytie.center",
        )
    ],
    [
        InlineKeyboardButton(
            text="Telegram:\n",
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
        ),
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
        ),
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


async def create_menu_other_help(
    user_id: int,
) -> Sequence[Sequence[InlineKeyboardButton]]:
    """Создаёт кнопки для клавиатуры раздела иной помощи."""
    notification_button = await create_notification_button_based_on_subscription_status(
        user_id=user_id
    )
    menu_other_help = [
        [notification_button],
        *OTHER_HELP_MENU_BUTTONS,
    ]
    return menu_other_help
