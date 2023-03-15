from telegram import InlineKeyboardMarkup, Update

from bot.keyboards.about_us import CONTACTS_BUTTONS


async def show_contacts(update: Update, _):
    """Нажатие на кнопку контакты.
    Открывается подменю с 4 кнопками."""
    query = update.callback_query
    await query.answer()
    keyboard = InlineKeyboardMarkup(CONTACTS_BUTTONS)
    await query.edit_message_text(
        text="Наш центр https://sobytie.center/\n"
        "Хотите узнать больше о нашей работе, обсудить "
        "сотрудничество, стать волонтёром? Просто "
        "хотите что-то спросить? Свяжитесь с нами любым "
        "удобным способом!",
        reply_markup=keyboard,
    )
