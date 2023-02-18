from telegram import InlineKeyboardButton, InlineKeyboardMarkup


async def start(update, context):
    """Главное меню, кнопка старт."""
    buttons = [
        [
            InlineKeyboardButton(
                text='О нас',
                callback_data='TestCallback',
            )
        ],
        [
            InlineKeyboardButton(
                text='Мероприятия',
                callback_data='TestCallbackdata2',
            )
        ],
        [
            InlineKeyboardButton(
                text='Помочь',
                callback_data='TestCallbackdata2',
            )
        ],
        [
            InlineKeyboardButton(
                text='Интерактив',
                callback_data='TestCallbackdata2',
            )
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    await update.message.reply_text(
        text='Мы - супер организация, делаем все и сразу, помогаем людям.',
        reply_markup=keyboard,
    )
    return []


async def end(update):
    await update.message.reply_text('bye')
