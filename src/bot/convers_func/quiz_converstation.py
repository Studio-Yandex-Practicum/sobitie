import urllib
from http import HTTPStatus

import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Poll, Update
from telegram.ext import CallbackContext

from bot.keyboards.main import QUIZZES, create_return_to_start_button
from bot.keyboards.quiz import FINISH_QUIZ_MENU_BUTTON, QUESTIONS_MENU_BUTTON, START_QUESTIONS
from core.settings import QUIZZES_URL


def get_quizzes():
    """Получить список викторин."""
    response = requests.get(QUIZZES_URL)
    if response.status_code != HTTPStatus.OK.value:
        return None
    if len(response.json()) < 1:
        return None
    return response.json()


def get_quizzes_inline_button():
    """Сформировать меню на основании списка викторин."""
    quizzes = get_quizzes()
    if quizzes is None:
        return FINISH_QUIZ_MENU_BUTTON
    quizzes_menu = [
        [InlineKeyboardButton(text=quiz["name"], callback_data=START_QUESTIONS + f"#{quiz['id']}")]
        for quiz in get_quizzes()
    ]
    quizzes_menu.append(
        [create_return_to_start_button()]
    )
    return quizzes_menu


def get_current_quiz_id(update: Update, context: CallbackContext):
    """Получить текущий ID викторины."""
    if "current_quiz_id" not in context.user_data:
        context.user_data["current_quiz_id"] = int(update.callback_query.data.split("#")[1])
    return context.user_data["current_quiz_id"]


async def send_start_quizzes_menu(update: Update, context: CallbackContext):
    """Отправить меню выбора викторины."""
    query = update.callback_query
    await query.answer()
    quizzes_menu_buttons = get_quizzes_inline_button()
    msg_text = "Выберите викторину"
    if quizzes_menu_buttons == FINISH_QUIZ_MENU_BUTTON:
        msg_text = "К сожалению пока нет ни одной викторины."
    markup = InlineKeyboardMarkup(quizzes_menu_buttons)
    await query.edit_message_text(text=msg_text, reply_markup=markup)
    return QUIZZES


def get_last_question_id(context: CallbackContext):
    """Получить ID последнего вопроса викторины."""
    if "last_question_id" not in context.user_data:
        return None
    return context.user_data["last_question_id"]


def get_image(image_url):
    request = urllib.request.Request(image_url)
    response = urllib.request.urlopen(request)
    if response.status != HTTPStatus.OK.value:
        return None
    return response.read()


def get_next_question(update: Update, context: CallbackContext):
    """Получить следующий вопрос викторины."""
    # Раскоментировать для get-запроса к DRF
    current_quiz_id = get_current_quiz_id(update=update, context=context)
    last_question_id = get_last_question_id(context=context)
    if last_question_id is None:
        clear_context(context)
    questions_url = f"{QUIZZES}/{current_quiz_id}/questions/"
    params = {"last_question_id": last_question_id}
    response = requests.get(questions_url, params=params)
    if response.status_code != HTTPStatus.OK.value:
        return None, None
    question = response.json()
    image = None
    if len(question) < 1:
        return None, None
    if "image" in question:
        image = get_image(question["image"])
        del question["image"]
    context.user_data["last_question_id"] = question["id"]
    del question["id"]
    return question, image


def correct_answer_count(update: Update, context: CallbackContext):
    """Обновление счетчика корректных ответов."""
    poll_data = update.callback_query.message.poll
    if poll_data.options[poll_data.correct_option_id]['voter_count'] > 0:
        if "correct_answer_counter" in context.user_data:
            context.user_data["correct_answer_counter"] += 1
        else:
            context.user_data["correct_answer_counter"] = 1


def increase_questions_count(context: CallbackContext):
    """Увеличение счетчика вопросов."""
    if "questions_counter" in context.user_data:
        context.user_data["questions_counter"] += 1
    else:
        context.user_data["questions_counter"] = 1


def scoring(context: CallbackContext):
    """Подсчет итогов прохождения."""
    questions_count = 0
    correct_answer_count = 0
    if "questions_counter" in context.user_data:
        questions_count = context.user_data["questions_counter"]
    if "correct_answer_counter" in context.user_data:
        correct_answer_count = context.user_data["correct_answer_counter"]
        # перевести в процент от общего кол-ва
        correct_answer_count = correct_answer_count * 100 / questions_count
    return correct_answer_count, questions_count


def get_message_for_result(update: Update, context: CallbackContext):
    """Получить текст сообщения из DRF по результату прохождения викторины."""
    correct_answer_count, questions_count = scoring(context)
    current_quiz_id = get_current_quiz_id(update, context)
    message_url = f'{QUIZZES_URL}/{current_quiz_id}/results/'
    params = {
        "correct_answer_count": correct_answer_count,
        "questions_cnt": questions_count,
    }
    response = requests.get(message_url, params=params)
    if response.status_code != HTTPStatus.OK.value:
        return None
    data = response.json()
    if len(data) < 1:
        return None
    if "image" in data:
        image = get_image(data["image"])
        if image is None:
            del data["image"]
        data["image"] = image
        return data
    return data


def clear_context(context: CallbackContext):
    if "questions_counter" in context.user_data:
        del context.user_data["questions_counter"]
    if "correct_answer_counter" in context.user_data:
        del context.user_data["correct_answer_counter"]
    if "current_quiz_id" not in context.user_data:
        del context.user_data["current_quiz_id"]
    if "last_question_id" in context.user_data:
        context.user_data["last_question_id"]


async def send_quiz_result(update: Update, context: CallbackContext):
    """Отправка результатов викторины."""
    markup = InlineKeyboardMarkup(FINISH_QUIZ_MENU_BUTTON)
    if "last_question_id" not in context.user_data:
        # если нет ID последнего вопроса, значит вопросов по викторине нет
        await update.effective_message.reply_text(
            text="К сожалению в данной викторине еще нет вопросов.",
            reply_markup=markup
        )
        return

    # отобразить результат,
    message_result = get_message_for_result(update, context)
    if message_result is None:
        correct_answer_count, questions_count = scoring(context)
        await update.effective_message.reply_text(
                text=f"Ваш результат: {correct_answer_count}%",
                reply_markup=markup
            )

    if "image" in message_result:
        await update.effective_message.reply_photo(
            photo=message_result["image"])

    await update.effective_message.reply_text(
            text=message_result["result_text"],
            reply_markup=markup
        )
    clear_context(context)
    return QUIZZES


async def send_quiz_question(update: Update, context: CallbackContext):
    """Отправка следующего вопроса викторины."""

    if update.callback_query.message.poll:
        # если прошлый пост был вопросом викторины, проверяем ответ
        correct_answer_count(update, context)

    question_data, image = get_next_question(update=update, context=context)

    if question_data is None:
        # если следующий вопрос не получен значит викторина завершена
        await send_quiz_result(update, context)
        return

    # увеличиваем счетчик вопросов
    increase_questions_count(context)

    # отправляем следующий вопрос викторины
    if image is not None:
        await update.effective_message.reply_photo(photo=image)

    markup = InlineKeyboardMarkup(QUESTIONS_MENU_BUTTON)
    await update.effective_message.reply_poll(
        type=Poll.QUIZ, reply_markup=markup, **question_data
    )
