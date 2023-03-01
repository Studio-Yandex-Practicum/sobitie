from telegram import InlineKeyboardMarkup


from bot.keyboards.main import START_MENU_BUTTONS
from core.states import START_STATE

async def start(update, context):
    """Главное меню, кнопка старт."""
    keyboard = InlineKeyboardMarkup(START_MENU_BUTTONS)

    await update.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return START_STATE


async def end(update, _):
    await update.message.reply_text('bye')
