from telegram.ext import ConversationHandler, CallbackQueryHandler, CommandHandler

from bot.convers_func.about_us_conversation import (go_back_to_start,
                                                    show_about_us,
                                                    show_projects
                                                    )
from bot.convers_func.main_conversation import end
from bot.keyboards.main import ABOUT_US, END
from bot.keyboards.about_us import (PROJECTS,
                                    RETURN_TO_MAIN,
                                    RETURN_TO_ABOUT_US)
from core.states import ABOUT_US_STATE, PROJECTS_STATE

about_us_conv = ConversationHandler(
    allow_reentry=True,
    entry_points=[CallbackQueryHandler(show_about_us, pattern='^' + ABOUT_US + '$')],
    states={
        ABOUT_US_STATE: [
            CallbackQueryHandler(show_projects, pattern='^' + PROJECTS + '$'),
            CallbackQueryHandler(go_back_to_start, pattern='^' + RETURN_TO_MAIN + '$'),
        ],
        PROJECTS_STATE: [
            CallbackQueryHandler(show_about_us, pattern='^' + RETURN_TO_ABOUT_US + '$'),
        ],
    },
    fallbacks=[CommandHandler(END, end)]
)
