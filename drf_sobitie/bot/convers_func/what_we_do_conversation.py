from telegram import InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext

from bot.keyboards.main import START_MENU_BUTTONS


async def show_info_what_we_do(update: Update, _: CallbackContext):
    """Обработчик кнопки 'Чем вы занимаетесь?'."""
    query = update.callback_query
    await query.answer()
    message = (
        "«Событие» — это творческое содружество.\n"
        "Мы верим, что каждый человек, по своей натуре, творец и имеет право делиться творчеством с другими. Ведь искусство — это способ взаимодействия с собой и миром.\n"
        "Мы посвящаем свою работу социокультурной реабилитации и социальной интеграции людей с особыми возможностями, содействуем раскрытию их творческого потенциала, а также повышению социального и культурного уровня. А ещё мы развиваем инклюзивное волонтёрство.\n"
        "Выберите раздел меню, чтобы узнать больше.\n"
    )
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)
    await query.edit_message_text(text=message, reply_markup=keyboard)
