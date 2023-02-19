from telegram.ext import CallbackQueryHandler, ConversationHandler, CommandHandler

from bot.convers_func.about_us_conversation import about_us, projects
from bot.convers_func.main_converation import start, end


conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[CommandHandler('start', start)],
    states={'FIRST': [
                CallbackQueryHandler(about_us, 'About us'),
            ],
            'ABOUT_US': [
                CallbackQueryHandler(projects, 'Projects'),
            ]

    },
    fallbacks=[CommandHandler('end', end)],
)
