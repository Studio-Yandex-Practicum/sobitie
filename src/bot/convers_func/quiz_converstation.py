from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Poll, Update
from telegram.ext import CallbackContext

from bot.keyboards.main import QUIZZES, create_return_to_start_button
from bot.keyboards.quiz import FINISH_QUIZ_MENU_BUTTON, QUESTIONS_MENU_BUTTON, START_QUESTIONS


def get_quizzes():
    """Получить список викторин."""
    return None  # TODO: заменить заглушку на запрос к DRF


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


def get_next_question(update: Update, context: CallbackContext):
    """Получить следующий вопрос викторины."""
    # Раскоментировать для get-запроса к DRF
    # current_quiz_id = get_current_quiz_id(update=update, context=context)
    # last_question_id = get_last_question_id(context=context)

    question = None  # TODO: заменить заглушку на запрос к DRF

    if question is None:
        return None
    context.user_data["last_question_id"] = question["id"]
    del question["id"]
    return question


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
    return questions_count, correct_answer_count


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
    # посчитать и отобразить результат,
    questions_cnt, answer_cnt = scoring(context)
    await update.effective_message.reply_text(
            text=f"Ваш результат: {answer_cnt} из {questions_cnt}",
            reply_markup=markup
        )
    clear_context(context)
    return QUIZZES


async def send_quiz_question(update: Update, context: CallbackContext):
    """Отправка следующего вопроса викторины."""

    if update.callback_query.message.poll:
        # если прошлый пост был вопросом викторины, проверяем ответ
        correct_answer_count(update, context)

    question_data = get_next_question(update=update, context=context)

    if question_data is None:
        # если следующий вопрос не получен значит викторина завершена
        await send_quiz_result(update, context)
        return

    # увеличиваем счетчик вопросов
    increase_questions_count(context)

    # отправляем следующий вопрос викторины
    markup = InlineKeyboardMarkup(QUESTIONS_MENU_BUTTON)
    await update.effective_message.reply_poll(
        type=Poll.QUIZ, reply_markup=markup, **question_data
    )
