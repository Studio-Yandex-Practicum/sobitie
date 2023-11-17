from telegram import InlineKeyboardMarkup, Update

from drf_sobitie.bot.keyboards.about_us import PEOPLE_BUTTONS


async def show_people(update: Update, _):
    """Нажатие на кнопку людей."""
    query = update.callback_query
    await query.answer()

    keyboards = InlineKeyboardMarkup(PEOPLE_BUTTONS)
    await query.edit_message_text(
        text=(
            "АНО «Событие» — это сообщество единомышленников. "
            "Наша организация была создана в 2016 году в Москве "
            "по инициативе педагогов и выпускников Театральной студии i-Школы, "
            "детского творческого объединения, основанного в 2009 году "
            "в очно-дистанционной школе для детей "
            "с особыми образовательными потребностями.\nДавайте познакомимся"
        ),
        reply_markup=keyboards,
    )
