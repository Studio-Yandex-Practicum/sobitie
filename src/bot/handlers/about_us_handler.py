from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.convers_func.about_us_conversation import (go_back_to_start,
                                                    show_about_us,
                                                    show_projects
                                                    )
from bot.convers_func.main_conversation import end
from core import constants

about_us_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_about_us, pattern='^' + constants.ABOUT_US + '$')],
    states={
        constants.ABOUT_US_STATE: [
            CallbackQueryHandler(show_projects, pattern='^' + constants.PROJECTS + '$'),
            CallbackQueryHandler(go_back_to_start, pattern='^' + constants.RETURN_TO_MAIN + '$'),
        ],
        constants.PROJECTS_STATE: [
            CallbackQueryHandler(show_about_us, pattern='^' + constants.RETURN_TO_ABOUT_US + '$'),
        ],
    },
    fallbacks=[CommandHandler(constants.END, end)]
)
