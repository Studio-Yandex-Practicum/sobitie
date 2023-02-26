from telegram import InlineKeyboardButton
from src.core import constants

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
