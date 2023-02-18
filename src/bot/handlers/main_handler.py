from telegram.ext import ConversationHandler, CommandHandler

from src.bot.convers_func.main_converation import start, end

conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[CommandHandler('start', start)],
    states={}, # Здесь сами состояния
    fallbacks=[CommandHandler('end', end)],
)