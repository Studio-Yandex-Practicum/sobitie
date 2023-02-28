import emoji

from telegram import InlineKeyboardButton
from core import constants

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
                text=f"{emoji.emojize(':performing_arts:')} Прийти на спектакль",
                callback_data=constants.ATTEND_EVENT
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':handshake:')} Партнерство",
                callback_data=constants.PARTNERSHIP
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':package:')} Заказать суверниры",
                callback_data=constants.ORDER_SOUVENIRS
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':dollar_banknote:')} Стать спонсором",
                callback_data=constants.BECOME_SPONSOR
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':flexed_biceps:')} Стать волонтером",
                callback_data=constants.BECOME_VOLUNTEER
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':mobile_phone_with_arrow:')} Стать активным подписчиком",
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
                text=f"{emoji.emojize(':open_mailbox_with_raised_flag:')} Контакты",
                callback_data=constants.CONTACTS,
                url='https://sobytie.center/contacts/'
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':chart_increasing:')} Уставные доументы",
                callback_data=constants.LEGAL_DOCUMENTS,
                url='https://sobytie.center/documents/'
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':card_file_box:')} Отчеты о деятельности",
                callback_data=constants.REPORTS,
                url='https://sobytie.center/reports/'
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':hatching_chick:')} Проекты",
                callback_data=constants.PROJECTS,
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':woman_and_man_holding_hands:')} Люди",
                callback_data=constants.PEOPLE,
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу",
                callback_data=constants.RETURN_TO_MAIN,
            )
        ],
    ]


# КНОПКИ ПОДМЕНЮ "ПРОЕКТЫ"
PROJECTS_MENU_BUTTONS = [
    [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':performing_arts:')} Инклюзивный театр-студия 'Событие'",
                callback_data=constants.INCLUSIVE_THEATRE,
                
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':artist:')} Инклюзивная мастерская",
                callback_data=constants.INCLUSIVE_WORKSHOP,
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':cityscape:')} Москва - Партала. Онлайн.",
                callback_data=constants.MOSCOW_ONLINE,
                url='https://sobytie.center/project/moskva-partala-onlajn/',
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу",
                callback_data=constants.RETURN_TO_ABOUT_US,
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

# кнопки для подменю заказать сувениры
SUPPORT_ORDER_BUTTONS = [
        [
            InlineKeyboardButton(
                text="Благотворительная	ярмарка",
                callback_data=constants.CHARITY_MARKET,
                url="https://vk.com/market-190536221"
                
            )
        ],
        [
            InlineKeyboardButton(
                text="Корпоративные подарки",
                callback_data=constants.ORDER_PRESENTS
            )
        ],
        [
            InlineKeyboardButton(
                text="Вернуться на предыдущую страницу",
                callback_data=constants.RETURN_TO_PREVIOUS
            )
        ],
    ]

# кнопки для меню интерактив
INTERACTIVE_BUTTONS = [
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':game_die:')}Викторины",
                callback_data=constants.QUIZZES
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':white_question_mark:')}Вопрос-ответ",
                callback_data=constants.ASK_QUESTIONS,
                url="https://vk.com/im?sel=-190536221"
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':books:')}Случайная цитата",
                callback_data=constants.RANDOM_QUOTE
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{emoji.emojize(':reverse_button:')}Вернуться",
                callback_data=constants.RETURN_TO_PREVIOUS,
            )
        ]
    ]
