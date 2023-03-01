import emoji
from telegram import InlineKeyboardButton

# Константы для меню "Помочь"
ATTEND_EVENT = 'ATTEND_EVENT'
OUR_NEEDS = 'OUR_NEEDS'
SHOW_DONATION_OPTIONS = 'SHOW_DONATION_OPTIONS'
PARTNERSHIP = 'PARTNERSHIP'
ORDER_SOUVENIRS = 'ORDER_SOUVENIRS'
BECOME_SPONSOR = 'BECOME_SPONSOR'
BECOME_VOLUNTEER = 'BECOME_VOLUNTEER'
FOLLOW_US = 'FOLLOW_US'
RETURN_TO_PREVIOUS = 'RETURN_TO_PREVIOUS'
FOLLOW_US_VKONTAKTE = 'FOLLOW_US_VKONTAKTE'
FOLLOW_US_TELEGRAM = 'FOLLOW_US_TELEGRAM'

# Константы для подменю "Выбрать способ пожертвования"
DONATE_WITH_SITE_FORM = 'DONATE_WITH_SITE_FORM'
DONATE_WITH_VK = 'DONATE_WITH_VK'
DONATE_WITH_TINKOFF = 'DONATE_WITH_TINKOFF'
DONATE_THROUGH_CHARITY_FUND = 'DONATE_THROUGH_CHARITY_FUND'
RETURN_TO_HELP_MENU = 'RETURN_TO_HELP_MENU'

# Константы для подменю "Заказать сувениры"
CHARITY_FAIR = 'CHARITY_FAIR'
CORPORATE_FAIR = 'CORPORATE_FAIR'

# КНОПКИ МЕНЮ "ПОМОЧЬ"
SUPPORT_MENU_BUTTONS = [

        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':thumbs_up:')} Наши нужды",
                callback_data='Our needs'
            )
        ],

        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':credit_card:')} Выбрать способ пожертвования",
                callback_data=SHOW_DONATION_OPTIONS
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':performing_arts:')} Прийти на спектакль",
                callback_data=ATTEND_EVENT
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':handshake:')} Партнерство",
                callback_data=PARTNERSHIP
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':package:')} Заказать суверниры",
                callback_data=ORDER_SOUVENIRS
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':dollar_banknote:')} Стать спонсором",
                callback_data=BECOME_SPONSOR
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':flexed_biceps:')} Стать волонтером",
                callback_data=BECOME_VOLUNTEER
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':mobile_phone_with_arrow:')} Стать активным подписчиком",
                callback_data=FOLLOW_US
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':reverse_button:')} Вернуться на предыдущую страницу",
                callback_data=RETURN_TO_PREVIOUS
            )
        ],
    ]

# КНОПКИ ПОДМЕНЮ "ВЫБРАТЬ СПОСОБ ПОЖЕРТВОВАНИЯ"
DONATION_OPTIONS_MENU_BUTTONS = [

        [
            InlineKeyboardButton(
                text='Форма на сайте',
                callback_data=DONATE_WITH_SITE_FORM,
                # url='http://sobytie.team/#about'
            )
        ],
        [
            InlineKeyboardButton(
                text='Вконтакте',
                callback_data=DONATE_WITH_VK,
            )
        ],
        [
            InlineKeyboardButton(
                text='Тинькофф',
                callback_data=DONATE_WITH_TINKOFF,
            )
        ],
        [
            InlineKeyboardButton(
                text='Через Благотворительный фонд "Нужна помощь"',
                callback_data=DONATE_THROUGH_CHARITY_FUND,
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':reverse_button:')}Вернуться в меню помощи",
                callback_data=RETURN_TO_HELP_MENU,
            )
        ]
    ]

# кнопки для подписок на соцсети
SUPPORT_FOLLOW_BUTTONS = [
    [
        InlineKeyboardButton(
            text="ВКонтакте",
            callback_data=FOLLOW_US_VKONTAKTE,
            url="https://vk.com/sobytie.center"

        )
    ],
    [
        InlineKeyboardButton(
            text="Telegram",
            callback_data=FOLLOW_US_TELEGRAM,
            url="https://t.me/sobytiecenter"
        )
    ],
    [
        InlineKeyboardButton(
            text="Вернуться на предыдущую страницу",
            callback_data=RETURN_TO_PREVIOUS
        )
    ],
]


MENU_ORDER_SUVENIR = [
    [
        InlineKeyboardButton(
            text='Благотворительная ярмарка',
            callback_data=CHARITY_FAIR
        )
    ],
    [
        InlineKeyboardButton(
            text='Корпоративные подарки',
            callback_data=CORPORATE_FAIR
        )
    ],
    [
        InlineKeyboardButton(
            text='Назад',
            callback_data=RETURN_TO_HELP_MENU
        )
    ]
]
