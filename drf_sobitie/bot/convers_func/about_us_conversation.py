from dataclasses import dataclass

from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from drf_sobitie.bot.constants import ABOUT_US_STATE, PROJECTS_STATE
from drf_sobitie.bot.keyboards.about_us import (
    ABOUT_US_MENU_BUTTONS,
    DOCUMENTS_MENU_BUTTONS,
    EMAIL_INFO_BUTTON,
    INCLUSIVE_WORKSHOP_BUTTON,
    MINISTRY_REPORTS_BUTTONS,
    MOSCOW_ONLINE_BUTTONS,
    PROJECTS_MENU_BUTTONS,
    REPORTS_MENU_BUTTONS,
    RETURN_BACK_BUTTON,
    THEATRE_SCHOOL_BUTTON,
    INCLUSIVE_THEATER_BUTTONS,
)


@dataclass
class ProjectInfoMessage:
    """Содержание сообщения о проекте."""

    text: str
    image_url: str
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(RETURN_BACK_BUTTON)


async def show_about_us(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'О нас'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(ABOUT_US_MENU_BUTTONS)
    message_text = (
        "«Событие» — это творческое содружество.\n\n"
        "Мы верим, что каждый человек, по своей натуре, творец и имеет право делиться творчеством с другими. "
        "Ведь искусство — это способ взаимодействия с собой и миром.\n\n"
        "Мы посвящаем свою работу социокультурной реабилитации и социальной интеграции людей с особыми возможностями, "
        "содействуем раскрытию их творческого потенциала, а также повышению социального и культурного уровня. "
        "А ещё мы развиваем инклюзивное волонтёрство.\n\n"
        "Выберите раздел меню, чтобы узнать больше.\n"
    )
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
        "Полное название: Автономная некоммерческая организация "
        "«Центр социокультурных практик «Событие»\n"
        "Сокращённое название: АНО «Событие»\n\n"
        "ИНН: 7727301229\n"
        "КПП: 772701001\n"
        "ОГРН: 1167700068051\n"
        "Расчётный счёт: 40703810002690000027\n"
        "Банк: АО «АЛЬФА-БАНК»\n"
        "БИК банка: 044525593\n"
        "Корреспондентский счёт: 30101810200000000593\n"
        "Директор: Елена Викторовна Киселева\n\n"

        "https://sobytie.center/documents/"
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


async def show_inclusive_workshop(update: Update, _: CallbackContext):
    """Нажатие кнопки 'Инклюзивная мастерская'."""
    message = ProjectInfoMessage(
        text=(
            "В мастерской актёры Инклюзивного театра-студии «Событие» создают костюмы, реквизит"
            "и декорации для спектаклей, а также различные сувениры и аксессуары для благотворительных ярмарок.\n\n"
            "Ребята не только сами учатся различным видам рукоделия, но и проводят очные и дистанционные мастер-классы."
        ),
        image_url="https://sobytie.center/wp-content/uploads/2022/07/Masterskaya-svechi.jpg",
        keyboard=InlineKeyboardMarkup(INCLUSIVE_WORKSHOP_BUTTON),
    )
    await _send_project_info(update=update, message=message)


async def show_theatre_school(update: Update, _: CallbackContext):
    """Нажатие кнопки 'Театральная студия i-Школы'."""
    message = ProjectInfoMessage(
        text=(
            "Актёры Инклюзивного театра-студии «Событие» принимают активное участие в жизни Театральной студии i-Школы:\n"
            "ассистируют на занятиях, проводят разминки и тренинги, участвуют в совместных творческих проектах,\n"
            "помогают изготавливать костюмы и реквизит для спектаклей, а также сопровождают школьников во время показов.\n"
        ),
        image_url="https://sobytie.center/project/inklyuzivnyj-teatr-studiya-sobytie/",
        keyboard=InlineKeyboardMarkup(THEATRE_SCHOOL_BUTTON),
    )
    await _send_project_info(update=update, message=message)


async def show_moscow_partala_online(update: Update, _: CallbackContext):
    """Нажатие кнопки 'Москва-Партала.Онлайн'."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(MOSCOW_ONLINE_BUTTONS)
    message_text = (
        "Мы сотрудничаем с Партальским домом-интернатом для престарелых "
        "и инвалидов и регулярно организуем совместные дистанционные "
        "концерты, мастер-классы, онлайн-прогулки и другие мероприятия. "
        "Помимо этого, мы совместно участвуем в благотворительных акциях "
        "и развиваем инклюзивное волонтёрство."
    )
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard,
    )

async def show_inclusive_theater(update: Update, _: CallbackContext):
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(INCLUSIVE_THEATER_BUTTONS)
    message_text = (
        "Актёры Инклюзивного театра-студии «Событие» — молодые люди с инвалидностью и их условно здоровые сверстники. "
        "Театр для наших актёров — способ взаимодействия с собой и миром вокруг, "
        "а также возможность созидать и делиться плодами сотворчества.")
    await query.edit_message_text(
        text=message_text,
        reply_markup=keyboard
    )


async def _send_project_info(update: Update, message: ProjectInfoMessage):
    """Отправка сообщения с информацией о проекте."""
    query = update.callback_query
    await query.answer()
    message.text += '<a href="%s">&#8205;</a>' % message.image_url
    await query.edit_message_text(
        text=message.text,
        parse_mode="HTML",
        reply_markup=message.keyboard,
    )


async def show_email_info(update: Update, _: CallbackContext):
    """Нажатие на кнопку 'Электронная почта"'."""
    query = update.callback_query
    keyboard = InlineKeyboardMarkup(EMAIL_INFO_BUTTON)
    message_text = (
        "Вы можете написать нам на нашу электронную почту: \n"
        "sobytie.center@yandex.ru"
    )
    await query.edit_message_text(text=message_text, reply_markup=keyboard)
