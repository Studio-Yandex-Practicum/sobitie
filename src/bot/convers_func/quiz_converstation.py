
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Poll, Update
from telegram.ext import CallbackContext

from bot.convers_func.api_conversation import *
from bot.keyboards.main import QUIZZES, create_return_to_start_button
from bot.keyboards.quiz import FINISH_QUIZ_MENU_BUTTON, QUESTIONS_MENU_BUTTON, START_QUESTIONS


def get_quizzes_inline_button():
    """Сформировать меню на основании списка викторин."""
    quizzes = APIClient.get_quizzes()
    if quizzes is None:
        return FINISH_QUIZ_MENU_BUTTON
    quizzes_menu = [
        [InlineKeyboardButton(
            text=quiz["name"],
            callback_data=START_QUESTIONS + f"#{quiz['id']}")]
        for quiz in APIClient.get_quizzes()
    ]
    quizzes_menu.append([create_return_to_start_button()])
    return quizzes_menu


def get_current_quiz_id(update: Update, context: CallbackContext):
    """Получить текущий ID викторины."""
    if "current_quiz_id" not in context.user_data:
        context.user_data["current_quiz_id"] = int(
            update.callback_query.data.split("#")[1]
        )
    return context.user_data["current_quiz_id"]


async def send_start_quizzes_menu(update: Update, context: CallbackContext):
    """Отправить меню выбора викторины."""
    query = update.callback_query
    await query.answer()
    quizzes_menu_buttons = get_quizzes_inline_button()
    msg_text = "Выберите викторину"
    if quizzes_menu_buttons == FINISH_QUIZ_MENU_BUTTON:
        msg_text = "Викторины скоро появятся."
    markup = InlineKeyboardMarkup(quizzes_menu_buttons)
    await query.edit_message_text(text=msg_text, reply_markup=markup)
    clear_context(context)
    return QUIZZES


def get_last_question_id(context: CallbackContext):
    """Получить ID последнего вопроса викторины."""
    if "last_question_id" not in context.user_data:
        return None
    return context.user_data["last_question_id"]


def correct_answer_count(update: Update, context: CallbackContext):
    """Обновление счетчика корректных ответов."""
    poll_data = update.callback_query.message.poll
    if poll_data.options[poll_data.correct_option_id]["voter_count"] > 0:
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
    return correct_answer_count, questions_count


def clear_context(context: CallbackContext):
    if "questions_counter" in context.user_data:
        del context.user_data["questions_counter"]
    if "correct_answer_counter" in context.user_data:
        del context.user_data["correct_answer_counter"]
    if "current_quiz_id" in context.user_data:
        del context.user_data["current_quiz_id"]
    if "last_question_id" in context.user_data:
        del context.user_data["last_question_id"]


async def send_quiz_result(update: Update, context: CallbackContext):
    """Отправка результатов викторины."""
    markup = InlineKeyboardMarkup(FINISH_QUIZ_MENU_BUTTON)
    if "last_question_id" not in context.user_data:
        await update.effective_message.reply_text(
            text="К сожалению викторина пока не готова.",
            reply_markup=markup
        )
        clear_context(context)
        return QUIZZES

    # отобразить результат,
    message_result, image = APIClient.get_message_for_result(update, context)
    correct_answer_count, questions_count = scoring(context)
    per_correct_answers = 0
    if correct_answer_count != 0:
        per_correct_answers = round(
            (correct_answer_count * 100 / questions_count), 2
        )
    if message_result is None:
        await update.effective_message.reply_text(
            text=f"Ваш результат: {per_correct_answers}%",
            reply_markup=markup
        )

    if image is not None:
        await update.effective_message.reply_photo(photo=image)

    await update.effective_message.reply_text(
        text=(f"{message_result['text']}\n"
              f"Вопросов в викторине: {questions_count}\n"
              f"Правильных ответов: {correct_answer_count}\n"
              f"Результативность: {per_correct_answers}%\n"),
        reply_markup=markup
    )
    clear_context(context)
    return QUIZZES


async def send_quiz_question(update: Update, context: CallbackContext):
    """Отправка следующего вопроса викторины."""

    if update.callback_query.message.poll:
        # если прошлый пост был вопросом викторины, проверяем ответ
        correct_answer_count(update, context)
    question_data, image = APIClient.get_next_question(
        update=update, context=context
    )
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

    correct_answer = None
    for index, i in enumerate(question_data["answers"]):
        if i["is_right"]:
            correct_answer = index

    await update.effective_message.reply_poll(
        question=question_data["question_text"],
        options=[str(x["answer_text"]) for x in question_data["answers"]],
        correct_option_id=correct_answer,
        type=Poll.QUIZ,
        reply_markup=markup
    )
