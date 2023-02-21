import emoji

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, Update

# кнопки стартового меню
START_MENU_BUTTONS = [
        [
            InlineKeyboardButton(
                text='О нас',
                callback_data='about_us',
            )
        ],
        [
            InlineKeyboardButton(
                text='Мероприятия',
                callback_data='events',
            )
        ],
        [
            InlineKeyboardButton(
                text='Помочь',
                callback_data='give_support',
            )
        ],
        [
            InlineKeyboardButton(
                text='Интерактив',
                callback_data='interactive_game',
            )
        ],
    ]


# НАСТРОЙКИ И КНОПОКИ МЕНЮ "ПОМОЧЬ"

# настройки
SUPPORT_BUTTONS = {
    1: f"{emoji.emojize(':credit_card:')} Пожертвования",
    2: f"{emoji.emojize(':performing_arts:')} Прийти на спектакль",
    3: f"{emoji.emojize(':handshake:')} Партнерство",
    4: f"{emoji.emojize(':heart_decoration:')} Заказать суверниры",
    5: f"{emoji.emojize(':dollar_banknote:')} Стать спонсором",
    6: f"{emoji.emojize(':flexed_biceps:')} Стать волонтером",
    7: f"{emoji.emojize(':mobile_phone_with_arrow:')} Стать активным подписчиком",
    8: f"{emoji.emojize(':reverse_button:')} Вернуться на предыдущую страницу"
}

SUPPORT_CALLBACKS = {
    1: 'Donations',
    2: 'Attend_event',
    3: 'Partnership',
    4: 'Order_souvenirs',
    5: 'Become_sponsor',
    6: 'Become_volunteer',
    7: 'Follow_us_in_social_networks',
    8: 'Return_to_previous_page'
}

# кнопки
SUPPORT_MENU_BUTTONS = [
        [
            InlineKeyboardButton(
                text=SUPPORT_BUTTONS[1],
                callback_data=SUPPORT_CALLBACKS[1]
            )
        ],
        [
            InlineKeyboardButton(
                text=SUPPORT_BUTTONS[2],
                callback_data=SUPPORT_CALLBACKS[2]
            )
        ],
        [
            InlineKeyboardButton(
                text=SUPPORT_BUTTONS[3],
                callback_data=SUPPORT_CALLBACKS[3]
            )
        ],
        [
            InlineKeyboardButton(
                text=SUPPORT_BUTTONS[4],
                callback_data=SUPPORT_CALLBACKS[4]
            )
        ],
        [
            InlineKeyboardButton(
                text=SUPPORT_BUTTONS[5],
                callback_data=SUPPORT_CALLBACKS[5]
            )
        ],
        [
            InlineKeyboardButton(
                text=SUPPORT_BUTTONS[6],
                callback_data=SUPPORT_CALLBACKS[6]
            )
        ],
        [
            InlineKeyboardButton(
                text=SUPPORT_BUTTONS[7],
                callback_data=SUPPORT_CALLBACKS[7]
            )
        ],
        [
            InlineKeyboardButton(
                text=SUPPORT_BUTTONS[8],
                callback_data=SUPPORT_CALLBACKS[8]
            )
        ],
    ]


# НАСТРОЙКИ И КНОПОКИ МЕНЮ "О НАС"

# настройки
ABOUT_US_BUTTONS = {
    1: f"{emoji.emojize(':open_mailbox_with_raised_flag:')} Контакты",
    2: f"{emoji.emojize(':chart_increasing:')} Уставные доументы",
    3: f"{emoji.emojize(':card_file_box:')} Отчеты о деятельности",
    4: f"{emoji.emojize(':hatching_chick:')} Проекты",
    5: f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу",
}

ABOUT_US_CALLBACKS = {
    1: 'Contacts',
    2: 'Documents',
    3: 'Reports',
    4: 'Projects',
    5: 'Return_to_previous_page',
}

# кнопки
ABOUT_US_MENU_BUTTONS = [
        [
            InlineKeyboardButton(
                text=ABOUT_US_BUTTONS[1],
                callback_data=ABOUT_US_CALLBACKS[1],
                url='http://sobytie.team/#about'
            )
        ],
        [
            InlineKeyboardButton(
                text=ABOUT_US_BUTTONS[2],
                callback_data=ABOUT_US_CALLBACKS[2],
            )
        ],
        [
            InlineKeyboardButton(
                text=ABOUT_US_BUTTONS[3],
                callback_data=ABOUT_US_CALLBACKS[3],
            )
        ],
        [
            InlineKeyboardButton(
                text=ABOUT_US_BUTTONS[4],
                callback_data=ABOUT_US_CALLBACKS[4],
            )
        ],
        [
            InlineKeyboardButton(
                text=ABOUT_US_BUTTONS[5],
                callback_data=ABOUT_US_CALLBACKS[5],
            )
        ],
    ]

# НАСТРОЙКИ И КНОПОКИ МЕНЮ "ПРОЕКТЫ"

# настройки
PROJECTS_BUTTONS = {
    1: f"{emoji.emojize(':keycap_1:')} Проект 1",
    2: f"{emoji.emojize(':keycap_2:')} Проект 2",
    3: f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу",
}

PROJECTS_CALLBACKS = {
    1: 'Project 1',
    2: 'Project 2',
    3: 'Return_to_previous_page',
}

#кнопки

PROJECTS_MENU_BUTTONS = [
        [
            InlineKeyboardButton(
                text=PROJECTS_BUTTONS[1],
                callback_data=PROJECTS_CALLBACKS[1],
                
            )
        ],
        [
            InlineKeyboardButton(
                text=PROJECTS_BUTTONS[2],
                callback_data=PROJECTS_CALLBACKS[2],
            )
        ],
        [
            InlineKeyboardButton(
                text=PROJECTS_BUTTONS[3],
                callback_data=PROJECTS_CALLBACKS[3],
            )
        ],
    ]


# кнопки для подписок на соцсети
SUPPORT_FOLLOW_BUTTONS = [
        [
            InlineKeyboardButton(
                text="ВКонтакте",
                callback_data="Vkontakte",
                url="https://vk.com/sobytie.center"
                
            )
        ],
        [
            InlineKeyboardButton(
                text="Telegram",
                callback_data="Telegram",
                url="https://t.me/sobytiecenter"
            )
        ],
        [
            InlineKeyboardButton(
                text="Вернуться на предыдущую страницу",
                callback_data="Return_to_previous_page"
            )
        ],
    ]
