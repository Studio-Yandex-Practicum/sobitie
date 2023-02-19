from telegram.ext import CallbackQueryHandler, ConversationHandler, CommandHandler

from bot.convers_func.about_us_conversation import about_us, projects
from bot.convers_func.support_conversation import give_support
from bot.convers_func.main_conversation import start, end
from bot.handlers.support_menu_buttons_handlers import send_donation, attend_event, go_back


conversation_handler = ConversationHandler(
    allow_reentry=True,
    entry_points=[CommandHandler('start', start)],
    states={'START_STATE': [
                CallbackQueryHandler(about_us, 'about_us'),
                CallbackQueryHandler(projects, 'projects'),
                CallbackQueryHandler(give_support, 'give_support')
                ],
            # состояние, возникающее после нажатия на кнопку "Помочь"
            'SUPPORT_STATE': [
                CallbackQueryHandler(send_donation, 'Donation'),
                CallbackQueryHandler(attend_event, 'Attend_event'),
                CallbackQueryHandler(go_back, 'Return_to_previous_page')
            ],

            'ABOUT_US_STATE': []

            },
    fallbacks=[CommandHandler('end', end)]
)















# conversation_handler = ConversationHandler(
#     allow_reentry=True,
#     entry_points=[CommandHandler('start', start)],
#     states={'FIRST': [
#                 CallbackQueryHandler(about_us, 'about_us'),
#                 CallbackQueryHandler(projects, 'projects'),
#                 ConversationHandler(
#                     allow_reentry=True,
#                     entry_points=[InlineQueryHandler(give_support, 'Помочь')],
#                     states={'SUPPORT_STATE': [
#                         CallbackQueryHandler(send_donation, 'Donation')]},
#                     fallbacks=[CommandHandler('end', end)])
#                 ]
#             },
#     fallbacks=[CommandHandler('end', end)]
# )