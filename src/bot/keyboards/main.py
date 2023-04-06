import emoji
from telegram import InlineKeyboardButton

ABOUT_US = "ABOUT_US"
END = "END"
EVENTS = "EVENTS"
GIVE_SUPPORT = "GIVE_SUPPORT"
INTERACTIVE_GAME = "INTERACTIVE_GAME"
QUIZZES = "QUIZZES"
MAIN_TEXT = """Привет! Познакомимся?

«Событие» — творческое содружество.

Мы верим:
каждый человек — творец,
каждый уникален и выразителен,
каждый имеет право делиться творчеством с другими.

Мы знаем:
искусство — это способ взаимодействия с собой и миром. Мы посвящаем свою деятельность социокультурной реабилитации и \
социальной интеграции людей с особыми возможностями, содействуем раскрытию их творческого потенциала, повышению \
социального и культурного уровня. А ещё мы развиваем инклюзивное волонтёрство.

Выберите раздел меню, чтобы узнать больше.
"""
RETURN_TO_START = "RETURN_TO_START"
RETURN_TO_START_BUTTON_TEXT = (
    f"{emoji.emojize(':BACK_arrow:')} Вернуться в главное меню"
)
SHORT_RETURN_TO_START_BUTTON_TEXT = f"{emoji.emojize(':house:')} В главное меню"
RETURN_BACK_BUTTON_TEXT = (
    f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу"
)
SHORT_RETURN_BACK_BUTTON_TEXT = f"{emoji.emojize(':BACK_arrow:')} Назад"

START_MENU_BUTTONS = [
    [InlineKeyboardButton(text="О нас", callback_data=ABOUT_US)],
    [InlineKeyboardButton(text="События", callback_data=EVENTS)],
    [InlineKeyboardButton(text="Помочь", callback_data=GIVE_SUPPORT)],
    [InlineKeyboardButton(text="Интерактив", callback_data=INTERACTIVE_GAME)],
]


def create_return_to_start_button(
    text: str = RETURN_TO_START_BUTTON_TEXT,
) -> InlineKeyboardButton:
    """Создаёт объект кнопки для возвращения в стартовое меню."""
    return InlineKeyboardButton(text=text, callback_data=RETURN_TO_START)
