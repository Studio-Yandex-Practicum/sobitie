from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update


BUTTONS = {
    1: 'Контакты',
    2: 'Уставные доументы',
    3: 'Отчеты о деятельности',
    4: 'Проекты',
}

CALLBACK = {
    1: 'Contacts',
    2: 'Documents',
    3: 'Reports',
    4: 'Projects',
}


async def about_us(update: Update, context):
    """Меню 'О нас'"""
    query = update.callback_query
    await query.answer()
    buttons = [
        [
            InlineKeyboardButton(
                text=BUTTONS[1],
                callback_data=CALLBACK[1],
                url='http://sobytie.team/#about'
            )
        ],
        [
            InlineKeyboardButton(
                text=BUTTONS[2],
                callback_data=CALLBACK[2],
            )
        ],
        [
            InlineKeyboardButton(
                text=BUTTONS[3],
                callback_data=CALLBACK[3],
            )
        ],
        [
            InlineKeyboardButton(
                text=BUTTONS[4],
                callback_data=CALLBACK[4],
            )
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await query.edit_message_text(
        text='О нас',
        reply_markup=keyboard,
    )
    
    return 'ABOUT_US'


async def projects(update: Update, context):
    '''Меню проектов'''
    query = update.callback_query
    await query.answer()
    buttons = [
        [
            InlineKeyboardButton(
                text='Project 1',
                callback_data='Project_1',
                
            )
        ],
        [
            InlineKeyboardButton(
                text='Project 2',
                callback_data='Project_2',
            )
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await query.edit_message_text(
        text='Наши проекты',
        reply_markup=keyboard,
    )

    return 'PROJECTS'
