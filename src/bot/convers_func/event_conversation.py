from telegram import InlineKeyboardMarkup

from bot.keyboards.event import BUTTON_BACK, CHOOSE_EVENT, EVENTS_BUTTONS


async def get_events(update, _) -> str:
    keyboard = InlineKeyboardMarkup(EVENTS_BUTTONS)
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="Меню мероприятий", reply_markup=keyboard
    )
    return CHOOSE_EVENT


async def get_master_classes(update, _):
    keyboard = InlineKeyboardMarkup(BUTTON_BACK)
    query = update.callback_query
    await query.edit_message_text(
        text="Ваши мастер классы: парам", reply_markup=keyboard,
    )


async def get_perfomances(update, _):
    keyboard = InlineKeyboardMarkup(BUTTON_BACK)
    query = update.callback_query
    await query.message.reply_text("Ваши спектакли")
    return


async def get_about_event(update, _):
    query = update.callback_query
    await query.edit_message_text(
        "Ваши спектакли", reply_markup=keyboard,
    )
