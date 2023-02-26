import emoji

from telegram import InlineKeyboardButton
from src.core import constants

# КНОПКИ СТАРТОВОГО МЕНЮ
START_MENU_BUTTONS = [

        [
            InlineKeyboardButton(
                text='О нас',
                callback_data=constants.ABOUT_US,
            )
        ],
        [
            InlineKeyboardButton(
                text='Мероприятия',
                callback_data=constants.EVENTS,
            )
        ],
        [
            InlineKeyboardButton(
                text='Помочь',
                callback_data=constants.GIVE_SUPPORT,
            )
        ],
        [
            InlineKeyboardButton(
                text='Интерактив',
                callback_data=constants.INTERACTIVE_GAME,
            )
        ],
    ]

# КНОПКИ МЕНЮ "СОБЫТИЯ"
EVENTS_BUTTONS = [

     [
        InlineKeyboardButton(
            text='Мастер-классы',
            callback_data=constants.GET_MASTER_CLASS,
        ),

     ],
     [
        InlineKeyboardButton(
            text='Спектакли',
            callback_data=constants.GET_PERFORMANCES,
        ),
     ],
     [
        InlineKeyboardButton(
            text='Сообщить о мероприятии',
            callback_data=constants.GET_EVENT,
        ),

     ],
]

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
                callback_data=constants.SHOW_DONATION_OPTIONS
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':ticket:')} Прийти на спектакль",
                callback_data=constants.ATTEND_EVENT
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':thumbs_up:')} Партнерство",
                callback_data=constants.PARTNERSHIP
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':thumbs_up:')} Заказать суверниры",
                callback_data=constants.ORDER_SOUVENIRS
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':thumbs_up:')} Стать спонсором",
                callback_data=constants.BECOME_SPONSOR
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':thumbs_up:')} Стать волонтером",
                callback_data=constants.BECOME_VOLUNTEER
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':thumbs_up:')} Стать активным подписчиком",
                callback_data=constants.FOLLOW_US
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':reverse_button:')} Вернуться на предыдущую страницу",
                callback_data=constants.RETURN_TO_PREVIOUS
            )
        ],
    ]


# КНОПКИ МЕНЮ "О НАС"
ABOUT_US_MENU_BUTTONS = [

        [
            InlineKeyboardButton(
                text='Контакты',
                callback_data=constants.CONTACTS,
                url='http://sobytie.team/#about'
            )
        ],
        [
            InlineKeyboardButton(
                text='Уставные доументы',
                callback_data=constants.LEGAL_DOCUMENTS,
            )
        ],
        [
            InlineKeyboardButton(
                text='Отчеты о деятельности',
                callback_data=constants.REPORTS,
            )
        ],
        [
            InlineKeyboardButton(
                text='Проекты',
                callback_data=constants.PROJECTS,
            )
        ],
    ]


# КНОПКИ ПОДМЕНЮ "ВЫБРАТЬ СПОСОБ ПОЖЕРТВОВАНИЯ"
DONATION_OPTIONS_MENU_BUTTONS = [

        [
            InlineKeyboardButton(
                text='Форма на сайте',
                callback_data=constants.DONATE_WITH_SITE_FORM,
                # url='http://sobytie.team/#about'
            )
        ],
        [
            InlineKeyboardButton(
                text='Вконтакте',
                callback_data=constants.DONATE_WITH_VK,
            )
        ],
        [
            InlineKeyboardButton(
                text='Тинькофф',
                callback_data=constants.DONATE_WITH_TINKOFF,
            )
        ],
        [
            InlineKeyboardButton(
                text='Через Благотворительный фонд "Нужна помощь"',
                callback_data=constants.DONATE_THROUGH_CHARITY_FUND,
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':reverse_button:')}Вернуться в меню помощи",
                callback_data=constants.RETURN_TO_HELP_MENU,
            )
        ]
    ]

# кнопки для подписок на соцсети
SUPPORT_FOLLOW_BUTTONS = [
        [
            InlineKeyboardButton(
                text="ВКонтакте",
                callback_data=constants.FOLLOW_US_VKONTAKTE,
                url="https://vk.com/sobytie.center"
                
            )
        ],
        [
            InlineKeyboardButton(
                text="Telegram",
                callback_data=constants.FOLLOW_US_TELEGRAM,
                url="https://t.me/sobytiecenter"
            )
        ],
        [
            InlineKeyboardButton(
                text="Вернуться на предыдущую страницу",
                callback_data=constants.RETURN_TO_PREVIOUS
            )
        ],
    ]
