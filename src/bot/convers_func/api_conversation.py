import os
import urllib.request
from http import HTTPStatus
from typing import Dict

import emoji
import requests
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.error import TelegramError
from telegram.ext import CallbackContext

from bot.async_requests import async_delete_request, async_get_request, async_send_json_post_request
from bot.convers_func.event_conversation import (
    CLOSING_NOTIFICATION_TEXT,
    EVENT_MESSAGE_TEMPLATE,
    _check_api_response_status,
    _fill_in_message_template_with_event,
    _log_subscription_status_failure,
    _process_no_events,
    _send_closing_message,
    _send_event_messages,
    _send_message_or_handle_error,
    logger,
)
from bot.convers_func.quiz_converstation import get_current_quiz_id, get_last_question_id, scoring
from bot.keyboards.event import (
    EVENT_MENU,
    NOTIFICATION_BUTTONS,
    NOTIFICATION_SUBSCRIBE_CALLBACK,
    SUBSCRIBE_BUTTON_TEXT,
    _process_and_update_button_based_on_api_response,
)
from bot.keyboards.interactive import RETURN_TO_INTERACTIVE_MENU_BUTTON
from core.settings import (
    CHECK_FOR_SUBSCRIPTION_API_URL,
    EVENTS_URL,
    NOTIFICATIONS_API_URL,
    QUIZZES_URL,
    QUOTE_URL,
    STICKERPACK_URL,
)

ABC=34
class APIClient:
    def __init__(self, host: str = None):
        self._host = os.getenv("HOST", "http://localhost:8000")
        '''self._httpx_client = AsyncClient(base_url=base_url)  # Чтобы каждый раз не указывать хост в начале урла.'''

    async def show_upcoming_events(update: Update, _: CallbackContext):
        """Отправляет сообщения с ближайшими событиями."""
        closing_message = """Вы можете подписаться на уведомления об анонсах, чтобы первыми узнавать о наших \
    будущих мероприятиях. Также вы можете вернуться в главное меню и ознакомиться с другими разделами. Спасибо за интерес \
    к нашей организации."""
        query = update.callback_query
        await query.answer()
        event_response = await async_get_request(url=EVENTS_URL)
        events = event_response.json()
        if len(events) == 0:
            await _process_no_events(query=query, closing_message=closing_message)
            return
        await _send_event_messages(query=query, events=events, message_template=EVENT_MESSAGE_TEMPLATE)
        await _send_closing_message(query=query, closing_message=closing_message)


    async def get_quote(update: Update, _: CallbackContext):
        """Нажатие на кнопку 'Цитата недели'."""
        response = requests.get(QUOTE_URL).json()
        keyboard = InlineKeyboardMarkup([[RETURN_TO_INTERACTIVE_MENU_BUTTON]])
        query = update.callback_query
        if len(response) < 1:
            await query.message.reply_text(
                text=(
                    f"{emoji.emojize(':detective:')}"
                    f"В поисках подходящей цитаты"
                    f"{emoji.emojize(':detective:')}"
                ), reply_markup=keyboard
            )
            return

        quote = response[0].get("text")
        if "image" in response[0] and response[0].get("image") is not None:
            image = response[0].get("image")
            photo = urllib.request.urlopen(image).read()
            await query.delete_message()
            await query.message.reply_photo(
                caption=quote,
                photo=photo,
                reply_markup=keyboard
            )
            return
    
        await query.edit_message_text(text=quote, reply_markup=keyboard)
        return


    async def get_stickers(update: Update, _: CallbackContext):
        """Нажатие на кнопку 'Стикерпаки'."""
        response = requests.get(STICKERPACK_URL).json()
        keyboard = InlineKeyboardMarkup([[RETURN_TO_INTERACTIVE_MENU_BUTTON]])
        query = update.callback_query

        def absence_stikers(text, my_moji):
            return (
                f"{emoji.emojize(my_moji)}"
                f"{text}"
                f"{emoji.emojize(my_moji)}"
            )

        if len(response) < 1:
            await query.message.reply_text(
                text=absence_stikers(
                    "Стикеры пока не завезли, ждем на днях",
                    ':ship:'
                ), reply_markup=keyboard
            )
            return

        active_stickerpaks = []
        for index, i in enumerate(response):
            if i["is_active"]:
                active_stickerpaks.append(index)
        if active_stickerpaks:
            for i in active_stickerpaks:
                name = response[i].get("name")
                description = response[i].get("description")
                url_sticker = response[i].get("url_sticker")
                image = response[i].get("image")
                text = (
                    f"{name} \n\n{description}\n\n"
                )
                caption = (
                    f"{emoji.emojize(':backhand_index_pointing_up:')}"
                    f"-Забирай-{emoji.emojize(':backhand_index_pointing_up:')}"
                )
                sticker_keyboard = InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text=caption,
                            url=url_sticker,
                        )
                    ]]
                )
                query = update.callback_query
                if image:
                    photo = urllib.request.urlopen(image).read()
                    await query.message.reply_photo(photo=photo)
                await query.message.reply_text(reply_markup=sticker_keyboard, text=text)
            await query.message.reply_text(
                text=(
                    f"Выбирайте и добавляйте себе понравившиеся варианты стикерпаков - их создают ученики нашего центра. А мы будем создавать для вас новые!"
                    f"{emoji.emojize(':backhand_index_pointing_up:')}"
                ),
                reply_markup=keyboard
            )
            return
        await query.message.reply_text(
            text=absence_stikers("Редактируем, скоро релиз!!", ":fire:"),
            reply_markup=keyboard
        )
        return


    def get_quizzes():
        """Получить список викторин."""
        response = requests.get(QUIZZES_URL)
        if response.status_code != HTTPStatus.OK.value:
            return None
        if len(response.json()) < 1:
            return None
        return response.json()


    def get_next_question(update: Update, context: CallbackContext):
        """Получить следующий вопрос викторины."""
        current_quiz_id = get_current_quiz_id(update=update, context=context)
        questions_url = f"{QUIZZES_URL}{current_quiz_id}/quiz_questions/"
        last_question_id = get_last_question_id(context=context)
        params = {"last_question_id": last_question_id}
        response = requests.get(questions_url, params=params)
        if response.status_code != HTTPStatus.OK.value:
            return None, None
        questions = response.json()
        if len(questions) < 1:
            return None, None
        image = None
        question = questions[0]
        question_exist = question["question_text"]
        result_exist = question["result_exist"]
        if not question_exist or not result_exist:
            return None, None
        if question["image"]:
            image = question.get("image")
            image = urllib.request.urlopen(image).read()
        context.user_data["last_question_id"] = question["id"]
        del question["id"]
        del question["image"]
        return question, image


    def get_message_for_result(update: Update, context: CallbackContext):
        """Получить текст сообщения из DRF по результату прохождения викторины."""
        correct_answer_count, questions_count = scoring(context)
        current_quiz_id = get_current_quiz_id(update, context)
        message_url = f"{QUIZZES_URL}{current_quiz_id}/quiz_result/"
        params = {
            "correct_answer_count": correct_answer_count
        }
        response = requests.get(message_url, params=params)
        if response.status_code != HTTPStatus.OK.value:
            return None
        data = response.json()
        if len(data) < 1:
            return None
        data = data[0]
        image = None
        if data["image"]:
            image = data.get("image")
            image = urllib.request.urlopen(image).read()
        del data["image"]
        return data, image


    async def show_gratitude_and_subscribe_to_notifications(update: Update, _: CallbackContext):
        """Отправляет сообщение благодарности за подписку и включает уведомления пользователю на события."""
        query = update.callback_query
        await query.answer()
        message_text = """Спасибо за интерес к нашим событиям! Вы будете получать уведомления о новых мероприятиях."""
        user_id = query.from_user.id
        response = await async_send_json_post_request(url=NOTIFICATIONS_API_URL, data={"user_id": user_id})
        message_text = await _check_api_response_status(message_text=message_text, response=response, user_id=user_id)
        keyboard = InlineKeyboardMarkup(NOTIFICATION_BUTTONS)
        await query.edit_message_text(text=(message_text + CLOSING_NOTIFICATION_TEXT), reply_markup=keyboard)
        return EVENT_MENU


    async def unsubscribe_and_notify_user(update: Update, _: CallbackContext):
        """Отключение уведомлений пользователю на события и отправка сообщения с оповещением об этом."""
        query = update.callback_query
        await query.answer()
        message_text = """Вы успешно отписались от уведомлений о наших событиях. Мы будем скучать по вашему участию, \
    но вы всегда можете подписаться на уведомления в любое время снова."""
        user_id = query.from_user.id
        response = await async_delete_request(url=f"{NOTIFICATIONS_API_URL}{user_id}/")
        message_text = await _check_api_response_status(
            message_text=message_text, response=response, user_id=user_id, expected_status=HTTPStatus.NO_CONTENT
        )
        keyboard = InlineKeyboardMarkup(NOTIFICATION_BUTTONS)
        await query.edit_message_text(text=(message_text + CLOSING_NOTIFICATION_TEXT), reply_markup=keyboard)
        return EVENT_MENU


    async def notify_subscribers_about_new_event(event_data: Dict, bot: Bot) -> None:
        """Отправляет уведомления о новом событии всем подписчикам."""
        response = await async_get_request(url=NOTIFICATIONS_API_URL)
        subscribers = response.json()
        for user_data in subscribers:
            message = await _fill_in_message_template_with_event(
                event_data=event_data, message_template=EVENT_MESSAGE_TEMPLATE
            )
            await _send_message_or_handle_error(bot=bot, message_text=message, user_id=user_data["user_id"])


    async def _handle_bot_block_error(error: TelegramError, user_id: int) -> None:
        """Проверяет, что ошибка связана с блокировкой бота пользователем, обрабатывая этот случай."""
        if "Forbidden: bot was blocked by the user" in str(error):
            logger.info(f"Бот был заблокирован пользователем, пользователь {user_id} будет удалён из подписчиков.")
            response = await async_delete_request(url=f"{NOTIFICATIONS_API_URL}{user_id}/")
            if response.status_code != HTTPStatus.NO_CONTENT:
                await _log_subscription_status_failure(response=response, user_id=user_id)
        else:
            logger.error(f"При отправке уведомления пользователю {user_id} произошла ошибка:", exc_info=error)


    async def create_notification_button_based_on_subscription_status(
        user_id: int,
    ) -> InlineKeyboardButton:
        """В зависимости от наличия подписки создаёт кнопку: подписаться/отписаться."""
        button = InlineKeyboardButton(
            text=SUBSCRIBE_BUTTON_TEXT, callback_data=NOTIFICATION_SUBSCRIBE_CALLBACK
        )
        response = await async_get_request(
            url=f"{CHECK_FOR_SUBSCRIPTION_API_URL}{user_id}/"
        )
        button = await _process_and_update_button_based_on_api_response(
            button=button, response=response
        )
        return button
