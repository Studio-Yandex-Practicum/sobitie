from telegram.ext import CallbackQueryHandler, ConversationHandler, CommandHandler

from bot.convers_func.about_us_conversation import about_us, projects
from bot.convers_func.main_converation import start, end
from bot.convers_func.support_conversation import give_support
from bot.handlers.support_menu_buttons_handlers import send_donation, attend_event, go_back


conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[CommandHandler('start', start)],
    states={'START_STATE': [
                CallbackQueryHandler(about_us, 'about_us'),
                CallbackQueryHandler(projects, 'projects'),
                CallbackQueryHandler(give_support, 'give_support')
                ],

            'SUPPORT_STATE': [
                CallbackQueryHandler(send_donation, 'Donation'),
                CallbackQueryHandler(attend_event, 'Attend_event'),
                CallbackQueryHandler(go_back, 'Return_to_previous_page')
            ],

            'ABOUT_US_STATE': [
                CallbackQueryHandler(projects, 'Projects'),
                CallbackQueryHandler(go_back, 'Return_to_previous_page'),
            ],
            'PROJECTS_STATE': [
                CallbackQueryHandler(about_us, 'Return_to_previous_page'),
            ],
            },
    fallbacks=[CommandHandler('end', end)],
)
