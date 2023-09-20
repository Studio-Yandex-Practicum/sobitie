import emoji
from telegram import InlineKeyboardButton

ABOUT_US = "ABOUT_US"
END = "END"
EVENTS = "EVENTS"
GIVE_SUPPORT = "GIVE_SUPPORT"
INTERACTIVE_GAME = "INTERACTIVE_GAME"
QUIZZES = "QUIZZES"
WHAT_WE_DO = "WHAT_WE_DO"
MAIN_TEXT = """Привет! Я — бот автономной некоммерческой организации «Событие». 

Со мной вы можете больше узнать о нашей организации, 
команде, проектах и мероприятиях, а также способах поддержки.

Выберите раздел меню, чтобы узнать больше.
"""
RETURN_TO_START = "RETURN_TO_START"
RETURN_TO_START_BUTTON_TEXT = (
    f"{emoji.emojize(':BACK_arrow:')} Назад"
)
SHORT_RETURN_TO_START_BUTTON_TEXT = f"{emoji.emojize(':house:')} В главное меню"
RETURN_BACK_BUTTON_TEXT = (
    f"{emoji.emojize(':BACK_arrow:')} Вернуться на предыдущую страницу"
)
SHORT_RETURN_BACK_BUTTON_TEXT = f"{emoji.emojize(':BACK_arrow:')} Назад"

START_MENU_BUTTONS = [
    [InlineKeyboardButton(text="Чем вы занимаетесь?", callback_data=WHAT_WE_DO)],
    [InlineKeyboardButton(text="О нас", callback_data=ABOUT_US)],
    [InlineKeyboardButton(text="События", callback_data=EVENTS)],
    [InlineKeyboardButton(text="Как помочь", callback_data=GIVE_SUPPORT)],
    [InlineKeyboardButton(text="Интерактив", callback_data=INTERACTIVE_GAME)],
]


def create_return_to_start_button(
    text: str = RETURN_TO_START_BUTTON_TEXT,
) -> InlineKeyboardButton:
    """Создаёт объект кнопки для возвращения в стартовое меню."""
    return InlineKeyboardButton(text=text, callback_data=RETURN_TO_START)