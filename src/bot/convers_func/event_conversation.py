from telegram import InlineKeyboardMarkup

from bot.keyboards.event import EVENTS_BUTTONS, CHOOSE_EVENT


async def get_events(update, _) -> str:

    keyboard = InlineKeyboardMarkup(EVENTS_BUTTONS)
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="Меню мероприятий", reply_markup=keyboard
    )
    return CHOOSE_EVENT


async def get_master_classes(update, _):
    query = update.callback_query
    await query.message.reply_text("Ваши мастер классы: парам")
    return


async def get_perfomances(update, _):
    query = update.callback_query
    await query.message.reply_text("Ваши спектакли")
    return


async def get_about_event(update, _):
    query = update.callback_query
    await query.message.reply_text("Ваши мероприятия")
    return
