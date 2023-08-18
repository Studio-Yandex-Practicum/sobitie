from dataclasses import dataclass

from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.keyboards.about_us import (
    ABOUT_US_MENU_BUTTONS,
    DOCUMENTS_MENU_BUTTONS,
    MINISTRY_REPORTS_BUTTONS,
    PROJECTS_MENU_BUTTONS,
    REPORTS_MENU_BUTTONS,
    RETURN_BACK_AND_TO_START_BUTTONS, INCLUSIVE_WORKSHOP_BUTTON, THEATRE_SCHOOL_BUTTON,
)
from core.states import ABOUT_US_STATE, PROJECTS_STATE


@dataclass
class ProjectInfoMessage:
    """Содержание сообщения о проекте."""

    text: str
    image_url: str


async def show_about_us(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'О нас'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(ABOUT_US_MENU_BUTTONS)
    message_text = "Узнайте о нас побольше. Выберите интересующее Вас:"
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )
    return ABOUT_US_STATE


async def show_documents(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Документы'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(DOCUMENTS_MENU_BUTTONS)
    message_text = (
        "Мы официально зарегистрированная некоммерческая организация.\n"
        "Полное название: Автономная некоммерческая организация «Центр социокультурных практик «Событие»\n"
        "Сокращённое название: АНО «Событие»\n"
        "ИНН: 7727301229\n"
        "ОГРН: 1167700068051\n"
    )
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )


async def show_reports(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Отчёты'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(REPORTS_MENU_BUTTONS)
    message_text = (
        "Наш принцип — открытость и прозрачность. Информация о нашей работе, "
        "проектах, полученных средствах и их использовании находится в открытом "
        "доступе. Исключением является информация об обращениях к нам за помощью.\n\n"
        "Ежегодно мы подаём финансовые отчёты в Министерство юстиции РФ, а также "
        "размещаем их у себя на сайте."
    )
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )


async def show_ministry_reports(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Отчёты на портале Минюста РФ'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(MINISTRY_REPORTS_BUTTONS)
    message_text = (
        "Перейдите на "
        "информационный портал Минюста РФ «О деятельности некоммерческих "
        "организаций» и введите в строку «ОГРН» номер: 1167700068051"
    )
    await query.edit_message_text(
        text=message_text, reply_markup=keyboard, parse_mode="HTML"
    )


async def show_projects(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Проекты'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(PROJECTS_MENU_BUTTONS)
    message_text = (
        "«Событие» было создано в 2016 году в Москве группой единомышленников из выпускников и педагогов Театральной студии i-Школы.\n"
        "Мы занимаемся социокультурной реабилитацией и социальной интеграцией людей с особыми возможностями, создаём условия для раскрытия творческого потенциала — не только для реабилитации участников проекта, но и для культурного обогащения общества.\n"
        "Познакомьтесь с нашими проектами.\n"
    )
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )
    return PROJECTS_STATE


async def show_inclusive_theatre(update: Update, _: CallbackContext):
    """Нажатие кнопки 'Инклюзивный театр'."""
    message = ProjectInfoMessage(
        text="""Театр для наших <a href="https://sobytie.center/project-tag/aktyory/">актёров</a> - способ \
взаимодействия с собой и миром вокруг, возможность созидать и делиться плодами сотворчества. В процессе работы \
решаются реабилитационные, воспитательные, образовательные и эстетические задачи.""",
        image_url="https://sobytie.center/wp-content/uploads/2021/09/09-12-2019.jpg",
    )
    await _send_project_info(update=update, message=message)


async def show_inclusive_workshop(update: Update, _: CallbackContext):
    """Нажатие кнопки 'Инклюзивная мастерская'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(INCLUSIVE_WORKSHOP_BUTTON)
    message = ProjectInfoMessage(
        text="""В инклюзивной мастерской актёры ИТС "Событие" создают как костюмы, реквизит и декорации для \
спектаклей, так и необычные вещи, сувениры, аксессуары для благотворительных ярмарок.
Ребята не только сами учатся какому-либо рукоделию, но и проводят очные и дистанционные мастер-классы.
""",
        image_url="https://sobytie.center/wp-content/uploads/2022/07/Masterskaya-svechi.jpg",
    )
    await query.edit_message_text(
        text=(message.text + '<a href="%s">&#8205;</a>' % message.image_url),
        parse_mode="HTML",
        reply_markup=keyboard,
    )


async def show_theatre_school(update: Update, _: CallbackContext):
    """Нажатие кнопки 'Театральная студия i-Школы'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(THEATRE_SCHOOL_BUTTON)
    message = ProjectInfoMessage(
        text="""Актёры ИТС "Событие" принимают активное участие в жизни Театральной студии i-Школы для учеников с \
особыми образовательными потребностями: ассистируют на занятиях, проводят разминки и тренинги, участвуют в совместных \
творческих проектах, помогают изготавливать костюмы и реквизит для школьных спектаклей, сопровождают школьников во \
время показов.""",
        image_url="https://sobytie.center/wp-content/uploads/2021/09/09-12-2019.jpg",
    )
    await query.edit_message_text(
        text=(message.text + '<a href="%s">&#8205;</a>' % message.image_url),
        parse_mode="HTML",
        reply_markup=keyboard,
    )


async def _send_project_info(update: Update, message: ProjectInfoMessage):
    """Отправка сообщения с информацией о проекте."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(RETURN_BACK_AND_TO_START_BUTTONS)
    message.text += '<a href="%s">&#8205;</a>' % message.image_url
    await query.edit_message_text(
        text=message.text,
        parse_mode="HTML",
        reply_markup=keyboard,
    )
