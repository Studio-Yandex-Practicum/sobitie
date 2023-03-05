from telegram import InlineKeyboardMarkup, Update

from bot.keyboards.about_us import (ABOUT_US_MENU_BUTTONS,
                                    DOCUMENTS_MENU_BUTTONS,
                                    MINISTRY_REPORTS_BUTTONS,
                                    PROJECTS_MENU_BUTTONS,
                                    REPORTS_MENU_BUTTONS,
                                    BUTTON_BACK)
from bot.keyboards.main import START_MENU_BUTTONS
from core.states import ABOUT_US_STATE, PROJECTS_STATE, START_STATE


async def show_about_us(update: Update, _):
    """Нажатие на кнопку 'О нас'.
    Открывает подменю с четырьмя кнопками
    разной информации."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(ABOUT_US_MENU_BUTTONS)
    await query.edit_message_text(
        text='Узнайте о нас побольше. Выберите интересуещее Вас:',
        reply_markup=keyboard,
    )
    return ABOUT_US_STATE


async def show_documents(update: Update, _):
    '''Нажатие на кнопку 'Документы'.'''
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(DOCUMENTS_MENU_BUTTONS)
    await query.edit_message_text(
        text='Мы официально зарегистрированная некомерческая организация.\n'
             'Полное название: Автономная некомерческая организация '
             '"Центр социокультурных практик Событие"\n'
             'Сокращенное название: АНО "Событие"\n'
             'ИНН: 7727301229\n'
             'ОГРН: 116700068051',
        reply_markup=keyboard,
    )


async def show_reports(update: Update, _):
    '''Нажатие на кнопку 'Отчёты'.'''
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(REPORTS_MENU_BUTTONS)
    await query.edit_message_text(
        text='Открытость и прозрачность деятельности - наш принцип.\n'
             'Мы защищаем тайну обращений к нам за помощью. Но информация о нашей '
             'деятельности, проектах, полученных средствах и их исполозовании открыта.\n'
             'Мы ежегодно подаём финансовые отчёты в Министерство юстиции РФ и '
             'размещаем годовые отчёты на сайте.',
        reply_markup=keyboard,
    )


async def show_ministry_reports(update: Update, _):
    '''Нажатие на кнопку 'Отчёты на портале Минюста РФ'.'''
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(MINISTRY_REPORTS_BUTTONS)
    await query.edit_message_text(
        text='Хотите посмотреть отчёты на  информационном портале Минюста РФ?'
             '"О деятельности некомерческих организаций"?\n'
             'Введите в поисковую строку ОГРН: 1167700068051',
        reply_markup=keyboard,
    )


async def show_projects(update: Update, _):
    '''Нажатие на кнопку 'Проекты'.'''
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(PROJECTS_MENU_BUTTONS)
    await query.edit_message_text(
        text='АНО "Событие" создана в 2016 году в Москве группой единомышленников. '
             'Инициаторы - выпускники и педагоги Театральной студии i-Школы, детского '
             'творческого объединения, основанного в 2009 году в очно-дистанционной '
             'школе для детей с особыми образовательными потребностями. '
             'Одной из важных задач нашей работы являетсяразвитие социальной '
             'ответсвенности её участников.',
        reply_markup=keyboard,
    )
    return PROJECTS_STATE


async def show_inclusive_theatre(update: Update, _):
    '''Нажатие кнопки 'Инклюзивный театр'.'''
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(BUTTON_BACK)

    await query.edit_message_text(
        text='[Т](https://sobytie.center/wp-content/uploads/2021/09/09-12-2019.jpg)'
             'еатр для наших [актёров ](https://sobytie.center/project-tag/aktyory/)'
             '- способ взаимодействия с собой и миром вокруг, '
             'возможность созидать и делиться плодами соотворчества. В процессе работы '
             'решаются реабилитационные, воспитательные, образовательные и '
             'эстетические задачи.',
        parse_mode='Markdown',
        reply_markup=keyboard,
    )


async def show_inclusive_workshop(update: Update, _):
    '''Нажатие кнопки 'Инклюзивная мастерская'.'''
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(BUTTON_BACK)
    await query.edit_message_text(
        text='[В ](https://sobytie.center/wp-content/uploads/2022/07/Masterskaya-svechi.jpg)'
             'инклюзивной мастерской актёры ИТС "Событие" создают как костюмы, '
             'реквезит и декорации для спектаклей, так и необычные вещи, сувениры, '
             'аксессуары для благотворительных ярмарок.\n'
             'Ребята не только сами учатся какому-либо рукоделию, но и проводят очные '
             'и дистанционные мастер-классы.',
        parse_mode='Markdown',
        reply_markup=keyboard,
    )


async def show_theatre_school(update: Update, _):
    '''Нажатие кнопки 'Театральная студия i-Школы'.'''
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(BUTTON_BACK)
    await query.edit_message_text(
        text='[А](https://sobytie.center/wp-content/uploads/2021/09/09-12-2019.jpg)'
             'ктёры ИТС "Событие" принимают активное участие в жизни Театральной '
             'студии i-Школы для учеников с особыми образовательными потребностями: '
             'ассистируют на занятиях, проводят разминки и тренинги, учавствуют в '
             'совместных творческих проектах, помогают изготавливать костюмы и '
             'реквезит для школьных спектаклей, сопровождают школьников во время показов.',
        parse_mode='Markdown',
        reply_markup=keyboard,
    )


async def go_back_to_start(update: Update, _):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await query.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return START_STATE
